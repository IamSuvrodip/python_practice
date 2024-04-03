# Fruit Ripeness Checker

print("The fruit is 'Banana'")
fruit_condition = input("What is the Banana's condition (Green), (Yellow) or (Brown)= ").lower()

if fruit_condition == 'green':
    print("This Banana is Unripe")
elif fruit_condition == 'yellow':
     print("This Banana is Ripe")
elif fruit_condition == 'brown':
     print("This Banana is Overripe")
else:
    print("You enterd wrong Details")