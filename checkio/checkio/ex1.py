#!/usr/bin/python

#This exercise is the Fizz buzz test
#This was the top ranked for clarity 


def checkio(number):
    if number % 15 == 0: 
        return "Fizz Buzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)
