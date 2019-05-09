"""filter()函数用于过滤序列，filter()接收一个函数和一个序列，和Map()不同的是，filter()把传入的函数依次作用
于每个元素，然后根据是True或者False来决定保留还是丢弃元素"""

#%%
#在一个list中,删掉偶数，保留奇数
def is_odd(n):
    return n%2==1

f=list(filter(is_odd,[1,2,3,4,5]))
print(f)


#%%
#将一个序列中的空字符串删掉
#strip()用于移除字符串头尾指定的字符，默认为空格或者换行符
def not_empty(s):
    if s==None:
        return False
    else:
        return s.strip()

f=list(filter(not_empty,['bds','ff','','   ',None]))
print(f)


#%%
s=['bds ',' ff']
for i in s:
    print(i.strip())


#%%求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n <1000:
        print(n)
    else:
        break


#%%
#筛选出回数

