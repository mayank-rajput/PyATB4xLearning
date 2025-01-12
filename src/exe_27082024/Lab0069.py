# Decorators

def my_decorators(func):
    # two parts
    # Wrapper & call
    def wrapper():
        print("1.Sommething happening before the Function is Called")
        print("2.Add Helmet, Dashcam, Gloves", "Knee Guards")
        func()
        print("3.Something IS HAppening After the function is Called")
        print("4.Secure Driving")

    return wrapper()


@my_decorators
def drive_bike():
    print("I am Driving")






