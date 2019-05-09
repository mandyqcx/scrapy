#%%位置参数
def power(x):
    return x*x

power(5)


#%%power(x)修改为power(x,n),计算任意n次方，两个参数都是位置参数，传入的两个值按照位置顺序依次赋予参数x和n
def power(x,n):
    s=1
    while n>0:
        n-=1
        s=s*x
    return s

power(5,3)


#%%默认参数
#默认参数可以简化函数的调用（1.必选参数在前，默认参数在后；（2.有多个默认参数时，可以按顺序提供默认参数，如果不按顺序提供参数，则指定名称提供默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

power(6)
power(4,7)


#%%默认参数的坑
#定义一个函数，传入一个list,添加一个end再返回
def add_end(L=[]):
    L.append('End')
    return L

add_end([1,2,3])

#%%使用默认参数调用
#第一次调用的时候会输出['End']，第二次调用的时候会输出['End', 'End']，以此类推
#Python函数在定义的时候，默认参数L是一个变量，它指向对象[]，在第一次调用函数的时候，变量L就改变了，则下次调用时，不再是函数定义时的[]了。
add_end()

#%%定义默认参数要牢记一点：默认参数必须指向不变对象！
#因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L

add_end()


#%%可变参数，允许传入0个以上任意参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*number):
    sum=0
    for n in number:
        sum=sum+n
    return sum

calc(1,2,3,4)


#%%关键字参数,允许传入0个以上的含参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def person(name,age,**kwargs):
    print('name:',name,'age:',age,'other:',kwargs)

person('Michale',30)

#%%
person('Bob',35,city='Beijing')


#%%命名关键字参数，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name,age,*,city,job):
    print(name,age,city,job)

person('jack',24,city='Beijing',job='Engineer')

#%%如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

#命名关键字参数必须传入参数名，这与位置参数不同，如果没有传入参数名，调用将报错
#由于调用的时候趋势参数名city和job,python将这4个参数视为位置参数，但是函数仅接受2个位置参数
person('jack',24,'Beijing','Engineer')

#%%命名关键字参数可以有缺省值，从而简化调用
#特别注意，如果没有可变参数，必须加一个*作为特殊分隔符，如果缺少，python将无法识别位置参数和命名关键字参数
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

person('Jack',24,job='Engineer')


#%% *仅作为特殊分隔符，分隔位置参数和关键字参数
def person(name,age,*,city,job):
    print(name, age, city, job)

person('Jack',24,2019,city='Beijing',job='Engineer')


#%% *kwargs是可变参数，也能分隔位置参数和关键字参数
def person(name, age, *kwargs, city, job):
    print(name, age, city, job)

person('Jack', 24, 2019, city='Beijing', job='Engineer')


#%%参数组合
#定义函数，可以选必选参数，默认参数，可变参数，关键字参数和命名关键字参数，
# 但是参数定义的顺序必须是：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kwargs):
    print(a,b,c,args,kwargs)

def f2(a,b,c=0,*,d,**kwargs):
    print(a,b,c,d,kwargs)

f1(1,2,23,46,fksj='kfisdji',kdjf='kdjs')

f2(1,2,3,d=99,gfkk='kdjkfkdm')


#%%以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*args):
    sum=1
    for n in args:
        sum=sum*n
    print('procudt{0}={1}'.format(args,sum))

product(1,4,6,4)


