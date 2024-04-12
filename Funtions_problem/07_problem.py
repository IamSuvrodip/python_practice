# Functuion with *args 
# * dinote multiple returns

def sum_all(*args): #------- args likhna mendatory nehi hain args ke ehape kusvi nam de sakteho * lagana medatory hain
    return sum(args)
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5),'\n\n')

def sum_all(*args):
    print(*args)
    return sum(args)
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5),'\n\n')

def sum_all(*args):
    print(args) #---------> print and covert tuple
    return sum(args)
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5),'\n\n')

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)
print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5),'\n\n')