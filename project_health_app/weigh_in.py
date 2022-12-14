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

val = []
#Generate date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Generate date
today = date.today()
name = ''
age = ''
height = ''
weight = ''
BMI = ''

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
    data.to_csv("bmi_data5.csv", index=False)

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
    df = pd.read_csv("bmi_data3.csv")

    # Plot the line graph with the specified labels
    df.plot(x='date',y='bmi',xticks=df.index)
    plt.title('BMI Change Over Time')
    plt.xlabel('Date')
    plt.ylabel('BMI kg/m\u00b2')
    #plt.show()
    
    #Save the graph to a desired location
    #plt.savefig('/home/student/static/bmi_graph88888888.png')
    plt.savefig('/home/student/mycode/project_health_app/bmi_graph.png')
    

# list that stores the values of the row
rows = []

# while loop to take inputs from the user
#run  = ' '
#while run != 'no':
    # lists to store the user data
   # val = []

#Take user information
def get_user_info():
    global name, age, weight, height
    #run = ' '
    while True:
        # lists to store the user data
   #     val = []
        try:
            name = input("Please type your name in alphabets:-")
            if type(name) is not str:
                print("Name must be a string")
                continue 
            name = name.capitalize()
            if name.isalpha() is True:
                print(f'\nWelcome {name}!')
                try:
                    age = int(input("\nPleae enter your age:- "))
                    weight = float(input("\nPlease input your weight in kilos: "))
                    height = float(input("\nPlease input your height in meters: "))
                    if 0 < age and 0 < weight and 0 < height < 150:
                        return age, weight, height
                        break
                except ValueError:
                    print('\nInvalid age, height or weight.')
            break
        except:
            print("\nOnly alphabets allowed for name.\n")
        break
'''run = input("Do you want to check the BMI of another person? Type Yes or No:- ")
        run = run.lower()
        try:
        age = int(input("\nPleae enter your age:- "))
        weight = float(input("\nPlease input your weight in kilos: "))
        height = float(input("\nPlease input your height in meters: "))
        if 0 < age and 0 < weight and 0 < height < 150:
            return age, weight, height
        else:
            raise ValueError('Invalid age, height or weight. Lets try again.')
    except ValueError:
       print('\nInvalid age, height or weight.')      
        
   # run = input("Do you want to check the BMI of another person? Type Yes or No:- ")
    #run = run.lower()'''



#Calculate BMI
def calculate_bmi():
    global BMI, age, weight, height
    age, weight, height = get_user_info()
    BMI = round((weight/(height*height)), 1)

    
    #Generate date
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")

    #Generate date
    #today = date.today()

    # Appending the inputs and calculations in a list
    append_input()

    #Report Calculated BMI to user
    print(f'\n{name}, Based on the information you provided, your BMI is {BMI} kg/m\u00b2')

    if 24.9 >= BMI >= 18.5:
        print(f'\n{name}, your BMI is within the normal range of 18.5 to 24.9.')
    elif BMI <18.5:
        print(f'\nYour BMI of {BMI} is lower than expected.')
        print('\nThe normal range of BMI is 18.5 and 24.9!')
        print('\nLets get to work to get you healthy')
    else:
        print(f"\nYour BMI of {BMI} is higher than the normal range of 18.5 and 24.9!")
        print('Follow our healthy habbits guide for ways to get healthier')

    #print date and time stamp
    print(f'\nOn {today} at {current_time}, you checked your BMI and found it to be {BMI}')

    #Time setter to remind user of next time to come take test instead
    # If user enters 'no' then the will loop will break
    #run = input("Do you want to check the BMI of another person? Type Yes or No:- ")
    #run = run.lower()


    # Adding the stored data in rows list
    rows.append(val)

#Call User inuput function
#get_user_info()

#cal
calculate_bmi()

#call on function to create_csv function
create_csv()

#Call function to append header
append_header()

#Call function to calculate graph
graphin()

