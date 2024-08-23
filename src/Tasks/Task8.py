# identify type of triangle

a = float(input("Enter First Side Of A Tringle: "))
b = float(input("Enter Second Side Of A Tringle: "))
c = float(input("Enter Third Side Of A Tringle: "))

if a == b and b == c and c == a:
    print("It's Equilateral Triangle")
elif a == b and b != c and c != a:
    print("It's Isosceles Triangle")
else:
    print("It's Scalene Triangle")
