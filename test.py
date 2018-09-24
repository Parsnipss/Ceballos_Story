import quiz2

quiz2.numBig()

quiz2.greeter()

age = quiz2.vote() #Stores the return value of the function age

if age >= 18:
    print("You are old enough to vote!")
elif age == 17 or age == 16:
    print("You are elibigble for pre-registration!")
else:
    print("In " + str(18-age) + " years you will be able to vote!")