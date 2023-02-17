mn=int(input("Enter month number : "))
if mn>12 or mn<1:
    print("invalid month number")
elif mn<8 and mn%2:
    print("31")
elif mn==2:
    print("28")
elif mn<8:
    print("30")
elif mn>7 and mn%2:
    print("30")
else:
    print("31")

