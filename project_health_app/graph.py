#!/usr/bin/env python3

'''Plotting graph'''
import pandas as pd
from matplotlib import pyplot as plt

def graphin():
    '''This function plots the bmi over a period of time'''
    # Set the figure size and layout
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # Make a list of columns
    columns = ['bmi']
    
    # Read a CSV file
    df = pd.read_csv("bmi_data3.csv", usecols=columns)

    # Plot the line graph with the specified labels
    df.plot()
    plt.title('BMI Change Over Time')
    plt.xlabel('Date')
    plt.ylabel('BMI kg/m\u00b2')
    #plt.show()
    
    #Save the graph to a desired location
    plt.savefig('/home/student/static/bmi_graph7.png')
    #plt.savefig('/home/student/mycode/project_health_app/bmi_graph4.png')
    
graphin()
