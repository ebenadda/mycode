#!/usr/bin/env python3

#Use the with to open the txtfile
with open('dnsservers.txt', 'r') as dnsfile:
    # Now read the content
#    dnslines = dnsfile.readlines()

    #then loop over the lines
    for svr in dnsfile:
        #print the lines leaving the extra line spacing
        print(svr)

#there is no need to close the file because when we use with it automatically closes the file once we exit the indentation
