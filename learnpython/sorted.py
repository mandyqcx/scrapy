"""python内置的sorted()函数就可以对list进行排序"""

#%%
sorted([36,5,-12,9,-21])


#%%可以接收一个key函数来实现自定义的排序
sorted([36,5,-12,9,-21],key=abs)


#%%按照字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
sorted(['bob','about','Zoo','Credit'])


#%%忽略大小写的排序
sorted(['bob','about','Zoo','Credit'],key=str.lower)


#%%反向排序
sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)


#%%用一个tuple表示学生和成绩
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted对上述列表分别按名字排序
def by_name(t):
    sorted(t)

L= [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
by_name(L)


sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)])




