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


