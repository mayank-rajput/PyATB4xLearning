def greet(name):
    print("Hello", name)
name = input("Enter Your Name:")
greet(name)

print("\nNo return Type with argument\n")
def greet_by_name(fname):
    print("Hello,", fname)

greet_by_name("Mayank")
greet_by_name(123)
greet_by_name(True)