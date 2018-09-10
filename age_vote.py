# Write a program hat will ask the user their age and then determin if they are old enough to vote

ask = int(input("How old are you?: "))

if ask < int(18):
    print ("You are not eligible to vote!")
elif ask == int(17):
    print ("You are not eligible to vote, but you may preregister.")
elif ask >= int(18):
    print ("You are eligible to vote!")
    vote = input("Are you going to participate in voting for your local area?")