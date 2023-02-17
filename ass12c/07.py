# fibbonacci series
n=int(input('enter how many fibbonaci number you want to print : '))
a,b,c=-1,1,0
while n>=1:
    c=a+b
    a=b
    b=c
    print(c,sep=" ")
    n-=1