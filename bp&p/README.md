# bp&p scripts

Simon Joly, 2015

## extract_trees.sh

Schell script for extracting trees from the tree file output of the bp&p software. Basically, it will extract trees with a given number of species (given by the command line) from the file "mcmc.txt" and write them in nexus format in the file "out.trees". This tree can then be read in TreeAnnotator.

#### Usage

```$>sh extract_trees.sh <number_of_species>```

where the <number_of_species> is the number of species you wish to have in the trees kept by the script.
