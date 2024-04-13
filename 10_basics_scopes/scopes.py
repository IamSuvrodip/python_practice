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

x = 99
def num4():
    x = 88
    def num5():
        print(x)
    num5()
num4()

def num6():
    #x = 88
    def num7():
        print(x)
    num7()
num6()
print('\n')

def num8():
    x = 88
    def num9():
        print(x)
    return num9
res = num8()
res()
print('\n')









