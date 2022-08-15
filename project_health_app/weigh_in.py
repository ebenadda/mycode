#!/usr/bin/env python3

''' Atla3 | Ebenezer Addae
This app is part of a project for my python class.
It takes in user values and calcultes the MBI for the user.'''

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
