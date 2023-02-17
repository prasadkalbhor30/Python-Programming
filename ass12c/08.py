# lcm
a,b=int(input("Enter two numbers to calculate lcm : ")),int(input())
if  a<b :
    num1,num2=a,b
else :
    num1,num2=b,a
while 1:
    while num1<=num2:
        if num2==num1:
            print(num1)
            break
        num1+=a
    if num1==num2:
        break
    num2+=b