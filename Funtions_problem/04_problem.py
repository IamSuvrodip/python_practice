# function return multiple values

# create a function that returns both the area and circumference of a circle given its radius.


'''radius = float(input("Enter the radius value: "))
pai = 3.1415

def area():
    print ("Your circle area is: ",pai * (radius**2))


def circumference():
    print ("Your circle circumference is: ", (2 * pai * radius))


area()
circumference()'''


# here another way using math library

import math

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(5.5)

print ("Your circle area is:", round(a,3), "\nYour circle circumference is:",  round(c,3))
