#!/usr/bin/env python3

#For -  looping across range()

# Standard library import
#Import uuid to generate UUIDs
import uuid


howmany =  int(input("How many UUIDs should be generated?"))

print("Generating UUIDs...")

#range is required because int cannot be looped
for rando in range(howmany):
    print(uuid.uuid1())
