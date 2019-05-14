# -*- encoding:utf-8 -*-

'''在类的内部，可以有属性和方法，外部代码可以直接修改实例的属性，但是也可以限制修改'''

#%%
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('{0}:{1}'.format(self.name,self.score))

bart=Student('Bob',12)
bart.score


#%%外部代码修改实例的属性
bart.score=299
bart.score


#%%禁止内部属性被外部访问，在属性的名称前面加两个下划线__，变成私有属性，只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('{0}:{1}'.format(self.__name,self.__score))

bart=Student('Bob',12)
bart.__score


#%%如果外部代码要获取属性，则可以给类增加获取属性的方法
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('{0}:{1}'.format(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart=Student('Bob',12)
bart.get_score()


#%%但是实际上不是完全不可访问
bart=Student('Kate',13)
bart._Student__name


#%%在外部代码中对修改属性，可以增加修改的方法，且可以在方法中做参数检查
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('{0}:{1}'.format(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('wrong score')

bart = Student('Bob', 12)
bart.set_score(14)
bart.get_score()


#%%注意不要在外部代码中修改__变量，因为修改后的这个变量和类中的变量不是同一个量
bart.__name='Piter'
bart.__name

#%%
bart.get_name()
