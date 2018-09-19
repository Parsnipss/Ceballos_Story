"""
Write a program that will generate a random number between 1 and 100.
Then have the user guess what the number is and determine if that number is above or below it.
"""

from random import *

print("An integer has been randomly selected between 1 and 100.")

answer = randint (1, 100)

def numGuess():
    
    while True:
        
        try:
            
            guess = int(input("Please input a guess: "))
            
            if guess > 100 or guess < 1:
                print("That value is not within the range given!")
                continue
            
            if guess == answer:
                print("Your guess, " + str(guess) + ", was correct!")
                break
            
            elif guess < answer:
                print("Your guess, " + str(guess) + ", is less than the answer!")
            
            elif guess > answer:
                print("Your guess, " + str(guess) + ", is greater than the answer!")
        
        except ValueError:
            print("This is not an integer!")

numGuess()