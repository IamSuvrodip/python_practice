# Password Strength Checker

password = input("Write Your Password= ")

if len(password) <= 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Yoyr password strength is= {strength}")