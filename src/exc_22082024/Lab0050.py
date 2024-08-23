# MAtch Statement - Switch in Java - MAtch the ouput and execute
# Match Statement will work in above python3.10 version

# match variable_name:
#    case patteren1:
#       code bloack
#   Case patteren2:
#        code block

# Write a program to ask user on which browser he want to run Automation

browser = input("Enter the name of browser:")
browser = browser.lower()

match browser:
    case "firefox":
        print("Execute firefox")
    case "chrome":
        print("Execute chrome")
    case "safari":
        print("Execute safari")
    case _:
        print("Browser not found")