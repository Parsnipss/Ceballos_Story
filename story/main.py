import storyRooms

health = 5

karma = storyRooms.karmaStart()

choice = storyRooms.karmaChoice()

if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
    print ("Your greed and self-interest clearly define you, for this you lose one karma")
    karma = karma - 1 
elif choice == "No" or choice == "no" or choice == "n" or choice == "N":
    print ("Your humble choice has gained you one karma!")
    karma = karma + 1
else:
    print ("Not following directions will have consequences, you have lost the opportunity to gain karma!")
    
