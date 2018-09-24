#Use a function to even odd 10 times
import random

def numBig():  #Insert directions
    even = 0
    for i in range(10):
        random_number = random.randint(0,100)
        if random_number % 2 == 0:
            print("This number, " + str(random_number) + ", is even!")
            even = even + 1
        elif random_number % 2 == 1:
            print("This number, " + str(random_number) + ", is odd!")
    print ("There were " + str(even) + " even numbers.")
    print ("Conversly. there were " + str(10-even) + " odd numbers.")
    print ("If this number ---> " + str(even + (10-even)) + " <--- is not 1000, you do not exist within reality.")

def greeter():
    name = input("Hello! What is your name? ")
    print("Hello, " + name + ", today is a great day!")

def vote():
    age = int(input("Hello! How old are you? "))
    return age
