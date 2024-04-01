name="suvrodip"
first_character= name[0]
second_character= name[1]
third_character= name[:]
fourth_character= name[-2]
print(first_character)
print(second_character)
print(third_character)
print(fourth_character,"\n")

full_name = "suvrodip chakroborty"
print(full_name)
slice_full_name = full_name[0:8] # its mean 0 to before 8 index mean upto 7 index
print(slice_full_name,"\n")


number_list = "0123456789"
print(number_list[:]) # first index to last index
print(number_list[3:]) # 3 index to last
print(number_list[:5]) #upto 4 index
print(number_list[0:10:2])
print(number_list[0:10:3])
print(number_list[0::2],'\n')

place = "KoLkAta"
print(place)
print(place.lower())
print(place.upper())
print(place.capitalize(),'\n')
print(place.replace("KoLkAta","basirhat"))
print(place,"\n") #place not change


username="  Suvrodip01  "
print(username)
print(username.strip(),'\n')


chai = "Lemon Ginger Masala Mint"
print(chai.split())
print(chai.split(", "),'\n') #remove (, and space)

print(chai.find("Ginger"),'\n')

order = "T-shirt, Pant, Shirt, Pant, T-shirt, T-shirt, T-shirt, Pant"
print("Today's total T-shirt sell= ",order.count("T-shirt"),'\n')

chai_type = "Masala"
quantity = 2
order = "I orderd {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type),'\n')

#2nd type
order1 = f"I orderd {quantity} cups of {chai_type} chai"
print(order1,'\n')

chai_variety= ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print(type(chai_variety),'\n')

print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety),'\n')

email = ["suvrochakroborty01", "rudrochakroborty565", ""]
print("gmail.com ".join(email),'\n')


name="suvrodip"
print(len(name),'\n')

for letter in name:
    print(letter)
print('\n\n')


chai = "He said, \"Masala chai is awesome\""
print(chai,'\n')
chai= "E:\python practice\n05_basics\06\04\03\02\01"
print(chai)
#raw string print
chai= r"E:\python practice\n05_basics\06\04\03\02\01"
print(chai,'\n')

#chai = r"c:\user\pwd\" --------- X[error]
chai = r"c:\user\pwd"
print(chai)
chai= r"c:\\user\\pwd\\"
print(chai,'\n')

#unicode exceping
chai = "c:\\user\\pwd\\"
print(chai,'\n')
#chai = "c:\user\pwd"--------- X
#print(chai) ----------[error]

if("c:" in chai):
    print("You are in C drive",'\n')
elif("E:" in chai):
    print("You are in E drive",'\n')
elif("D:" in chai):
    print("You are in D drive",'\n')
else:
    print("Your path is not found",'\n')
    
email = "suvrodipchakroborty01@gmail.com"
print("@gmail.com" in email)
print("@edu.in" in email,'\n')








