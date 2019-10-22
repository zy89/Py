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

#5 遍历dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for name in d:
    print name +":",d[name] 