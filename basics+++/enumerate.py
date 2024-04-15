# enumerate

names = ("Suvro", "Dip", "Rudro") #--------> this is a tuple
names1 = enumerate(names)

print(names1)#---------><enumerate object at 0x7f7ed39644c0>

print(list(names1))#----------->[(0, 'Suvro'), (1, 'Dip'), (2, 'Rudro')]

print(dict(names1))#----------->{0: 'Suvro', 1: 'Dip', 2: 'Rudro'}

print(tuple(names1))#----------->((0, 'Suvro'), (1, 'Dip'), (2, 'Rudro'))

# enumerate make key value format list , dict , tuple
