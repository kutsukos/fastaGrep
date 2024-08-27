Usage: ``` $python3 fastagrep.py [fasta file] [output file] [keyword]  ```



### ABOUT fastaGrep
FastaGrep is a python application, for exporting fasta format data sets of genomes, which names match a keyword.

This program needs 3 arguments/option to run.
```
- the input filename, which will be used to extract data [fasta format]
- the name of the output filename [fasta format]
- a keyword to apply a "grep" in input file
```

### EXAMPLE
Lets say that, there is a fasta-format file, which contains the genomes of some viral elements. 
We want to collect the data of entries which have the keyword ERV on the title and save them in a fasta format file.

For this procedure we run
```
$ python3 fastagrep.py viralgenome.fasta viral.ERV.fasta ERV 
```
Now at ``` viral.ERV.fasta ``` file we have only the entries with names that match ERV.





### Contact
Contact me at ioannis.kutsukos@gmail.com for reporting bugs or anything else! :)
