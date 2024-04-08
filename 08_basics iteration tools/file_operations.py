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
    print(line, end='') # ------->print without next line gap


