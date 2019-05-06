#%%一般的求和函数
def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

calc_sum(1,3,5,7)


#%%不返回求和的结果，返回求和的函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

#调用lazy_sum()的时候，返回的不是求和的结果，而是求和函数
f=lazy_sum(1,3,5,7)
print(f)

#调用函数f时，才计算求和的结果
print(f())


###函数lazy_sum中又定义了函数sum,内部函数sum可以引用外部函数lazy_sum的参数和局部变量
###当lazy_sum函数返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包”
###当调用lazy_sum时，每次调用都会返回一个新的函数，即使传入相同的参数
#%%
f1=lazy_sum(1,3,5,7)
f2=lazy_sum(1,3,5,7)
f1==f2


#%%返回的函数并没有执行，直到调用了f()才执行
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()


##返回值都是9，因为返回的函数都引用了变量i,但是没有立即执行，等到3个函数都返回时，所引用的变量已经变成了3，所以最终结果为9
print(f1())
print(f2())
print(f3())


#%%不建议在闭包中引用循环变量，如果一定要引用循环变量，则再创建一个函数，用该函数的参数绑定循环变量当前的值
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())



#%%利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    def counter(j):
        def g():
            return j*j
        return g
    i=1
    while True:
        i+=1
        result=(counter(i))
        break
    return result

counterA = createCounter()
print(counterA())
print(counterA())
print(counterA())

