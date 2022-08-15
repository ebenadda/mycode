#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

#creating a for loop to iterate over netifaces.interfaces()
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') # This statement wil always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')  # This statement will always print IP without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except: # This is a new line
        print('Could not collect adapter information') # Print an error message



