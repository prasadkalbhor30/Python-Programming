# sum of elements in a given list
l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
k=0
for i in l1:
    k+=i
print("Average of numbers in list =",k/len(l1))