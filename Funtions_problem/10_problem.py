# Recursive function
# calculate factorial number

# speacial techniqe 
# function ko call karteho bar bar functionke undersehi

def add_num(a, b):
    add_num(2,3) # ehape khudi khudiko call kar raha hein infite loop main fas geyi

# how to exit to the recurtion this is main thing
def factorial(n):
    if n == 0: #--------->exit stratagy
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
