# -*- coding: utf-8 -*

#1.对list切片; 对tuple切片操作也一样，输出为tuple
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

#2.倒序切片
L = ['Adam', 'Lisa', 'Bart', 'Paul']

L[-2:] #倒2开始到结束：['Bart', 'Paul']

L[:-2] #index0开始到倒2：['Adam', 'Lisa']

L[-3:-1] #倒3开始到倒1，不包括倒1：['Lisa', 'Bart']

L[-4:-1:2] #倒4开始到倒1，每2个取一个：['Adam', 'Bart']

#3.字符串切片，输出仍是字符串。规则都一样
#输出string首字母大写
def firstCharUpper(s):
    a = s[0].upper()+s[1:]
    return a

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
    


