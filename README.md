# TRGN510_Assignment4
**The program called ensg2hugo.py that takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has become a HUGO name. The result will change the COLUMN into "gene_name".**

## Download and Installation

**1.You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.**

**2. Homo_sapiens.GRCh37.75.gtf will be too large, thus we would use wget -O http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz.**

**3.Unzip it and git clone**
<pre>
gunzip Homo_sapiens.GRCh37.75.gtf.gz
</pre>
<pre>
git clone https://github.com/zeyuandong/TRGN510_Assignment4/ 
</pre>

## Use it

** Run the programe ```./ensg2hugo.py -f[0-9] Your_file.csv >Your_file.hugo.csv```, an option “-f [0-9]” where -f2 would pick the 2nd column. If there is no “-f” then the first column is used.**

## Dependencies

**1.wget**

**2.re**

**3.sys**

**4.pandas**

**5.dictionary**


## Contact

**Zeyuan Dong**

**zeyuando@usc.edu**
 
