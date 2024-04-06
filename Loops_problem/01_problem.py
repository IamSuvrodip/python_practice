# Counting Positive Numbers

numbers_str = input("Enter elements of the list separated by spaces: ")
numbers = numbers_str.split()
number_list = list(map(int, numbers))

positive_number_count = 0

for num in number_list:
    if num > 0:
        positive_number_count += 1
print(positive_number_count)




