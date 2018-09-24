def karmaStart():
    karma = 0
    print("This game runs on a karma system, that is, you have an invisible number, whos value will never be known to you, that will affect the situations you find yourself in.")
    print("Possibly... Maybe it will only affect one choice... or several.")
    print("That being said your current karma is equal to: " + str(karma))
    
    return karma
    
def karmaChoice():
    print("The only oppotuniy you have to directly manipulate this value is right now!")
    choice = input("Do you wish to have one additional karma added to your total? (Yes or No): ")
    return choice