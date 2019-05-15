# -*- encoding:UTF-8 -*-


#%%使用递归函数计算列表中元素的和
def sum(item):
    if len(item)<2:
        return 0
    else:
        return item[0]+sum(item[1:])


f=sum([1,2,3,4,5])
print(f)


#%%使用递归函数计算列表中包含的元素数
def count(item):
    if len(item)<2:
        return 1
    else:
        return 1+count(item[1:])

c=count([2,4,6,7,89,9])
print(c)


#%%找出列表中最大的数字
def find_max(item):
    if len(item)<2:
        return item[0]
    else:
        if item[0]>find_max(item[1:]):
            return item[0]
        else:
            return find_max(item[1:])

find_max([1,2,3,7,5])

