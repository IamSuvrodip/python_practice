# scopes

# simple function
name= "suvrodip"
def username():
    name = "Dip"
    print(name)
print(name)
username()
print('\n')

name= "suvrodip"
def username():
    # name = "Dip"
    print(name)
print(name)
username()
print('\n')

x = 99
def num(y):
    z = x + y
    return z
result = num(1)
print(result,'\n')


x = 99  #--------->global
def num1():
    x = 88#-------->local
    print(x)
num1()
print(x,'\n')

x = 50
def num3():
    global x #------> make it local to global
    x = 10
num1()
print(x,'\n')





