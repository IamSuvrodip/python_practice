x = 5
y = 10
z = 5

print(f"Sum of {x}+{y}= ",x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % 2)
print(z ** 2)
print(x ** 5)

print("\n")
print(x+y*z)    #-----X this is not actually write in production level it is follow BODMAS rule
print((x+y)*z)  #-----^_^ this is actually write in production level it is not follow BODMAS rule
print(x+(y*z))  #-----X this is actually write in production level it is also follow BODMAS rule


print("\n")
print(40 + 2.14) #----X this not proper way to write
# print('suvrodip' + 2.14) #-----X this not proper way to write STR and FLOAT values not add
print('suvrodip' + '2.14')  #-----^_^ this proper way to write STR and STR values are add

print("\n")
print(40 + int(2.14))   # there float value covert into int value
print(float(40) + 2.14)  # there int value covert into float value


print(100 ** 2) # this is all c c++ calculate this 
print(2 ** 100)     # this is all c c++ calculate this but so many time this capablity in python calculate this in less time
print(2 ** 10000)


result = 1/3.0
print(result,"\n")

a = repr('Suvrodip')
b = repr("Suvrodip")
print(a)
print(type(a))
print(b)
print(type(b),"\n")

a = str('Rudronil')
b = str("Rudronil")
print(a)
print(type(a))
print(b)
print(type(b),"\n")

print('sumit')
print("sumit")


print("\n")
print(1 == 2 < 3) #-------1
print(1 == 2 and 2 < 3) #-------2 (1 and 2) are same

print("\n")
print(1 == 2 < 3) #-------1
print(1 == 2 or 2 < 3) #-------2 (1 and 2) are not same


print("\n")
import math
print(math.floor(3.5))     # 3 always lower value
print(math.floor(-3.5))     # 4 always lower value
print(math.floor(3.6))     # 3 always lower value
print(math.floor(3.9))     # 3 always lower value

print("\n")
print(math.trunc(2.8))     # 2 towords 0
print(math.trunc(-2.8))     # 2 towords 0

x = 3.1415
print(round(x,2))


print("\n")
print(2 + 1j)
print(2 + 1j * 3)
print((2 + 1j)*3)


print("\n****** binay,octal,hexadecimal********")
print(0b1000,0b11,0b0111)
print(0o77,0o607,0o435)
print(0xff,0xabcdef,0x435)

print("\n****** decimal to all types********")
print(oct(64))
print(hex(64))
print(bin(13))


print("\n****** all types to decimal********")     
print(int('77',8))
print(int('a0',16))
print(int('10010',2))
print(int('64',10))
      
      
#*********bit wise operator**********


print("\n****** import random ********")     
import random
print(random.random())  #there value placed bitween 0 and 1
print(random.random())
print(random.random())

print("\n")
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))


print("\n")
l1 = ['RCB', 'KKR', 'CSK', 'MI']
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))

print("\n")
random.shuffle(l1)
print(l1)
(random.shuffle(l1))
print(l1)
(random.shuffle(l1))
print(l1)
(random.shuffle(l1))
print(l1)



