'''如何知道对象的类型，有什么方法'''

#%%使用type(),判断对象类型
type(134)

type('str')

type(None)

type(abs)


#%%使用type模块中定义的常量，判断一个对象是否是函数
import types
def fn():
    pass

type(fn)==types.FunctionType

type(fn)==types.BuiltinFunctionType

type(lambda x:x)==types.LambdaType

type(x for x in range(10))==types.GeneratorType


#%%使用isinstance(),判断对象是否是class


#%%判断一个变量是否是某种类型的一种,如判断是否是list或者tuple
isinstance([1,2,3],(list,tuple))

isinstance((1,2,3),(list,tuple))


#%%使用dir()获得一个对象的所有属性和方法，返回一个包含字符串的list
#类似__xxx__的属性和方法都是有特殊方法的
dir('ABC')


#%%配合getattr(),setattr()以及hasattr(),可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x=0
    def power(self):
        return self.x*self.x

obj=MyObject()


#%%
hasattr(obj,'x') #有属性'x'吗？

hasattr(obj,'y')

setattr(obj,'y',19) #设置一个属性'y'
hasattr(obj,'y')

getattr(obj,'y')

obj.y

#%%能写成obj.y，就不用写成getattr(obj,'y')
