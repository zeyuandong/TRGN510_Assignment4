#!/usr/bin/python

import sys
import fileinput
import re
import pandas as pd

if sys.argv[1][:2]=="-f":
    change = sys.argv[1][2]
    test_gene = sys.argv[2]
else:
    change = 1
    test_gene = sys.argv[1]
col_need=int(change)-1

Need_gene = {}
Genes="Homo_sapiens.GRCh37.75.gtf"
for lines in fileinput.input(Genes):
    matchGene=re.match(r'^\w+.*\sgene\s+\w+\s+\w+\s\W\s\W\s\W\s+gene_id\s\"(\w+)\"\;\sgene_name\s\"(\w+)',lines)
    if matchGene:
        ID=matchGene.group(1)
        GN=matchGene.group(2)
        Need_ID={ID:GN}
        Need_gene.update(Need_ID)
new_df={}
new_point={}
test_df= pd.read_csv(test_gene)
if test_df.columns[col_need] != 'gene_id':
    test_df.rename(columns={test_df.columns[col_need]:'gene_id'},inplace=True )
for each_lines in test_df['gene_id']:
    Point=re.sub(r'\.\w+','',each_lines)
    Point_list={each_lines:Point}
    new_point.update(Point_list)
test_df['gene_id']= test_df['gene_id'].map(new_point)
test_df['gene_id']= test_df['gene_id'].map(Need_gene)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
print(test_df)
