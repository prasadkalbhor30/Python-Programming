# print distinct elements from given list
l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
l2=[]
for i in l1:
    k=0
    if i not in l2:
        for j in l1:
            if i==j:
                k+=1
        print(i,"==",k)
        l2.append(i)