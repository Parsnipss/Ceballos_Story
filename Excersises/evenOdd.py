"""
Let user know if even or odd (int only)
"""

x = float(input("Please input an integer for inspection: "))

if (x % 2 == 0):  # This is the even return
    print("Your number, " + str(x) + ", is even.")
elif (x % 2 == 1):  # This is the odd return
    print("Your number, " + str(x) + ", is odd.")
else:
    print("That is a decimal, Please use an integer!")