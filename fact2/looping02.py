#!/usr/bin/env python3

'''Alta3 Research
    For - using a files lines as a source for the for-loop'''

#Open file in read mode
dnsfile = open('dnsservers.txt', 'r')

#Create the list of lines
dnslist = dnsfile.readlines()

#loop over lines
for svr in dnslist:
    #print and end without new line
    print(svr, end="")

#close the file 
dnsfile.close()
