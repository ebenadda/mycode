#!/usr/bin/env python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 #initialize counter

#open the file
with open("keystone.common.wsgi","r") as keystone_file:
    #loop over the lines in the file
    for line in keystone_file:
        # if the pattern appears in line
        if "- - - - -] Authorization failed" in line:
            #add 1 to the count
            loginfail += 1

#print the number of failed attempts
print("The number of failed log in attempts is", loginfail)
