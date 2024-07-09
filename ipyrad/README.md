# ipyrad scripts

## ipyradlociparser.py

Python3 script that parses a ".loci" file from ipyrad into multiple phylip files for gene tree phylogenetic analysis

#### Usage

```$>python ipyradlociparser.py -h```


## remove_dup.py

This Python3 script is used to remove PCR duplicates of RAD-seq data when a random nucleotide index in incorporated in the Illumina adaptors by PCR. It basically removes reads that have the same sequences for both forward and reverse reads.

#### Usage

```$>python remove_pcr_dup.py -h```


## vcf_parser.py

Python3 script that parses a ".vcf" file in different ways, for instance by keeping only a single SNP per loci for Structure analysis.

#### Usage

```$>python vcf_parser.py -h```


