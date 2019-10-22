# -*- coding: utf-8 -*
L = ["Adam",95.5,"Lisa",85,"Bart",59]
print L

#倒序索引，-1是最后一位
L = [95.5, 85, 59] 
print L[-1]
print L[-2]
print L[-3]

#添加元素
L = ['Adam', 'Lisa', 'Bart'] 
L.append('Jack')  #添加在数组最后
L.insert(2,'Paul') #添加在L[2]的位置
print L

#删除元素
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L.pop() #删除最后一个，并且返回它
L.pop(1) #删除L[1]
print L

#替换元素
L = ['Adam', 'Lisa', 'Bart']
L[0]='Bart'
L[2]='Adam'
print L

#Tuple元组：用()，无法增删改元素
t = (0,1,2,3,4,5,6,7,8,9)
print t

#单元素：加逗号，否则输出是1
t2=(1,)
print t2