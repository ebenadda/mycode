#!/usr/bin/env python3

#This app reads the soldier list file

# We first have to open the file in read mode
solfile = open("soldiercity.txt", "r")

# Then we read the file
readsfile = solfile.readlines()

#We then loop over the lines in the file
for city in readsfile:
    # and print each line
    print(city)

#Then finally close the file
solfile.close()
