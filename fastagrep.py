from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="infile",
                  help="read sequences from FILE", metavar="FILE")
parser.add_option("-o", "--output", dest="outfile", default="fastaGrep.out",
                  help="write output to FILE")
parser.add_option("-k", "--key", dest="word",
                  help="key used for grep")

(options, args) = parser.parse_args()
print "Fasta Grep 0.2.1"
print "Reading sequences from: ", options.infile
print "Writing selected sequences to: ",options.outfile
print "Key for selecting sequences: ",options.word


filename=options.infile
grep=options.word    #word we are searching in fasta names
nameIDI='>'         #indicator that a line contains name or desc of a genome
outputfile=options.outfile

file = open(filename, "r")
outFile = open(outputfile, "w")

flag=False
for line in file:
    if(nameIDI in line):
        if(grep in line):   #that means that we need the following genome until the next (>)
            #sys.stdout.write(line)     #when this program used to write in stdout
            outFile.write(line)
            flag=True
        else:
            flag=False
    else:
        if(flag==True):
            #sys.stdout.write(line)
            outFile.write(line)
file.close()
outFile.close()