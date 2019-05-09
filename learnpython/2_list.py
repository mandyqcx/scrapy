'''列表生成式'''
#%%第一种方法
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)


#%%第二种方法
L2=[]
for i in L1:
    if isinstance(i,str):
        L2.append(i.lower())
    else:
        L2.append(i)
print(L2)


#%%第三种方法,将for放到if之后
L2=[i.lower() if isinstance(i,str) else i for i in L1]
print(L2)


#%%利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
#使用递归
def trim(s):
    if s[0]==' ':
        return trim(s[1:])
    elif s[-1]==' ':
        return trim(s[0:-1])
    else:
        return s

trim('  hello ')


#%%for循环值作用于可迭代对象
#判断一个对象是否是可迭代对象
from collections import Iterable
isinstance('abc',Iterable)
isinstance(123,Iterable)


#%%emumerate函数可以将list表变成索引-元素对，可在for循环中同时迭代索引和元素本身
for i ,value in enumerate(['A','B','C']):
    print(i,value)



