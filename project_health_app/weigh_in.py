#!/usr/bin/env python3

''' Atla3 | Ebenezer Addae
This app is part of a project for my python class.
It takes in user values and calcultes the MBI for the user.'''

#Imports
from datetime import date
from datetime import datetime
import csv

#Inititiate csv function
def create_csv(rows):
    #open csv in r+ mode
    with open('bmi_data1.csv', 'a+', newline='') as file:

        #create the csv writer
        file_write = csv.writer(file)
        
       # file_write.writerow(['date', 'time', 'name', 'age', 'weight', 'height'])
        
        #Iterate over the data in the row
        for val in rows:
            file_write.writerow(val)

# list that store the values of the rows
rows = []

# while loop to take
# inputs from the user
run = ''
while run != 'no':
    
    # lists to store the user data
    val = []

    #Take user information
    name = input("What is your name?")
    age = input("Enter your age:- ")

    #Print welcome message
    print(f'\nWelcome {user}, we are happy to help you stay healthy.')
    print('Answer a couple more questions to get going.')

    #Ask user for their weight
    weight = input("\nPlease input your weight in kilos: ")

    #Ask user for their height
    height = input("\nPlease input your height in meters: ")

    #Calculate BMI
    BMI = (int(us_weight)/(int(us_height)*int(us_height)))

    #Generate date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    #Generate date
    today = date.today()

    # Appending the inputs and calculations in a list
    val.append(today)
    val.append(current_time)
    val.append(name)
    val.append(age)
    val.append(weight)
    val.append(height)
    val.append(BMI)


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

    #Time setter to remind user of next time to come take test instead
    # If user enters 'no' then the will loop will break
    run = input("Do you want to check the BMI of another person? Type Yes or No:- ")
    run = run.lower()


    # Adding the stored data in rows list
    rows.append(val)

#call on function to create_csv function
create_csv(rows)
