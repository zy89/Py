# -*- coding: utf-8 -*

#1. dict是数组每个元素包含key和value,可以通过key直接查找value。用{}表示dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'bart': 59,
    'Paul': 75
}
a=len(d) #dict也是数组可以直接访问长度
print a

#2.访问dict
'''如果dict没有这个key，则返回会显示KeyError。有两种方法可以避免
1.用in判断key是否存在
if 'Paul' in d:
    print d['Paul']

2.用get方法，key不存在的时候自动返回None
print d.get('Bart')
59
print d.get('Paul')
None
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:', d['Adam']
print 'Lisa:', d['Lisa']
print 'Bart:', d['Bart']
print d.get('Paul') #None

#3.dict特点：1.查找速度快，但是占用内存。list是查找慢，内存小
# 特点2：dict是无序的。特点3：key不可变，value无所谓

#4.更新dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d['Paul'] = 72 #加入新元素
print d
d['Bart'] = 60 #如果key已经存在，则替换原来的value
print d 

#5.遍历dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for name in d:
    print name +":",d[name] 

#6.set是一个无序不重复的数组。如果有重复元素则会自动去重
#声明方法是set([])
s = set(['A', 'B', 'C', 'C']) #只会有一个C，len也是3
print s

#7.访问set
s = set(['adam','bart']) #由于是无序所以没有index，只能用in访问
print 'Adam' in s #false，大小写敏感
print 'bart' in s

#8.set特点：1.访问速度快 2.元素不能变 3.无序;因此可以用来快速判断一些东西
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'Feb' # 用户输入的字符串
if x in weekdays:
    print 'input ok'
else:
    print 'input error'

#9.遍历set；用for
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0]+":",x[1]

#10 更新set；就是remove或者add元素
'''
如果已经有了，则add完不会报错但是也不会加进去。
remove如果没有的元素则会报错
'''
#对于s，如果list里面有的名字就删掉。没有的名字就加入
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s
