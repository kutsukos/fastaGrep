Usage: $python fastagrep.py [-i fasta file] [-k key] [-o output file]



#ABOUT fastaGrep
FastaGrep is a python application for exporting fasta format data sets of genomes which names match a keyword.

This program needs 3 arguments/option to run.
-o --output - Defines the name of the output filename [fasta format][default = fastaGrep.out]
-i --input - Defines the input filename, which will be used to extract data [fasta format]
-k --key - a keyword to apply a "grep" in input file.


#EXAMPLE
We have a fasta file, which contains the genomes of some viral elements. 
We want to search for the genomes of entries which have the word ERV on the title and save them in a fasta format file, so we run:
    >$ python fastagrep.py -i viralgenome.fasta -k ERV -o viral.ERV.fasta
Now at viral.ERV.fasta file we have only the entries with names that match ERV.



#VERSION CHANGELOG
-0.2.1	-	CURRENT
+ arguments as options
+ output is an argument. there is no need for redirection



#Contact
Contact me at skarisg@gmail.com or ioannis.kutsukos@gmail.com for reporting bugs or anything else! :)