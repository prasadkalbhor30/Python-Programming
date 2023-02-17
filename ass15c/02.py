str=input("Enter a string :")
pat=input("Enter pattern you want to check : ")
if pat in str:
    print("Given string contain given pattern")
else:
    print("Given string does not contain given pattern")
# ======or=========
k=0
for i in range(len(str)):
    if str[i]==pat[0]:
        l=i
        for j in pat:
            if str[l]!=j:
                break
            k+=1
            l+=1
if k==len(pat):
    print("Given string contain given pattern")
else:
    print("Given string does not contain given pattern")
