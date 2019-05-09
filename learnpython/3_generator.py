"""受到内存限制，列表的容量是有限的且占据了很大的存储空间，
如果只需要访问列表中的几个元素，则其他元素所占的空间则浪费了
如果能在循环的过程中不断推算出后续的元素，则不需要创建完整的list,节省大量的空间
在python中一边循环一边计算的机制，称为生成器,generator"""

#%%
#列表生成式
L=[x*x for x in range(10)]
print(L)
#将列表生成式的[]改成()，则变为生成器
G=(x*x for x in range(10))
print(G)

#%%
#打印生成器使用next()函数,但是基本上不会调用它，而是使用for循环
print(next(G))

#%%
for g in G:
    print(g)


#%%
#斐波拉契数列
def fib_1(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib_1(6))


#%%
#改成斐波拉契生成器，将print改成yield
#函数定义中如果有yield,则这个函数不再是一个普通函数，而是一个生成器
def fib_2(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

for n in fib_2(6):
    print(n)


#%%
#生成器在每次调用next()的时候执行，遇到yield返回，再次执行的时候从上次的yield语句继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield (5)

#调用生成器的时候，首先要生成一个生成器的对象，然后用next()函数不断获得下一个返回值
#在第四次使用next()函数的时候报错StopIteration
o=odd()
print(next(o))
print(next(o))
print(next(o))
#print(next(o))
#print(next(o))

#用for循环调用生成器的时候，会发现拿不到生成器的return语句的返回值，
#如果要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
#%%
g=fib_2(6)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value',e.value)
        break


#%%
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#杨辉三角

def triangles(n):
    L=[]
    for i in range(n):
        if i<=1:
            L.insert(i,1)
            yield L
        else:
            G=L[:]
            for t in range(1,i):
                L[t]=G[t]+G[t-1]
            L.insert(i,1)
            yield L

for n in triangles(10):
    print(n)

#%%
def triangles_2(n):
    L=[]
    for i in range(n):
        L.insert(i,1)
        G = L[:]
        for t in range(1, i):
            L[t] = G[t] + G[t-1]
        yield L


for n in triangles_2(1):
    print(n)


#%%
for i in range(1,4):
    print(i)


