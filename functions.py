"""
This is all about functions
"""
def greeting():  #Does not return anything
    print("H")

def nameAsk():
    name = input("What is your name? ")
    return name

def ageAsk():
    age = int(input("What is your age, if you do not mind my asking? "))
    return age

def canVote(age):
    if age == 18:
        print("You can Vote!")
        canVote = True
    else:
        print("You cannot Vote!")
        canVote = False
    return canVote

#CALL IT
greeting()
#SAVE THE OUTPUT OF FUNCTIONS to a variable
name = nameAsk() 
age = ageAsk()
print("Hello " + name + ", you are " + str(age) + " years old!")
vote = canVote(age)
print(vote)