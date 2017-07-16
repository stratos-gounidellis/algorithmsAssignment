## Frequent itemsets

In several applications (consumer behavior, biomarkers' analysis, plagiarism detection, etc.) we need to detect frequent itemsets. One way is the algorithm of Agrawal and Srikant (Apriori algorithm). 

The baskets of items are contained in a CSV file. Each line of this file is of the following form:

```
item_1, item_2, ..., item_n
```

Τhe program runs with the following command: 

```
python a_priori.py [-n] [-p] [-o OUTPUT] support filename
```

- The -n parameter is optional. If parameter-n is given, the program will consider that the objects are numeric. Otherwise, it considers that the objects are strings.
- The -p parameter is optional. If parameter -p is given, the program considers that the minimum support given by the -s parameter is the percentage of baskets that should contain an itemset to be considered significant.
- The -o OUTPUT parameter is optional. If the -o parameter is given, the program will save the results to an output file . Otherwise, it displays the results on the screen.
- Parameter support is mandatory, as it is the minimum support, that the algorithm  will use in characterizing an itemset as frequent.
- The filename parameter is mandatory and refers to the name of the input file of the program.
