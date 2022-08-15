#!/usr/bin/env python3

'''writing a program that reads the data in csv_users.txt, and uses it to produce 26 separate admin.rc files. '''

#standard library import
import csv

#open the csv file
with open("csv_users.txt", "r") as csvfile:
    #initialize counter
    i = 0

    #loop across the file
    for row in csv.reader(csvfile):
        i += 1 # increase count by 1
        filename = f"admin.rc{i}"

        # open files and append the counted lines in the file
        with open(filename, "w") as rcfile:
            # use the standard library print function to print our data 
            #out to the open file open rcfile (open in write mode)
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

# display this to the screen when all of the looping is over
print("admin.rc files created!")
