import random  #All imports should be first

gameExit = False  #Assigns the status of exiting the game as False
acc = 6  #Lives Variable as Accumulator
answer = random.randint(1, 100)  #Random answer every game

#Intro, outside loop so it is not repeated
print ("A random integer has been selected from 1 - 100.")

while (gameExit == True):  #Exits the program
  break

while (gameExit == False):
  if (acc <= 0):  #Checks for lives
    print("You are out of lives!")
    print("The number was: " + str(answer))
    gameExit = True
    continue
  try:
    guess = int(input("Please guess: "))
    if (guess > 100 or guess < 1):  #Checks for number in range
      print ("This value is ouside the range! You will not lose a life.")
      continue
    if (guess == answer):  #Main guess statements
      print ("You win!")
      gameExit = True
    elif (guess < answer):
      print ("That number is lower than the answer!")
      acc = acc -1
      print ("Lives left: " + str(acc))
    elif (guess > answer):
      print ("That number is higher than the answer!")
      acc = acc -1
      print ("Lives left: " + str(acc))
  except ValueError:  #Catchs non-integers
    print("That is not an integer! You will not lose a life.")