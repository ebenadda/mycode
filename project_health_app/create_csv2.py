#!/usr/bin/env python3

#Importing needed modules
import csv
from datetime import datetime
from datetime import date

#Initiate csv function
def create_csv(rows):

    #open csv in r+ mode
    with open('bmi_data.csv', 'a+', newline='') as file:

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
    #run = input("Do you want to check your BMI today? Type Yes or No:- ")
    #run = run.lower()  
    
    # lists to store the user data
    val = []
  
    # Taking inputs from the user
    name = input("Enter your name:- ")
    
    weight = input("Enter your weight in kilos:- ")
    height = input("Enter your height in meters:- ")

    #Generate date
    today = date.today()
    
    #Generate date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Appending the inputs in a list
    val.append(today)
    val.append(current_time)
    val.append(name)
    val.append(age)
    val.append(weight)
    val.append(height)

    #Time setter to remind user of next time to come take test instead
    # If user enters 'no' then the will loop will break
    run = input("Do you want to check the BMI of another person? Type Yes or No:- ")
    run = run.lower()


     # Adding the stored data in rows list
    rows.append(val)

# Calling function to create csv file
create_csv(rows)
