current_year = 2025
birth_year = int(input (" Enter your year of birth: "))
age = current_year - birth_year
print (f"you are {age} years old")
if age <16:
    print("You can't vote: ")
elif age <18 or age >70:
    print ("Your vote is optional")
else:
    print ("Your vote is obrigatory")
    