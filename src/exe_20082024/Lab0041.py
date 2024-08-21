# Grade Calculater
Score = float(input("Enter Your Score: "))

if 90 <= Score <= 100:
    print("Your Grade Is A")
elif 80 <= Score <= 89:
    print("Your Grade Is B")
elif 70 <= Score <= 79:
    print("Your Grade Is C")
elif 60 <= Score <= 69:
    print("Your Grade Is D")
elif 50 <= Score <= 59:
    print("Your Grade Is E")
elif Score >= 100:
    print("Invalid Score!!")
else:
    print("Your Grade Is F")
