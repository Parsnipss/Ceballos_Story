"""
EVEN ODD INTEGERS ONLY
"""

x = float(input("Please input an integer for inspection: "))

if x % 2 == 0:
    print("The number, " + str(x) + ", is even!")
elif x % 1 == 0:
    print("The number, " + str(x) + ", is odd!")
else:
    print("This is not an integer!")