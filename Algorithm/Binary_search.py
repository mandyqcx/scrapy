# -*- encoding:UTF-8 -*-

import math

def Binary_Search(x,list):
    index_begin=0
    index_end=len(list)-1
    index_medium=math.floor((index_begin+index_end)/2)

    while index_begin<index_end:
        if x>=list[index_begin] and x<=list[index_medium]:
            index_begin=index_begin
            index_end=index_medium
            index_medium=math.floor((index_begin+index_end)/2)
        elif x>=list[index_medium+1] and x<=list[index_end]:
            index_begin=index_medium+1
            index_end=index_end
            index_medium=math.floor((index_begin+index_end)/2)
        else:
            return None
    return index_begin


if __name__=='__main__':
    f=Binary_Search(3,[0,1,2,4,5,6])
    print(f)



