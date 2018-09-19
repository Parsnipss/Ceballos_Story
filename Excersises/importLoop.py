"""
Import and Loops
"""

# import statements go FIRST! (Cannot be used before)
import time
import random

"""
for variableName in range(start, stop, step):
OR
for variables in range(stop):  * This will start at 0 and step by 1
"""

"""
for i in range (20, -6, -2):
    print('Hello ' + str(i))
"""
"""
print 10 random integers between -100 and 100
"""
    
print (random.sample(range(*sorted([-100, 100])), 10))
