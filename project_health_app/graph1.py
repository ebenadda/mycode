#!/usr/bin/python3
"""Russell Zachary Feeser | Alta3 Research
Learning to work with Time-based indexing in pandas
"""

import pandas as pd

import matplotlib
matplotlib.use('Agg') # required to generate images without a window appearing

# does not appear to be necessary
#import matplotlib.pyplot as plt

import seaborn as sns

def main():
    """run-time code"""
    # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
    opsd_daily = pd.read_csv('bmi_data3.csv', index_col=0, parse_dates=True)

    # add some additional columns to our data
    # Add columns with year, month, and weekday name
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    # Use seaborn style defaults and set the default figure size
    sns.set(rc={'figure.figsize':(11, 4)})


    ### LINE PLOT - create a line plot of the full time series of daily network consumption, using the DataFrame’s plot() method.
    netlineplot = opsd_daily['Consumption'].plot(linewidth=0.5)

    # save out this figure
    fig = netlineplot.get_figure()
    fig.savefig("/home/student/static/linePlot.png")

