Usage: ``` $python fastagrep.py [-i fasta file] [-k key] [-o output file] ```



### ABOUT fastaGrep
FastaGrep is a python application, for exporting fasta format data sets of genomes, which names match a keyword.

This program needs 3 arguments/option to run.
```
-o --output - Defines the name of the output filename [fasta format][default = fastaGrep.out]
-i --input - Defines the input filename, which will be used to extract data [fasta format]
-k --key - a keyword to apply a "grep" in input file.
```

### EXAMPLE
Lets say that, there is a fasta-format file, which contains the genomes of some viral elements. 
We want to collect the data of entries which have the keyword ERV on the title and save them in a fasta format file.

For this procedure we run
```
$ python fastagrep.py -i viralgenome.fasta -k ERV -o viral.ERV.fasta
```
Now at ``` viral.ERV.fasta ``` file we have only the entries with names that match ERV.



### VERSION CHANGELOG
```console
-0.2.1	-	CURRENT
+ arguments as options
+ output is an argument. there is no need for redirection
```


### Contact
Contact me at skarisg@gmail.com or ioannis.kutsukos@gmail.com for reporting bugs or anything else! :)