l1=[21,28,31,35,86,1251]
l2=[25,25,26,1,32,38,84,1288]
l3=l1+l2
l3.sort()
print(l3)
# j=0
# i=0
# while i<len(l1):
#     while j<len(l2):
#         if l1[i]>=l2[j]:
#             l1.insert(i, l2[j])
#             j+=1
#         elif l2[len(l2)-1]>l1[len(l1)-1]:
#             l1.append(l2[len(l2)-1])
#         else:
#             break
#     i+=1
# print(l1)