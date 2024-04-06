# Multiplication Table Printer
# Multiplication Table Print upto 10 but skip 4th and 8th 

table = int(input("What number table you want to print= "))

for i in range(1, 11):
    if i == 4 or i == 8: # detection
        continue  
    print(f"{table} X {i} = ",table * i)
