#!/usr/bin/env python3
## create file object in "r"ead mode

filename = input("Type the name of file you want to open:")

with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    #initialize counter
    i = 0
 
    # iterate over lines
    for x in configlist:
        if "vlan" or "name" in line:
            i += 1
#print("the number of lines in the file is", i-1)

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

print("\nthe number of lines in the file is", i-1)
