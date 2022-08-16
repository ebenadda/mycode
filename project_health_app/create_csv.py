#!/usr/bin/env python3

import csv
import os
 

with open('bmi.csv', 'w+') as data:
    myData = csv.writer(data)
    myData.writerow(['date', 'time', 'name', 'weight', 'height', 'bmi'])

    current_date = 20220816
    current_time = 1854
    date = input(current_date)
    time = input(current_time)
    user_name = input("What is your name?")
    weight = input("weight")
    height = input("height")
    bmi = input("bmi")
    myData.writerow([date, time, user_name, weight, height, bmi])
