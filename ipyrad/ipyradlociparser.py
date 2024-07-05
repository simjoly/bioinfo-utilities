#! /usr/bin/env python3

#----------------------------------------------------------------------
#
# ipyradlociparser
#
# Copyright 2023 Simon Joly under the terms of the GNU General Public 
# License as published by the Free Software Foundation, either version 
# 3 of the License, or (at your option) any later version.
#
#----------------------------------------------------------------------


# Import modules
import argparse
import os

# Parser
parser = argparse.ArgumentParser(description='Parse a ".loci" file from ipyrad into multiple phylip files for gene tree phylogenetic analysis')
parser.add_argument("-i","--inputfile", dest='inputfile', type=str, 
	default="infile.loci", help="Name of the input file")
parser.add_argument("-o","--outfolder", dest='outfolder', type=str, 
	default="", help="Name of the output folder (path) where the files should be saved. Ex: ./results/")
parser.add_argument("--subfolders", help="Write the output files in different subfolders", 
	action="store_true")
args = parser.parse_args()


def main():

	with open(args.inputfile) as infile:

		# prepare output file info
		outfilenumber = 1
		if args.outfolder != "":
			if not os.path.exists(args.outfolder):
				os.makedirs(args.outfolder)

		# lists to store sequence info
		seqnames = []
		sequences = []

		for line in infile:

			if line.startswith("//"):

				writeoutput(seqnames,sequences,outfilenumber)

				# prepare for new gene
				outfilenumber = outfilenumber + 1
				seqnames = []
				sequences = []

			else:

				# Get sequence info
				seqnames.append(line.split()[0])
				sequences.append(line.split()[1])


def writeoutput(seqnames,sequences,outfilenumber):

	# Prepare outputfile
	if args.outfolder != "":
		if args.subfolders:
			if not os.path.exists(args.outfolder+"/"+"gene" + str(outfilenumber)):
				os.makedirs(args.outfolder + "/" + "gene" + str(outfilenumber))
			outfilename = args.outfolder + "gene" + str(outfilenumber) + "/gene" + str(outfilenumber) + ".phy"
		else:
			outfilename = args.outfolder + "gene" + str(outfilenumber) + ".phy"
	else:
		if args.subfolders:
			if not os.path.exists("./gene" + str(outfilenumber)):
				os.makedirs("./gene" + str(outfilenumber))
			outfilename = "./gene" + str(outfilenumber) + "/gene" + str(outfilenumber) + ".phy"
		else:
			outfilename = "./gene" + str(outfilenumber) + ".phy"

	outfile = open(outfilename, "w")

	# Write output file
	longestname = max(len(s) for s in seqnames)
	outfile.write(str(len(seqnames))+" "+str(len(sequences[0]))+"\n")
	for x in range(len(seqnames)):
		outfile.write(seqnames[x].ljust(longestname+4))
		outfile.write(sequences[x]+"\n")

main()
