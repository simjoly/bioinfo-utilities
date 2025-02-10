# ipyrad scripts

## ipyradlociparser.py

Python3 script that parses a ".loci" file from ipyrad into multiple phylip files for gene tree phylogenetic analysis

#### Usage

```$>python ipyradlociparser.py -h```


## remove_pcr_dup.py

This Python3 script is used to remove PCR duplicates of RAD-seq data when a random nucleotide index in incorporated in the Illumina adaptors by PCR. It removes reads that have the same sequences for both forward and reverse reads and for a random nucleotide index incorporated by PCR. All input files must be in fastq format. A 'nodup_' prefix is added to the file names of the read1 and read2 output files.

There are two options to run the program. 

#### Separate index file

If the random index is in a separate fastq file (same order as in the files that contain the reads), you can run the program using this command:

```$>python remove_pcr_dup.py -index <indexfile> -read1 <read1file> -read2 <read2file>```

#### Index in the read1 file

If the random index is at the begining of the read1, then you can run the program with the following command:

```$>python remove_pcr_dup.py -read1 <read1file> -read2 <read2file>```

#### Get help

```$>python remove_pcr_dup.py -h```

## vcf_parser.py

Python3 script that parses a ".vcf" file in different ways, for instance by keeping only a single SNP per loci for Structure analysis.

#### Usage

```$>python vcf_parser.py -h```


