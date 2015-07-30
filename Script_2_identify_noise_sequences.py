import os
import re

#requires python 2.6
#must be run in same directory as, and only after, count_unique_seq_per_barcode_pair.sh 
#all files should look like "X*.counts"
#dir should be current dir

input_filename = ""
output_filename = "noise_sequences.fa"
outfile = open(output_filename,"w")

for filename in os.listdir("."):
    if re.search( ".counts", filename):
        input_filename = filename
        opens = open(input_filename)
        read = opens.read()
        splits = read.split("\n")
        total = 0
        for line in splits:
            
            if len(line)>1:
                splitline = line.split(" ")
                count = 0

                for tabs in splitline:
                    if not "A" in tabs:
                        if len(tabs)>0:
                            total = total + int(tabs)

        for line in splits:
            if len(line)>1:
                splitline = line.split(" ")
                for tabs in splitline:
                    if not "A" in tabs:
                        if len(tabs)>0:
                            tot_1 = total
                            tot = float(tot_1)
                            acc_1 = int(tabs)
                            acc = float(acc_1)
                            if acc*100/tot<5:
                                #print (str(acc*100/tot))  # prints the actual %
                                #print line  # will print with numerals associated
                                #print splitline[-1] #prints just barcode and seq.
                                #for each of the lines need to be removed from the all gtthn 265 etc then can repeat the rest as normal.
								outfile.write(splitline[-1] + "\n")
outfile.close()
infile.close()
