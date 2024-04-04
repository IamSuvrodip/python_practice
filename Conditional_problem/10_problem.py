# Pet Food Recommendation

pet =(input("Enter your pet's type dog/cat= ").lower())
age = int(input("Enter your pet's age= "))

if (pet == 'dog' and age<3):
    print("Puppy food")
elif (pet == 'dog' and age>2):
    print("Adult dog food")
elif (pet == 'cat' and age<6):
    print("Junior cat food")
elif (pet == 'cat' and age>5):
    print("Senior cat food")
else:
    print("something wrong..")