tea_types = ("Black", "Green", "Oolomg", "White", "Masala")
print(tea_types)
print(type(tea_types),'\n\n')

#Slicing
print(tea_types[0])
print(tea_types[-1])
print(tea_types[0::2])
print(tea_types[2:])
print(tea_types[:3])
print(tea_types[:],'\n\n')

#Tuple is imutable
#refernace changable
#--------X Error['tuple' object does not support item assignment]
#tea_types[0] = "Lemon"


print(len(tea_types),'\n\n')

more_tea = ("Herbal","Mint")
all_tea = more_tea + tea_types
print(all_tea,'\n\n')

if "Green" in all_tea:
    print("I have grren tea",'\n\n')
else:
    print("I dont have grren tea",'\n\n')

more_tea = ("Herbal", "Suger Free","Herbal")
print(more_tea)
print(all_tea,'\n\n') # Here all tea mean ('Herbal', 'Mint', 'Black', 'Green', 'Oolomg', 'White', 'Masala')
# privius more_tea + tea_types

print(more_tea.count("Herbal"))
print(more_tea.count("Suger Free"))
print(more_tea.count("Herb"),'\n\n')

print(tea_types)
(black, green, oolomg, white, masala) = tea_types
print(black)
print(type(black))
print(oolomg)
print(type(oolomg),'\n\n')



















