 # -*- coding: utf-8 -*
print("hello world PY")
print 'The quick brown fox', 'jumps over', 'the lazy dog'   # 逗号是空格

'''
\n 表示换行
\t 表示一个制表符
\\ 表示 \ 字符本身
'''
print "Python was started in 1989 by \"Guido\".\nPython is free and easy to learn."
print r'\(~_~)/ \(~_~)/' #有一个r在前面，后面就不需要转义了

print u'中文'  # 以一个u开头表示Unicode，支持中文等

print ur'''静夜思  # ur连用
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''

print 11/4  # 整数除以整数仍然是整数
print 11%4
print 11.0/4 #用浮点除以整数就可以得到浮点
print 11/4.0

# 0、空字符串''和None是false，其他数值和非空字符串是True。遵循短路计算
a = True
print a and 'a=T' or 'a=F' #输出是a=F，因为and要求计算两个值，因此返回后一个a=F。or只需要计算第一个值，因此a=F返回了