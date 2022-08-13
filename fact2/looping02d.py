#!/usr/bin/env python3
'''This app is going to seperate the servers into those that end with .org and .com. The two ending types would be put in two different files: servers_com.txt and servers_org.txt'''

#We first have to open the file using the with command
with open('dnsservers.txt', 'r') as servers:
    #loop across the servers
    for svr in servers:
        #then we delete the extra lines at the end of each svr
        svr = svr.rstrip('\n')


#if svnl ends with .com, put it in a different folder
        if svr.endswith('com'):
            with open('servers_com.txt', 'a') as newseverlist:
                newseverlist.write(svr + '\n')

#if svrnl ends with .org
        if svr.endswith('org'):
            with open('servers_org.txt', 'a') as newseverlist:
                newseverlist.write(svr + '\n')

#that is it. we should have two new folders in our fact2 folder with the names we created above. 
