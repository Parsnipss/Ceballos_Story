"""
Write a program that will generate a random number between 1 and 100.
Then have the user guess what the number is and determine if that number is above or below it.
"""

from random import *

answer = randint (1, 100)

guess = int(input("An integer was selected between 1 and 100, Please input a guess: "))

if guess == answer:
    print("Your guess, " + str(guess) + ", was correct!")
elif guess < answer:
    print("Your guess, " + str(guess) + ", is less than the answer")
elif guess > answer:
    print("Your guess, " + str(guess) + ", is greater than the answer")
    


"""
def get_int(prompt):
    while True:
        try:
            guess = int(input("An integer was selected between 1 and 100, Please input a guess: "))
            break
        except ValueError:
            print('Please enter an integer value.')
    return guess
"""



