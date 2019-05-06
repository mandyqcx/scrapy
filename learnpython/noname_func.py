#-*- encoding:UTF-8 -*-
'''关键字lambda表示匿名函数，冒号前面的x表示函数参数，只能有有个表达式，不用写return，返回值就是该表达式的结果'''
#%%匿名函数
list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))

#匿名函数lambda x: x*x实际上是
#def f(x):
#    return x*x

#%%匿名函数没有名字，不用怕函数名冲突，匿名函数也是一个函数对象，可以将匿名函数赋予一个变量，再利用变量来赋值
f=lambda x:x*x
f(5)


#%%可以将匿名函数作为返回值返回
def build(x,y):
    return lambda: x*x + y*y

c=build(3,4)
print(c())

#%%
def is_odd(n):
    return n%2==1

L=list(filter(is_odd,range(1,20)))
print(L)

#%%
list(filter(lambda x:x%2==1,range(1,20)))

