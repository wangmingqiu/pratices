# -*- coding: utf-8 -*-
from datetime import datetime
'''x = input("请输入一个字符串：")
y = x.split("-")
print(y)'''
def count(year,month,day):
    count = 0
    if year%400==0 or (year%4==0 and year%100!=0):
        list1 = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            count += list1[i]
        return count + day
    else:
        list2 = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            count += list2[i]
        return count + day
def weekday(year,month,day):
    weekdays = datetime(year,month,day).isocalendar()[1]

    return weekdays
if __name__ == "__main__":
    x = input("请输入日期：")
    y = x.split("-")
    year = int(y[0])
    month = int(y[1])
    day = int(y[2])
    count = count(year,month,day)
    weekdays = weekday(year,month,day)
    print('%d %d'%(count,weekdays))