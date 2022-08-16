!/usr/bin/env python3

import csv

with open('bmidata', 'w+') as data:
    myData = csv.writer(data)
    myData.writerow(['date', 'time', 'name', 'weight', 'height', 'bmi'



#ask user for their name
#user = input("What is your name?")

#Print welcome message
#print(f'\nWelcome {user}, we are happy to help you stay healthy.')

#print('Answer a few questions to get started.')

