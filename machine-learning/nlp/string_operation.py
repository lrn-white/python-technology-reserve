import operator

# python基础类库中常用的对字符串处理

# 1.去空格及特殊符号
s = ' hello world!'
print(s.strip())
print(s.lstrip(' hello,'))
print(s.rstrip('!'))

"""
hello world!
world!
 hello world
"""

# 2.连接字符串
sStr1 = "strcat"
sStr2 = 'append'
sStr1 += sStr2
print(sStr1)
"""
strcatappend
"""

# 3.查找字符
sStr1 = 'strchr'
sStr2 = 'r'
nPos = sStr1.index(sStr2)
print(nPos)
"""
2
"""

# 4.比较字符串
sStr1 = 'strchr'
sStr2 = 'strch'
print(operator.eq(sStr2, sStr1))
print(operator.eq(sStr1, sStr2))
print(operator.eq(sStr1, sStr1))
"""
False
False
True
"""

# 5.字符串中的大小写转换
sStr1 = 'JCstrlwr'
sStr1 = sStr1.upper()
sStr1 = sStr1.lower()
print(sStr1)
"""
jcstrlwr
"""

# 6.翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print(sStr1)
"""
gfedcba
"""

# 7.查找字符串
sStr1 = 'abcdefg'
sStr2 = 'cde'
print(sStr1.find(sStr2))
"""
2
"""

# 8.分割字符串
sStr1 = 'ab,cde,fgh,ijk'
print(sStr1.split(","))
"""
'ab', 'cde', 'fgh', 'ijk']
"""
