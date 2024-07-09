#!/usr/bin/env python3

#----------------------------------------------------------------------
#
# remove_pcr_dup.py
#
# Copyright 2024 Simon Joly under the terms of the GNU General Public 
# License as published by the Free Software Foundation, either version 
# 3 of the License, or (at your option) any later version.
#
#
# This script is used to remove PCR duplicates of RAD-seq data when  
# a random nucleotide barcode in incorporated int he Illumina adaptors.
# It basically removes reads that have the same sequences for both 
# forward and reverse reads and optionnaly for a random nucleotide 
# index incorporated by PCR.
#
# Usage: python3 remove_pcr_dup.py -h (will show all available options)
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
    with gzip.open("nodup_"+args.read1, "wt") as outfile1:
        with gzip.open("nodup_"+args.read2, "wt") as outfile2:
            if args.index == "":
                with gzip.open(args.read1, "rt") as read1, gzip.open(args.read2, "rt") as read2:
                    fastq_iter1 = SeqIO.parse(read1, "fastq")
                    fastq_iter2 = SeqIO.parse(read2, "fastq")
                    for rec1, rec2 in zip(fastq_iter1, fastq_iter2):
                        if str(rec1.seq) not in Unique_seqs:
                            SeqIO.write(rec1, outfile1, "fastq")
                            SeqIO.write(rec2, outfile2, "fastq")
                            Unique_seqs.add(str(rec1.seq))
                        else:
                            duplicates+=1
                        total+=1
            else:
                with gzip.open(args.read1, "rt") as read1, gzip.open(args.read2, "rt") as read2, gzip.open(args.index, "rt") as index:
                    fastq_iter1 = SeqIO.parse(read1, "fastq")
                    fastq_iter2 = SeqIO.parse(read2, "fastq")
                    fastq_iter3 = SeqIO.parse(index, "fastq")
                    for rec1, rec2, ind1 in zip(fastq_iter1, fastq_iter2, fastq_iter3):
                        if (str(ind1.seq) + str(rec1.seq)) not in Unique_seqs:
                            SeqIO.write(rec1, outfile1, "fastq")
                            SeqIO.write(rec2, outfile2, "fastq")
                            Unique_seqs.add(str(ind1.seq) + str(rec1.seq))
                        else:
                            duplicates+=1
                        total+=1
    print(total," sequences in file\n",duplicates," duplicates (",round(duplicates/total*100,2),"%)")

def ParseArg():
    parser = argparse.ArgumentParser(description="Remove pairs of reads that are identical. If "
        "you have a random index incorporated by PCR, identify the file containing the index with "
        "the -index argument to remove PCR duplicates. Exported files will have a \'nodup_\' prefix "
        "apprended to them.")
    parser.add_argument("-read1", dest="read1", type=str, help="forward input fastq/fasta file")
    parser.add_argument("-read2", dest="read2", type=str, help="reverse input fastq/fasta file")
    parser.add_argument("-index", dest="index", type=str, default="", help="random index file")
    return parser.parse_args()

if __name__ == '__main__':
    Main()
