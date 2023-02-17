str=input("Enter a string :")
str1=""
for i in range(len(str)-1,-1,-1):
    str1+=str[i]
print(str1)

# ================or====================

rstr=str[len(str)-1::-1]
print(rstr)