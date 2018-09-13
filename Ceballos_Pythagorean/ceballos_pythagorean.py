"""
Write a program that will ask the user to
enter their name and respond with a greeting using this name. (3 points)
"""

name = input("What is your name? ")
print ("Hello " + name + ", you are now cleared for hypotenuse calculation.")

"""
Next your program will ask them to enter the lengths of the legs of a right triangle a and
b. We will use these to compute the length of the hypotenuse: c. (3 points)
"""

a = float(input("Value for leg one (a): "))
b = float(input("Value for leg two (b): "))

"""
Compute the length of the hypotenuse and then return the result in a print statement.
(*Don’t only print the value, make sure you add both strings and floats in your statement).
(5 points)
"""

print("a^2 = " + str(a**2))
print("b^2 = " + str(b**2))
print("The hypotenuse (c) is equal to: " + str(((a**2)+(b**2))**(1/2)))