# Grade Calculator

ben = float(input("Enter your bengali subject marks= "))
eng = float(input("Enter your english subject marks= "))
math = float(input("Enter your math subject marks= "))
com = float(input("Enter your computer subject marks= "))
geo = float(input("Enter your geography subject marks= "))

total = ben+eng+math+com+geo

per= (total/500)*100

print("Your total marks is",total)
print("Your percentage is: ",round(per,2),'\n')



if per>100:
    print("Wrong grading")
elif per >= 90:
    print("Grade='A'\tPASS ")
elif per >= 80:
    print("Grade='B'\tPASS ")
elif per >= 70:
    print("Grade='C'\tPASS ")
elif per >= 60:
    print("Grade='D'\tPASS ")
else:
    print("Grade='F'\tFAIL ")


