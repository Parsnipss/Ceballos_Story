# 1. Print out a random number bewteen -5 and 5
import random
"""
print ("A random number bewteen -5 and 5 would be: " + str(random.randint(-5, 5)))
"""

# 2. Print out a random integer between 0 and 100, 50 times
"""
for i in range(500):
    print (random.randint(0, 100))
"""

# 3. Print a random number and determin if it is even or odd
"""
rum = random.randint(-100,100)

print ("The random number is: " + str(rum))

if rum %2 == 0:
    print("The number, " + str(rum) + ", is even!")
elif rum %2 == 1:
    print("The number, " + str(rum) + ", is odd!")
"""
    
# 4. Print 10 random numbers and determine if they are even or odd along the way
even = 0

for i in range(1000):
    random_number = random.randint(0,100)
    if random_number % 2 == 0:
        print("This number, " + str(random_number) + ", is even!")
        even = even + 1
    elif random_number % 2 == 1:
        print("This number, " + str(random_number) + ", is odd!")
        
print ("There were " + str(even) + " even numbers.")
print ("Conversly. there were " + str(1000-even) + " odd numbers.")
print ("If this number ---> " + str(even + (1000-even)) + " <--- is not 1000, you do not exist within reality.")

# 5. ADD all the evens and tell how many