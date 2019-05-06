# -*- coding: utf-8 -*-
#第一种方法
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)


#第二种方法
L2=[]
for i in L1:
    if isinstance(i,str):
        L2.append(i.lower())
    else:
        L2.append(i)
print(L2)


#第三种方法,将for放到if之后
L2=[i.lower() if isinstance(i,str) else i for i in L1]
print(L2)

