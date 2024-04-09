file1 = open("08_basics iteration tools/file.txt")
'''
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
'''
'''print(file1.__next__())
print(file1.__next__())
print(file1.__next__())
print(file1.__next__())'''

for line in open('08_basics iteration tools/file.txt'):
    print(line) # ---------> print next line gap
print('\n\n')

for line in open('08_basics iteration tools/file.txt'):
    print(line, end='') # ------->print without next line gap
print('\n\n')


file1 = open("08_basics iteration tools/file.txt")
while True:
    line = file1.readline()
    if not line:
        break
    print(line, end='')
print('\n\n')

name = "suvrodip"
if not name:
    print("rudronil")
else:
    print(name)
print('\n\n')






