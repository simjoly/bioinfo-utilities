#!/usr/bin/env python3

#----------------------------------------------------------------------
#
# remove_dup.py
#
# Copyright 2024 Simon Joly under the terms of the GNU General Public 
# License as published by the Free Software Foundation, either version 
# 3 of the License, or (at your option) any later version.
#
#
# This script is used to remove PCR duplicates of RAD-seq data when  
# a random nucleotide barcode in incorporated int he Illumina adaptors.
# It basically removes reads that have the same sequences for both 
# forward and reverse reads.
#
# Usage: python3 remove_dup.py -h (will show all available options)
#
#----------------------------------------------------------------------

from Bio import SeqIO
import argparse
import gzip

def Main():
    Unique_seqs = set()
    args = ParseArg()
    duplicates = 0
    total = 0
    with gzip.open("nodup_"+args.input1, "wt") as outfile1:
        with gzip.open("nodup_"+args.input2, "wt") as outfile2:
            with gzip.open(args.input1, "rt") as input1, gzip.open(args.input2, "rt") as input2:
                fastq_iter1 = SeqIO.parse(input1, "fastq")
                fastq_iter2 = SeqIO.parse(input2, "fastq")
                for rec1, rec2 in zip(fastq_iter1, fastq_iter2):
                    if str(rec1.seq) not in Unique_seqs:
                        SeqIO.write(rec1, outfile1, "fastq")
                        SeqIO.write(rec2, outfile2, "fastq")
                        Unique_seqs.add(str(rec1.seq))
                    else:
                        duplicates+=1
                    total+=1
    print(total," sequences in file\n",duplicates," duplicates (",duplicates/total*100,"%)")

def ParseArg():
    parser = argparse.ArgumentParser(description="Remove duplicated reads which have same sequences for both forward and reverse reads. Choose the one appears first.")
    parser.add_argument("input1", type=str, help="forward input fastq/fasta file")
    parser.add_argument("input2", type=str, help="reverse input fastq/fasta file")
    return parser.parse_args()

if __name__ == '__main__':
    Main()
