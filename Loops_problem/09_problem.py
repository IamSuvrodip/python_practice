# List Uniqueness Checker

user_input = input("Enter words separated by spaces: ")
items = user_input.split()

unique_item = set() # set always duplicate value remove

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
        #break it use so it print first dublicate value just
    unique_item.add(item) #here print all dublicate value print





