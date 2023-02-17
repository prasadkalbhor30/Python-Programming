i=0
n=int(input("Enter a number : "))
while n!=0:
    i+=n%10
    n=n//10
print(i)