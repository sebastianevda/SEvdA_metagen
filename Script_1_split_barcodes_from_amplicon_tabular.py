import re

#runs in python 2.6
#requires assembled reads, all in same orientation, as input file
#outputs the assembled reads trimmed of bases 5' or 3' to terminal barcodes, and prints tabular file as barcode1 barcode2 amplicon without primer sequences 
#12/03/2020 - Thanks to Peter Cock ("Peter Cock" <Peter.Cock@hutton.ac.uk>) for finding an error.

input_filename = "All_with_F_and_R.fa"
output_filename = "All_with_F_and_R_and_2_barcodes_and_grthn265.fa"
Primer_1 = "CTTGAAGACCTTCTGTAAAAATG"
Primer_2 = "CTCTTAAGACGGTAGCTCG"
minlen_of_amplicon_not_including_primers = 265


infile = open(input_filename)
outfile = open(output_filename,"w")
read = infile.read()
lenad = 0
tabular = ""
split = read.split("\n")
count6 = 0
count5 = 0
count4 = 0
count3 = 0
count2 = 0
count1 = 0
countr6 = 0
countr5 = 0
countr4 = 0
countr3 = 0
countr2 = 0
countr1 = 0
for line in split:
    fbartest = 0
    rbartest = 0
    Fbar = "XXX"
    Rbar = "XXX"
    if len(line)>250:
        #print line
        searchfor = re.search(Primer_1,line,flags=0)
        end = searchfor.start()
        before_forward_primer = line[0:end]
        if len(before_forward_primer) is 6:
            count6 = count6 + 1
            if line.startswith("AA"):
                Fbar = before_forward_primer[2:]
                fbartest = fbartest +1
        if len(before_forward_primer) is 5:
            count5 = count5 + 1
            if line.startswith("A"):
                Fbar = before_forward_primer[1:]
                fbartest = fbartest +1
        if len(before_forward_primer) is 4:
            Fbar = before_forward_primer[:]
            fbartest = fbartest +1
            count4 = count4 + 1
        if len(before_forward_primer) is 3:
            count3 = count3 + 1
        if len(before_forward_primer) is 2:
            count2 = count2 + 1
        if len(before_forward_primer) is 1:
            count1 = count1 + 1                                                

        searchrev = re.search(Primer_2,line,flags=0)
        start = searchrev.end()
        after_rev_primer = line[start:]
        if len(after_rev_primer) is 6:
            countr6 = countr6 + 1
            Rbar = after_rev_primer[:6-2]
            rbartest = rbartest +1
        if len(after_rev_primer) is 5:
            Rbar = after_rev_primer[:5-1]
            rbartest = rbartest +1
            countr5 = countr5 + 1
        if len(after_rev_primer) is 4:
            Rbar = after_rev_primer[:4]
            rbartest = rbartest +1
            countr4 = countr4 + 1
        if len(after_rev_primer) is 3:
            countr3 = countr3 + 1
        if len(after_rev_primer) is 2:
            countr2 = countr2 + 1
        if len(after_rev_primer) is 1:
            countr1 = countr1 + 1



            
        if rbartest > 0:
            if fbartest > 0:
                amplicon_between_primers = line[searchfor.end():searchrev.start()]
                #print len(amplicon_between_primers)
                if len(amplicon_between_primers) >= minlen_of_amplicon_not_including_primers:
                    outfile.write(Fbar + "\t" + Rbar + "\t" + amplicon_between_primers + "\n")
                
print "count f6 = " + str(count6)
print "count f5 = " + str(count5)
print "count f4 = " + str(count4)
print "count f3 = " + str(count3)
print "count f2 = " + str(count2)
print "count f1 = " + str(count1)

print "count r6 = " + str(countr6)
print "count r5 = " + str(countr5)
print "count r4 = " + str(countr4)
print "count r3 = " + str(countr3)
print "count r2 = " + str(countr2)
print "count r1 = " + str(countr1)
outfile.close()
infile.close()
