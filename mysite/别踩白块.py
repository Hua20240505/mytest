#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 计算净利润的税收
i = int(input('123456'))
# 税率阶梯限制
arr = [1000000,600000,400000,200000,100000,0]
# 不同利润对应的税率
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
# 遍历税率阶梯
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
# 输出总税收
print r