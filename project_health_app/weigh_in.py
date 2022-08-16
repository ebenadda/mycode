#!/usr/bin/env python3

''' Atla3 | Ebenezer Addae
This app is part of a project for my python class.
It takes in user values and calcultes the MBI for the user.'''

#Imports
from datetime import date
from datetime import datetime

#Generate date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Generate date
today = date.today()

#Ask user for their name
user = input("What is your name?")

#Print welcome message
print(f'\nWelcome {user}, we are happy to help you stay healthy.')

print('Answer a few questions to get started.')

#Ask user for their weight
us_weight = input("\nPlease input your weight in kilos: ")

#Ask user for their height
us_height = input("\nPlease input your height in meters: ")

#Calculate BMI
BMI = (int(us_weight)/(int(us_height)*int(us_height)))

#Report Calculated BMI to user
print(f'\n{user}, Based on the information you provided, your BMI is {BMI} kg/m\u00b2')

if (BMI >= 18.5 and BMI <= 24.9):
    print(f'{user}, your BMI is within the normal range. Keep up with your healthy habits.')
elif BMI <18.5:
    print(f'Your BMI of {BMI} is lower than expected.')
    print(f'The normal range of BMI is 18.5 and 24.9!')
    print('Lets get to work to get you healthy')
else:
    print(f"Your BMI of {BMI} is higher than the normal range of 18.5 and 24.9!")
    print('Follow our healthy habbits guide for ways to get healthier')

#print date and time stamp
print(f'\nOn {today} at {current_time}, you checked your BMI and found it to be {BMI}')
