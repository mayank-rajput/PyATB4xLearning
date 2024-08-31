def print_arg(*args):
    # *args = multiple args with no Limit - list
    print(args[0])

print_arg("Mayank", "Amit", "Lucky")
print_arg( "Amit", "Lucky")
print_arg(  "Lucky")
#print_arg() ----->>> Error


print("AMit")
print("AMit", "MAyank")
print("AMit", "MAyank", "Rajput", "Somesh")
print("AMit", "MAyank", "Rajput", "Somesh", 10)
print("AMit", "MAyank", "Rajput", "Somesh", 10, True)
print("AMit", "MAyank", "Rajput", "Somesh", 10, True, False)