# Factorial Calculator using while loop

number = int(input("Enter your number: "))
factorial = int(input("Enter your factorial number: "))

while number > 0:
    factorial *= number
    number = number - 1
print(f"Factorial number of is= {factorial}")


    

