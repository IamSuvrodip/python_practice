# files operations

file = open('test.txt','w')

# this one type of error handling
try:
    file.write("Suvrodip")
finally:
    file.close()

# this is another type of error handling
with open('./project/youtube.txt', 'w') as file:
    file.write("rudronil")