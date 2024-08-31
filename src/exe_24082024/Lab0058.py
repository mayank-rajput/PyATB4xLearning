# Create A program for Sum of 3 Number with user inputs

num1 = int(input("Enter the Number1: "))
num2 = int(input("Enter the Number2: "))
num3 = int(input("Enter the Number3: "))



def sum_of_three_num(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_num(num1, num2, num3)
print(result)
result = sum_of_three_num(n1=num1, n2=num2, n3=num3)
print(result)