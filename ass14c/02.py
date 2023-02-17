matrix1=[]
matrix2=[]
matrix3=[]
print("Enter values of matrix 1 row wise : ")
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    matrix1.append(a)
print("Enter values of matrix 2 row wise : ")
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    matrix2.append(a)
print("Sum of matrix = ")
for i in range(3):
    a=[]
    for j in range(3):
        a.append(matrix2[i][j]+matrix1[i][j])
    matrix3.append(a)

for i in range(3):
    for j in range(3):
        print(matrix3[i][j],end=" ")
    print()