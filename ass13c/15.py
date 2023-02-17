# sum of elements in a given list
l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
e=0
o=0
for i in l1:
    if i%2:
        o+=i
    else:
        e+=i
print("Sum of even numbers in list =",e,"\nSum of odd numbers in list =",o)