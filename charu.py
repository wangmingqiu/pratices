# -*- coding: utf-8 -*-
l = [8,5,2,50]
for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j] < l[j-1]:
            l[j],l[j-1] = l[j-1],l[j]
        else:
            break
print(l)