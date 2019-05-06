'''函数是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数'''
#%%
def now():
    print('2019-05-05')

f=now
f()


#%%函数对象由一个__name__属性，可以拿到函数的名字
now.__name__

#%%
f.__name__

#%%增强函数的功能，比如在函数调用的前后自动打印日志，但不希望修改函数定义，这种在代码运行期间动态增加功能的方式，称之为装饰器
#本质上，decorator是一个接受一个函数作为参数，并返回函数的高阶函数，将decorator置于函数的定义处
# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():' %func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print('2019-05-05')

now()


#%%相当于
no=log(now)
no()


#%%如果decorator()函数本身需要传入参数，则需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2019-05-05')

now()



#%%请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    def wrapper(*args,**kwargs):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args,**kwargs)
    return wrapper

@metric
def now():
    print('2019-05-05')

now()


#%%
import time,functools

def log(func):
    #@functools.wraps(func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        print('%s executed in %s ms' %(func.__name__,10000*(time.time()-t1)))
        return func(*args,**kwargs)
    return wrapper

@log
def fast(x,y):
    return x^y

fast(3,5)
