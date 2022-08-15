#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode

configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
configlist = str(configlist).strip()
print(configlist)

## Iterate through configlist
for x in configlist:
    print(x, end="")

#configliststrip = configlist.strip(" ")

## Always close your file
configfile.close()
