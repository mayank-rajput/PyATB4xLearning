# Find Max between 3 numbers

num1 = float(input("enter number 1 :"))
num2 = float(input("enter number 2 :"))
num3 = float(input("enter number 3 :"))

if num1 > num2 and num1 > num3:
    print(f"Max is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Max is {num2}")
else:
    print(f"Max is {num3}")
