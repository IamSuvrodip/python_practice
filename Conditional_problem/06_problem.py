# Transportation Mode Selection

distance = float(input("How much your Destination Distance: "))
if distance < 0:
    print("You Enter Wrong Distance")
    exit()
if distance < 3:
    print("You go to padel")
elif distance <=15:
    print("You go to on Bike")
else:
    print("You go to on Car")




