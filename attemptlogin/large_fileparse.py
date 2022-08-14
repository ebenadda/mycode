#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0

# open the file for reading
keystone_file =  open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over the file
for line in keystone_file:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("The number of failed log in attempts is", loginfail)

keystone_file.close()
