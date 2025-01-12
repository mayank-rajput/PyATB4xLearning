# Function Scope
global_b = 12 # Global Variable
def my_function():
    a = 10 # local Variable -->> it should be within function
    print(a)
    print(global_b)

my_function()
print(global_b)

def f1():
    print(global_b)

f1()