# USer Defined Function

# They Can Return Something
# The Can't Resturn - No return Type
# They HAve PArameters
# They don't have Parameters
# No Return Type and No Parameters


# 1 . No return Type No Parameter
def greet():
    print("Hello World")


# 2. No REturn Type with Parametere

def greet_by_name(name):
    print("Hello", name)


greet_by_name("Mayank")


# 3. No Return Type With Default PARA

def say_hello_default_arg(name="Mayank"):
    print("Hello,", name.upper())


say_hello_default_arg("Amit")
say_hello_default_arg(name="Tushar")  # Positional Arg
say_hello_default_arg()


# Multiple ARGS

def multiple_args(name1= "Sunny", name2= "Shubham", name3="Saurabh"):
    print("Multiple Args,", name1, name2, name3)


multiple_args(name1="mayank", name2="Tushar", name3="Amit")
multiple_args(name1="Akshay")
multiple_args()

# 4. Arg  + Return Type

def sum_of_two_num(num1, num2):
    return num1 + num2


result = sum_of_two_num(num1=10, num2=20)

print(result)


def sum_of_two_num_default(num1=20, num2=20):
    return num1 + num2


result = sum_of_two_num_default()

print(result)
