public_toilet = "PB" # global Variable

def my_home():
    pvt_toilet = "PT" # Local Variable
    public_toilet = "LPB"
    print(public_toilet) # Global Variable Callled
    print(pvt_toilet)

my_home()

def stranger():
    print(public_toilet) # Global Variable Callled
stranger()
# print(pvt_toilet)
print(public_toilet) # Global Variable Callled