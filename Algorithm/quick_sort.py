# -*- encoding:UTF-8 -*-

#%%
def quick_sort(item):
    if len(item)<2:
        return item
    else:
        pivot=item[0]
        less=[i for i in item[1:] if i<=pivot]
        greater=[i for i in item[1:] if i>pivot]
        return quick_sort(less)+ [pivot] + quick_sort(greater)

quick_sort([3,5,7,2,2,80,32])
