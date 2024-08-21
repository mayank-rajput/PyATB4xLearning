# Create a program that takes 2 numbers as input and prints wheather the first number is Greater that,less that or
# Equal to the second number

num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

if num1 > num2:
    print(f"{num1} is Greater than {num2}")
elif num1 < num2:
    print(f"{num1}  is less that {num2}")
else:
    print(f"{num1} is Equal to {num2}")