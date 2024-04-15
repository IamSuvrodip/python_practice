# files operations

file = open('test.txt','w')

# this one tupe
try:
    file.write("Suvrodip")
finally:
    file.close()

# this is another type
with open('./project/youtube.txt', 'w') as file:
    file.write("rudronil")