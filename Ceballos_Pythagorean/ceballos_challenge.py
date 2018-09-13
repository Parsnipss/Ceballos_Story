name = input("What is your name? ")
print ("Hello " + name + ", you are now cleared for triangle inspection.")

#Legs of triangle

a = float(input("Value for leg one (a): "))
b = float(input("Value for leg two (b): "))
c = ((a**2)+(b**2))**(1/2)

#Values

print("a^2 = " + str(a**2))
print("b^2 = " + str(b**2))
print("c^2 = " + str(c**2))

#Triangle check

if (a + b < c):
    print ("This is not a triangle!")
elif ((a**2) + (b**2) == (c**2)):
    print ("This is a right triangle!")
elif ((a**2) + (b**2) < (c**2)):
    print ("This is an obtuse triangle!")
elif ((a**2) + (b**2) > (c**2)):
    print ("This is an acute triangle!")
else:
    print("Something went wrong! Yell at gavin to fix his code!")
    
#Final Values
"""
ask = input("Would you like to see your Final Values? (Yes or No): ")

if ask == "Yes" or ask == "yes" or ask == "y" or ask == "Y":
    print("a^2 = " + str(a**2))
    print("b^2 = " + str(b**2))
    print("c^2 = " + str(c**2)) 

else:
    print("Have a nice day!")
"""