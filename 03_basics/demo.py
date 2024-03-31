# python have a garbage collector

a = 5 #imidiate garbage collector not remove 5 because in memory first a asign 5 but next a asign 7 so remove 5 in memory by garbage collector
b = 10
a = a + 2

print(a)
print(b)


mylistone = [1, 2, 3, 4, 5]
mylisttwo = mylistone

print("\n\nlist one ", mylistone)
print("list two ", mylisttwo)

mylistone = ["suvrodip",125,"CSE"] #full list was changes
print("\nlist one ", mylistone)
print("list two ", mylisttwo)

mylistone = [1,2,3,4,5]
print("\nlist one ", mylistone)
print("list two ", mylisttwo)

mylistone[0] = 50
mylistone[3] = 60
print("\nlist one ", mylistone)
print("list two ", mylisttwo)


l1=[1,2,3,4,5]
l2=l1
print("\nlist one ", l1)
print("list two ", l2)

l1[0]=50        #full list not changes its index number was change so l2 is same as l1
l2[3]=60
print("\nlist one ", l1)
print("list two ", l2)

p1=[1,2,3]
p2=p1
print("\nlist two ", p2)
p2=[5,6,7]
p1[0]=50
print("\nlist one ", p1)
print("list two ", p2)


h1=[1,2,3]
h2=h1[:]        #slicing make a copy of this list
h1[0]=55
print("\nlist one ", h1)
print("list two ", h2)  #not chnage because h2 copy of this list 


#********** == is **********
n = [1,2,3]
m=n
print("\nlist one ", n)
print("list two ", m)

print(m == n)
print(m is n,"\n")

m = [1,2,3] # memory create a list values are same but n not asign m thats why m==n is true but m is n not true
print(m == n)
print(m is n)

