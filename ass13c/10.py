# print distinct elements from given list
from operator import index
l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
l2=[]
for i in l1:
    if i not in l2:
        print(i,"==",end="")
        for j in range(0,len(l1)):
            if i==l1[j]:
                print(j,end=" ")
        l2.append(i)
        print("\n")