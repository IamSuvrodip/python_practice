# Behind the loop 
# loop and itretion same
# (for,comprehension,map)-------->tools of itretion
# iterable objects(lists,file)

# __next__ ---------> response

# iter()------>tool
# next()
# next()
# next()

'''import time

print("suvrodip chakroborty")
username = "Suvrodip"
print(username)'''

name = "suvrodip"
if not name: #-------> Value not in the variable or list then this call true
    print("rudronil")
else:
    print(name)
print('\n\n')


#iter tools
my_list = [1, 2, 3, 4, 5]  #----->list
I = iter(my_list)
print(I) #-----------><list_iterator object at ---->0x7f33c6b5ff70<--- THIS IS MEMOEY LOCATION first memory referance
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
