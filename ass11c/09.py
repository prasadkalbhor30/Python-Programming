b=""
n=int(input("Enter a number to convert in binery : "))
while n>=2:
    b=str(n%2)+b
    n=n//2
b=str(n)+b
b=int(b)
print(b)