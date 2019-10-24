# -*- coding: utf-8 -*
'''
Python的for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。
因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。
'''
#1.迭代打印出100以内7的倍数
for i in range(1,101):
    if i%7 == 0:
        print i

#2.index迭代
'''
实际上enumerate()把原list变成[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
迭代的每个元素其实是一个tuple： (index, element)
'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

#zip()函数把两个list合成一个，一一对应
#如果要输出L的名字且从1开始，就可以用zip()
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name

#3.迭代dict的value
'''
dict对象有一个values()方法，可以把dict转换成包含所有value的list。可print
还有一个itervalues()作用一样，但是它不会转换。只是依次取出dict中的value值。节省内存。不可print
'''
#计算平均分
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for s in d.values():
    sum = sum+s
print sum/len(d)