# Object types / Data types
'''
list = []
dictionary = {}
tuple = ()
file = open('test.txt')
'''

mylist = [123,"hello",3.1415]
print('\n**********List***********\n')
print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[-1])

mydict = {'one':'lemon','two':'sugar','three':'masala'} #one is key and lemon is value
print('\n**********Dictionary***********\n')
print(mydict)
print(len(mydict))
#print(mydict[0])-------X
#print(mydict[-1])-------X
print(mydict['two'])
print(mydict['three'])

mytuples = (1,2,3,4,5,6,7,8,9)
print('\n**********Tuple***********\n')
print(len(mytuples))
print(mytuples[0])
print(mytuples[-1])

num=(0)
print(type(num)) #<class 'int'>
num=(0,)
print(type(num)) #<class 'tuple'>

print('\n**********Files***********\n')
f= open("demo.txt")
print(f)

f= open("demo.txt",'w')
data = f.write("Sumit kumar roy\n")

f= open("demo.txt",'a')
f.write("Suvrodip\n")
f.write("Rudronil\n")


f= open("demo.txt",'r')
data = f.read()
print(data)
print(type(data))
f.close()
