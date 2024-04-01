tea_varities = ["Black", "Green", "Oolong", "White", "Masala", "Ginger", "Mint"]
print(tea_varities)
print(tea_varities[1])
print(tea_varities[-1])
print(tea_varities[0:])
print(tea_varities[:4])
print(tea_varities[::2])
print("Length of this list= ",len(tea_varities),'\n')

tea_varities[3]= "Herbal"
print(tea_varities,'\n')

#tea_varities[1:1]="Lemon" 
#print(tea_varities)  ------#['Black', 'L', 'e', 'm', 'o', 'n', 'Green', 'Oolong', 'Herbal', 'Masala', 'Ginger', 'Mint']
#tea_varities[1:2]="Lemon"
#print(tea_varities)  ------#['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal', 'Masala', 'Ginger', 'Mint']
#tea_varities[1:3]="Lemon"
#print(tea_varities)  ------#['Black', 'L', 'e', 'm', 'o', 'n', 'Herbal', 'Masala', 'Ginger', 'Mint']
#tea_varities[1:]="Lemon"
#print(tea_varities)  ------#['Black', 'L', 'e', 'm', 'o', 'n']
#tea_varities[:1]="Lemon"
#print(tea_varities)  ------#['L', 'e', 'm', 'o', 'n', 'Green', 'Oolong', 'Herbal', 'Masala', 'Ginger', 'Mint']
#tea_varities[1]="Lemon"
#print(tea_varities)  ------#['Black', 'Lemon', 'Oolong', 'Herbal', 'Masala', 'Ginger', 'Mint']

tea_varities = ["Black", "Green", "Oolong", "White", "Masala", "Ginger", "Mint"]
print(tea_varities[1:2])
tea_varities[1:2] = ["Lemon"]
print(tea_varities,'\n')

print(tea_varities[1:3])
tea_varities[1:3] = ["Green", "Sugerfree"]
print(tea_varities,'\n')

print("List is Empty= ",tea_varities[1:1],'\n') #-------Empty List

tea_varities[1:1] = ["chsi1", "chai2"] #-------add operation
print(tea_varities)
print(tea_varities[1:2])
print(tea_varities[1:3],'\n\n')

tea_varities[1:3] = [] #---------delete operation
print(tea_varities,'\n')


tea_varities = ["Black", "Green", "Oolong", "White", "Masala", "Ginger", "Mint"]
for tea in tea_varities:
    print(tea)
print('\n')

for tea in tea_varities:
    print(tea,'\n')
print('\n')

for tea in tea_varities:
    print(tea, end=" ")
print('\n')

for tea in tea_varities:
    print(tea, end=",")
print('\n')

for tea in tea_varities:
    print(tea, end=" , ")
print('\n')

for tea in tea_varities:
    print(tea, end=", ")
print('\n')

for tea in tea_varities:
    print(tea, end=" - ")
print('\n\n')



#remove last coma,space and dash sign
tea_varities = ["Black", "Green", "Oolong", "White", "Masala", "Ginger", "Mint"]

for tea in tea_varities[:-1]:
    print(tea, end=" ")
print(tea_varities[-1])

for tea in tea_varities[:-1]:
    print(tea, end=",")
print(tea_varities[-1])

for tea in tea_varities[:-1]:
    print(tea, end=" , ")
print(tea_varities[-1])

for tea in tea_varities[:-1]:
    print(tea, end=", ")
print(tea_varities[-1])

for tea in tea_varities[:-1]:
    print(tea, end=" - ")
print(tea_varities[-1])
print('\n')


#2nd method using join function
tea_varieties = ["Black", "Green", "Oolong", "White", "Masala", "Ginger", "Mint"]

print(' '.join(tea_varieties))

print(', '.join(tea_varieties))

print(', '.join(tea_varieties))

print(', '.join(tea_varieties))

print(' - '.join(tea_varieties),'\n\n')


tea_varieties = ["Black", "Green", "Oolong", "White", "Ginger", "Mint"]
if "Masala" in tea_varieties:
    print("Yes I have Masala tea")
else:
    print("No I dont have masala tea")
print('\n')

tea_varieties.append("Masala") #--------add masala tea in list at last
if "Masala" in tea_varieties:
    print("Yes I have Masala tea")
else:
    print("No I dont have masala tea")
print('\n')
print(tea_varieties)


#STACK practice
tea_varieties = ["Black", "Green", "Oolong", "White", "Ginger", "Mint"]
last= (tea_varieties.pop())
print("\nPop function remove last element of list= ",last,'\n')
print(tea_varieties)
print(f"\nNow you see {last} tea is remove this list\n\n")

tea_varieties.remove("Green")
print("\nremove function remove specific element what I want to remove of list\n")
print(tea_varieties)
print(f"\nNow you see Green tea is remove this list\n\n")

print("\ninsert function insert a element what I want to insert and which position of list\n")
tea_varieties.insert(1,"Green") #----(1,"Green") here 1 is index position and "Green" is what you want to insert in this list
print(tea_varieties)
print(f"\nNow you see Green tea is add this list\n\n\n\n")


#Memory references 
tea_varieties_1 = tea_varieties
print(tea_varieties_1,'\n')
tea_varieties.append("Lemon")
print("List 1 after append= ",tea_varieties)
print("List 2 after append= ",tea_varieties_1,'\n\n')
#here print same value and tea_varieties_1 and tea_varieties reference same list in memory

tea_varieties_copy = tea_varieties.copy()
print("List 2 copy before pop= ",tea_varieties_copy,'\n')
tea_varieties.pop()
print("List 1 after pop= ",tea_varieties)
print("List 2 copy afer pop= ",tea_varieties_copy,'\n')
print("You see list 1 after pop change but List 2 not change after list 1 pop\n\n\n\n")
#here print same value but tea_varieties_copy and tea_varieties reference different list in memory 
#tea_varieties this list make a copy help of copy function and assign it in tea_varieties_copy






