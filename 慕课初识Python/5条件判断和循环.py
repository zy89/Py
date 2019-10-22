# -*- coding: utf-8 -*

#1.if语句
age = 20
if age >= 18:    #if后面要:
    print 'your age is', age     #缩进严格按照4个空格形成代码块，不要tab
    print 'adult'
print 'END'

#2. if..else
score = 55
if score>=60:
    print 'passed'
else:
    print 'failed'

#3. if-elif-else
score = 85
if score>=90:
    print 'excellent'
elif score>=80:    #elif就是 else if
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'

#4. for循环
L = [75, 92, 59, 68]
sum = 0.0
for score in L:  #score是在for循环中定义的，依次取出L中的元素并赋值给score
    sum=sum+score
print sum / 4

#5 while循环
sum = 0
x = 1
while x<100:
    sum=sum+x
    x=x+2
print sum

#6 break：计算1+2+4+8...前20项的和
sum = 0
x = 1
n = 1
while True:
    sum=sum+x
    x=x*2
    n=n+1
    if n>20:
        break
print sum

#7 continue：计算100以内所有奇数的和
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2==0:
        continue
    sum=sum+x
print sum

#8 多重循环：打印出100以内所有十位数小于个位数的数
for x in [ 1,2,3,4,5,6,7,8,9 ]:
    for y in [ 1,2,3,4,5,6,7,8,9 ]:
        if x<y:
            print x*10 + y