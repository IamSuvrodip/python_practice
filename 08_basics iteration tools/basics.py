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
print(I) #-----------><list_iterator object at ---->0x7f33c6b5ff70<--- THIS IS SAME ADDRESS BECAUSE THIS REFERANCE NOT CHANGE
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print('\n\n')

my_list1 = [1, 2, 3, 4, 5, 6]
print(iter(my_list1) is my_list1)
print('\n\n')


dict = {'a':1, 'b':2 }
for item in dict.items():
    print(item)
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)
print('\n')
I = iter(dict)
print(I) #------><dict_keyiterator object at 0x7ff08c9759e0>
print('\n')

print(next(I))
print(next(I))
print('\n')

print(range(5))
R = range(5)
I = iter(R)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))






