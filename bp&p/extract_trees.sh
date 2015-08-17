#!/bin/bash

# Simon Joly, 2015

# Script for extracting some trees from the tree file output of the 
# bp&p software. Basically, it will extract trees with a given number
# of species (given by the command line) and write them in nexus format
# in the file "out.trees". This tree can then be read in TreeAnnotator.

# Specify the species number to extract from (by default = 6)
numb_sp=6
if [ "$1" != "" ];then
    numb_sp="$1"
fi

echo " ->Conserving trees with $numb_sp species"

# Select the trees with exactly the number of species requested
grep "; $numb_sp $" mcmc.txt > out.txt
# Remove population size information
sed -e "s/\(.*;\) [0-9]/\1/" out.txt > temp.txt
sed -e "s/\(\#[0-9].[0-9e\-]*\)\([:;]\)/\2/g" temp.txt > temp2.txt

# Add nexus format tree information to each line 
COUNT=0
a="tree "
b=" = [&R] "
while read -r line; do
    COUNT=$(( $COUNT + 1 ))
    if [ ... ];then
    	echo $a$COUNT$b$line >> temp3.txt
    fi
done < temp2.txt

# Write output file
echo "#nexus" > out.trees
echo "begin trees;" >> out.trees
cat temp3.txt >> out.trees
echo "end;" >> out.trees
echo " ->Trees written to file out.trees\n"

# Remove temporary files.
rm temp.txt temp2.txt temp3.txt out.txt
