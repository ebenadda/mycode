#!/usr/bin/env python3

'''this app loops over a log file to count the number of successful and failed login attempts'''

#initialize count for successful and failed attempts
success = 0
fail = 0
#open file to read content
with open("keystone.common.wsgi","r") as keystone_file:

    #loop over the lines to find success patterns
    for line in keystone_file:
        if  "- - - - -] Loaded" in line:
            #add to a count to the successful attempts
            success += 1
        elif "- - - - -] Authorization failed" in line:
            # add a count to the failed attempts
            fail += 1

#print the number of succesful attempts
print("the number of succesfful login attempts are", success)

#print the number of failed attempts
print("the number of failed login attempts are", fail)

#print IP address of the user with failed login
print(line.split(" ")[-1])
