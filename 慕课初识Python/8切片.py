# -*- coding: utf-8 -*

#对list切片; 对tuple切片操作也一样，输出为tuple
L = ['Adam', 'Lisa', 'Bart', 'Paul']

a = L[0:3]  #从index0开始到index3，不包括3。
#如果默认从index0，也可以写作 L[:3]
print a  

b = L[:] #从头到尾。相当于复制初一个新list
print b   

c = L[::2]  #每n个取一个，2表示每两个取一个
print c

L = range(1, 101)  #range()创建一个数列；(1,2,3....100)

print L[0:10] #前10个数
print L[2::3] #3的倍数
print L[4:50:5] #不大于50的5的倍数
