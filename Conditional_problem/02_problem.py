# Movie Ticket Pricing

age = int(input("Enter Your age= "))
day = (input("What the day today= ").lower())
print("Your age is= ",age)
print("Today is= ",day)

if age<18 and day!='wednesday':
    print("You are Child So Your Movie ticket price is= $8")
elif age>17 and day!='wednesday':
    print("You are Adult So Your Movie ticket price is= $12")
elif age<18 and day=='wednesday':
    print("You are Child and today is wednesday So discount $2 So Your Movie ticket price is= $6")
elif age>17 and day=='wednesday':
    print("You are Adult and today is wednesday So discount $2 So Your Movie ticket price is= $10")
else:
    print("Something Wrong")