# Generator function with yield
# yield concept is little bit dificult
# but you think about this memory perspective then its easy for understand

def even_generator(limit):
    for i in range(0, limit+1, 2):
        print(i)
even_generator(10)
print('\n')

def even_generator(limit):
    for i in range(3, limit+1, 2):
       return(i)
print(even_generator(10),'\n')

def even_generator(limit):
    li=[]
    for i in range(0, limit+1, 2):
       li.append(i)
    return li
print(even_generator(10),'\n\n')

def even_generator(limit):
    for i in range(0, limit+1, 2):
       yield(i)
for num in even_generator(10):
    print(num)
