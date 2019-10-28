# -*- coding: utf-8 -*

#1.生成列表
# 生成[1x2, 3x4, 5x6, 7x8,9x10]的list
print [x*(x+1) for x in range(1,11,2)]

#2.复杂表达式
'''
打印出来的结果保存在html就可以看到结果;
字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

#3条件过滤：for循环后面加个if判断
print [x * x for x in range(1, 11) if x % 2 == 0] #只输出偶数

'''
upper()
isinstance(x,str)判断变量是否为字符串
'''
def toUppers(L): #将字符串变大写，剔除不是字符串的变量
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello', 'world', 101])

#4多层表达式
L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)
print L
#也可以写成：
print [m + n for m in 'ABC' for n in '123']