# Write a program hat will ask the user their age and then determin if they are old enough to vote

ask = float(input("How old are you? Please use numbers only: "))

if ask < float(18):
    print ("You are not eligible to vote!")
elif ask >= float(18):
    print ("You are eligible to vote!")
    vote = input("Are you going to participate in voting for your local area? ")
    if vote == "yes" or vote == "Yes" or vote == "y" or vote == "Y":
        print ("Good job doing your civic duty!")
    elif vote == "no" or vote == "No" or vote == "n" or vote == "N":
        print ("Please consider participation, however, it is up to you.")
else:
    print ("I'm not familiar with that number system.")
    
