# Sum of Even Numbers
numbers_str = input("Enter elements of the list separated by spaces: ")
numbers = numbers_str.split()
number_list = list(map(int, numbers))

sum = 0

for num in number_list:
    if num > 0:
        if num % 2 == 0:
            sum += num
print(f"Total sum of even numbers of this list= {sum}\n\n")





# 2nd type
user= int(input("Enter the total element you want= "))

total = 0

for i in range(1,user+1):   #user = 10 mean 10 index mean 9 tak jayega isliye user+1 karna hain
    if i%2 == 0:
        total += i
print(total)


