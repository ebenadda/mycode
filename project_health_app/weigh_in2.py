#!/usr/bin/env python3

''' Atla3 | Ebenezer Addae
This app is part of a project for my python class.
It takes in user values and calcultes the MBI for the user.'''

#Imports
from datetime import date
from datetime import datetime
import csv
import pandas as pd
from matplotlib import pyplot as plt

#Inititiate csv function
def create_csv():
    '''This function creates the csv file into which user information is stored.
        The csv file is first opened in append mode
        with the option to add a new line to it.
        Then the csv writer is used to write the rows of
        the file by adding the val as input is entered by the user '''
    #open csv in r+ mode
    with open('bmi_data1.csv', 'a+', newline='',  encoding='utf8') as file:

        #create the csv writer
       # file_write = csv.writer(file)

        #Iterate over the data in the row
        for entry in rows:
            csv.writer(file).writerow(entry)

#Append header to CSV file
def append_header():
    '''This function appends a header to the csv table'''
    data = pd.read_csv("bmi_data1.csv",
            names = ['date',
                'time',
                'name',
                'age',
                'weight',
                'height',
                'bmi'])
    #convert back to csv without index
    data.to_csv("bmi_data7.csv", index=False)

    #print the new file
    print(data)

#Append input to list
def append_input():
    '''This function appends each of the user input to the val in the row'''
    #Append input data
    val.append(today)
    val.append(current_time)
    val.append(name)
    val.append(age)
    val.append(weight)
    val.append(height)
    val.append(BMI)

#define matplotlib function to plot graph
def graphin():
    '''This function plots the bmi over a period of time'''
    # Set the figure size and layout
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # Read a CSV file
    df = pd.read_csv("bmi_data7.csv")

    # Plot the line graph with the specified labels
    df.plot(x='date',y='bmi',xticks=df.index)
    plt.title('BMI Change Over Time')
    plt.xlabel('Date')
    plt.ylabel('BMI kg/m\u00b2')
    #plt.show()

    #Save the graph to a desired location
    #plt.savefig('/home/student/static/bmi_graph8.png')
    plt.savefig('/home/student/mycode/project_health_app/bmi_graph1.png')

# list that stores the values of the row
rows = []

# while loop to take inputs from the user
run  = ' '
while run != 'no':
    # lists to store the user data
    val = []

    #Take user information
    while True:
        name = input("\nWhat is your name?")
        name = name.capitalize()
        if name.isalpha() is True:
            print(f'\nWelcome {name}, we are happy to help you stay healthy.')
            break
        print("\nName has to be in alphabets only.")

    age = int(input("\nPlease enter your age:- "))

    print('\nAnswer a couple more questions to get going.')

    #Ask user for their weight
    weight = float(input("\nPlease input your weight in kilos: "))

    #Ask user for their height
    height = float(input("\nPlease input your height in meters: "))

    #Calculate BMI
    BMI = round((weight/(height*height)), 1)

    #Generate date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    #Generate date
    today = date.today()

    # Appending the inputs and calculations in a list
    append_input()

    #Report Calculated BMI to user
    print(f'\n{name}, Based on the information you provided, your BMI is {BMI} kg/m\u00b2')

    if 24.9 >= BMI >= 18.5:
        print(f'\n{name}, your BMI is within the normal range. Keep up with your healthy habits.')
    elif BMI <18.5:
        print(f'\nYour BMI of {BMI} is lower than expected.')
        print('\nThe normal range of BMI is 18.5 and 24.9!')
    else:
        print(f"\nYour BMI of {BMI} is higher than the normal range of 18.5 and 24.9!")

    #print date and time stamp
    print(f'\nOn {today} at {current_time}, you checked your BMI and found it to be {BMI}')

    #Time setter to remind user of next time to come take test instead
    # If user enters 'no' then the will loop will break
    run = input("\nDo you want to check the BMI of another person? Type Yes or No:- ")
    run = run.lower()


    # Adding the stored data in rows list
    rows.append(val)

#call on function to create_csv function
create_csv()
append_header()
graphin()
