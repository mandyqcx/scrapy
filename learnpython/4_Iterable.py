"""可以直接作用于for循环的数据类型有以下几种：
集合数据类型，list,tuple,dict,set,str
generator,包括生成器和带yield的generator function

可以直接作用于for循环的对象统称为可迭代对象：Iterable"""

#可以使用isinstance()判断一个对象是否是Iterable对象
#%%
from collections import Iterable
isinstance([1],Iterable)

#%%
isinstance({},Iterable)

#%%
isinstance('abc',Iterable)

#%%
isinstance((x for x in range(10)),Iterable)

#%%
isinstance(100,Iterable)

#可以被next()函数调用并不断返回下一个值的对象称为'迭代器'
#%%
from collections import Iterator
isinstance((x for x in range(10)),Iterator)

#%%
isinstance([],Iterator)

#%%
isinstance({},Iterator)

#%%
isinstance('abc',Iterator)


#生成器都是Iterator对象，但是list,dict,str虽然是Iterable的，但是不是Iterator
#把list,dict,str等Iterable变成Iterator可以使用iter()函数
#%%
isinstance(iter([]),Iterator)

#%%
isinstance(iter('abc'),Iterator)


#%%Iterator是一个数据流，在被next()函数调用的时候不断返回下一个数据，直到没有数据时抛出stopIteration错误
#for循环本质上就是不断调用next()函数实现的
it=iter([1,2,3,4,5,6])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration as e:
        break


