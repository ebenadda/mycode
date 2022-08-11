#!/usr/bin/env python3

'''A program that prompts the user for a value (1 through n), then returns a quick synopsis of a book or movie in that series.
Harry Potter
Hobbit & Lord of the Rings
Chronicles of Narnia'''

bookid = input("Input a number 1 through 3: ")

#if Harry Potter Selected
if bookid == "1": 
    print("You selected Harry Potter. Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.")

#if Hobbit and Lord of the rings selected
elif bookid == "2":
    print("You just selected Hobbit and Lord of the Rings. One of the most magical epic adventures in motion picture history, Peter Jackson adapted the cinematic trilogy from the enduringly beloved novel, The Hobbit, by J.R.R. Tolkien.")

#if Chronicles of Narnia selected
elif bookid == "3":
    print("You selected Chronicles of Narnia, the greatest collection!!! The Chronicles of Narnia is a series of seven fantasy novels by British author C. S. Lewis. Illustrated by Pauline Baynes and originally published between 1950 and 1956, The Chronicles of Narnia has been adapted for radio, television, the stage, film and video games.")


#catch all sentence
else:
    print(" Your selection is invalid. Please make a selection between 1 and 3.")


