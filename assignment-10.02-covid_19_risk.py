age = True if input("Are you a cigarette addict older than 75 years old? ").lower() == "yes" else False
chronic = True if input("Do you have a severe chronic disease? ").lower() == "yes" else False
immune = True if input("Is your immune system too weak?").lower() == "yes" else False
risk = age or chronic or immune 
if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")