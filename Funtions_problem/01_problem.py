# Basic Function Syntax
# Write a function to calculate and return the square of a number
# 3 types of written function

def square_of_num(number): #---------->defination in baraket(parameter)
    print(number ** 2)
square_of_num(4) # call function //(4) mean 4^2=16
print('\n')

def square_of_num(number):
    print(number ** 2)
result = square_of_num(4)
print(result,'\n')

def square_of_num(number): 
    return number ** 2

result = square_of_num(5)
print(result,'\n')



