user_type = input("Enter the User Type(Manager/ Guest/ Admin/ User):")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello Guest")
    case "user":
        print("hello USer")
    case _:
        print("Hello There")


