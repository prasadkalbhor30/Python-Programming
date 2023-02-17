year=int(input("Enter year : "))
if year%100==0:
    if year%400==0:
        print("Leap Year")
    else:
        print("Not a leap year")
else:
    if year%4==0:
        print("Leap Year")
    else:
        print("Not a leap year")

