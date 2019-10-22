# -*- coding: utf-8 -*

#2.Py的函数以及调用
#绝对值abs()
print abs(-20)

#比较函数cmp(x,y);x<y返回-1，x==y返回0，x>y返回1
print cmp(1,2)
print cmp(2,1)
print cmp(3,3)

#int()函数，把其他数据类型转换为整数
print int('123')
print int(12.34) #12

#str()函数，转换为string
print str(123)

#sum()函数，接收一个list并返回所有元素之和
L = []
x=1
while x<=100:
   L.append(x*x)
   x=x+1
print sum(L)

#3.编写函数
'''
使用def语句，依次写出函数名，括号，括号中的参数和冒号。返回值用return
'''
def square_of_sum(L):
    sum=0
    for x in L: 
        sum=sum+x*x
    return sum

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

#4.多返回值函数
import math
def move(x,y,step,angle):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print int(x),int(y)  #其实返回的是一组tuple

#5.递归函数; 使用递归函数需要注意防止栈溢出。
'''
计算阶乘 n!=1*2*3*4...*(n-1)*n = (n-1)! * n = fact(n-1) *n
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(5)

#6.定义默认参数; 
'''
由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面:
def fn1(a, b=1, c=2):可以  def fn2(a=1, b):不行

定义x的n次方的函数：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    调用power需要传两个参数，如果就需要算平方，可以这样写：
'''
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)  

#7.定义可变参数：加*
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)