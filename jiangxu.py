# -*- coding: utf-8 -*-\
list1 = [5,9,2,7,4]
for i in range(1,len(list1)):
    for j in range(i,0,-1):
        if list1[j] > list1[j-1]:
            list1[j],list1[j-1] = list1[j-1],list1[j]
        else:
            break
print(list1)