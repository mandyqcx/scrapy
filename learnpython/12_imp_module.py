# -*- encoding:utf-8 -*-

#%%
import sys

def test():
    args=sys.argv
    print(args)
    if len(args)==1:
        print('print hello')
    elif len(args)>=2:
        print('name is {0}'.format(args[0]),str(args[1:]))

if __name__=='__main__':
    test()


#%%sys模块
#sys有一个argv变量，储存了命令行的所有参数，至少包含一个参数:文件名


#%%if __name__=='main'
#每个py文件都包含内置的变量__name__,当文件被直接执行的时候，__name__等于文件名（含py后缀）
#当文件被import到其他文件的时候，__name__等于模块名称（文件名，但不含py后缀）
#'__main__'始终当前文件的名称（含py后缀）
#所以直接执行该文件，会输出结果，如果作为模块导入，不会输出结果
