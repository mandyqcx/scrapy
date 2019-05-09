'''python的functools模块提供了很多的有用的功能，其中一个就是偏函数(partial_function)
通过设定参数的默认值，可以降低函数调用的难度，偏函数就可以做到这一点'''

#%%int()函数可以把字符串转换成整数，当仅传入字符时，int()函数默认按十进制转换
int('12345')

#%%int()函数提供额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换
int('12345',base=8)

#%%
int('12345',base=16)


#%%假设要转换大量的二进制字符串，每次都传入int(x,base=2)非常麻烦，所以可以定义一个int2()函数，默认将base=2传入
def int2(x,base=2):
    return int(x,base)

int2('100000')


#%%functools.partial可以帮助创建一个偏函数，不需要自定义int2
import functools
int2=functools.partial(int,base=2)
int2('100001')


#%%所以functools.partial的作用就是，把一个函数的某些参数固定住(也就是设置默认值),返回一个新的函数，调用这个函数会更简单
#创建偏函数的时候，实际上可以接收函数对象，*args,**kwargs这三函数
int2=functools.partial(int,base=2)
#相当于
kwargs={'base':2}
int('10010',**kwargs)


#%%实际上是默认将10作为*args的一部分自动加到左边
max2=functools.partial(max,10)
max2(5,6,7)


#%%hex(x)：将整数转成十六进制的数字输出
hex(34)
