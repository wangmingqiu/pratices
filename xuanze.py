# -*- coding: utf-8 -*-
l = [8,3,2,50]
for i in range(0,len(l)-1):
    minindex = i
    for j in range(i,len(l)):
        if l[j] < l[minindex] :
            l[j],l[minindex] = l[minindex],l[j]
print(l)