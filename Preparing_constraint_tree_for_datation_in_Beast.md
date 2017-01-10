# Preparing a constraint tree for a datation analysis in BEAST

A frequent problem when performing a datation analysis in BEAST is to get an analysis to fail because of an undefined likelihood. For instance, you could get the following log message:

```
The initial posterior is zero: 
  CompoundLikelihood(compoundModel)=(
    Gamma(tmrca(Eudicots))=-48.9448, 
    Gamma(tmrca(Fagales))=-3.0618, 
    Gamma(tmrca(Paleotaxus))=-2.6452, 
    Gamma(tmrca(Sapindopsis))=-Inf, 
 ...
 ```

 The `-Inf` value indicates and impossible probability. This is likely because the likelihood is not defined given the prior. This can occur, for instance, if the date for a given clade (here Sapindopsis) is outside the range of possible values as defined by the prior.

 A solution for this is to provide BEAST with an input tree that is compatible with the priors. This can be done in R.

First, load the tree in R.

 ```r
# get tree
library(ape)
tree <- read.nexus(file.choose())
```

Then you need to get the node to which you want to apply age constraints. For the example given above with Sapindopsis, you can get the node number with the function `mrca(tree)` that returns the most recent common ancestor (mrca) for the taxa given to the function. For instance,

```r
# Get node number for different constraints

# 1. Sapindopsis = 87
mrca(tree)["Nelumbo_nucifera","Platanus_occidentalis"]
```

You can also do this for other nodes as well.

```r
# 2. Tricolpate pollen = 86
mrca(tree)["Fagus_grandifolia","Platanus_occidentalis"]
```

Now, you need to assign an a minimum and maximum age for each node. Make sure to use dates that are compatible with the prior you used in Beauti. The easiest was is to make 2 vectors: one for the minimum and one for the maximum ages. You will also need a vector of node numbers.

```r
# vector of node numbers that you want to calibrate
nodes <- c(86,87)
# vector of min. ages
min.ages <- c(125,105)
# vector of max. ages
max.ages <- c(140,115)
```

With this, you assign a minimum age of 125 and a maximum age of 140 to the node 86.

Finaly, you can use the fonction chronopl to generate a chronogram that is compatible with the above constraints. Of course, the tree has to be compatible with these.

```r
tree.pl <- chronopl(tree, lambda=1,
                age.min=min.ages, age.max=max.ages, node=nodes, S=3064, tol=1e-8)
plot(tree.pl)
```

Output the ultrametric trees.

```
# write trees in newick and nexus formats
write.tree(tree.pl, file="starting_tree_pl2.nwk")
write.nexus(tree.pl, file="starting_tree_pl2.tre")
```