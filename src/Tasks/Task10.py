integer = int(input("Please Enter A Number: "))
f = 1
for i in range(integer, 1, -1):
    f = i * f
print(f"Factorial of {integer} is:", f)
