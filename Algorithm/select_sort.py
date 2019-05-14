# -*- encoding:UTF-8 -*-

#去列表中最小的值
def select_smallest(item):
    smallest=item[0]
    for i in item:
        if smallest>i:
            smallest=i
    return smallest


def select_sort(item):
    result=[]
    for i in range(len(item)):
        smallest=select_smallest(item)
        result.append(smallest)
        item.remove(smallest)
    return result


if __name__=='__main__':
    f=select_sort([3,5,2,6])
    print(f)
