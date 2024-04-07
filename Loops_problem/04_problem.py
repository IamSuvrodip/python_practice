#  Reverse a String using a loop

string = input("Enter your string: ")

reversed_str = ""

for char in string:
    reversed_str = char +reversed_str 
print(reversed_str)


