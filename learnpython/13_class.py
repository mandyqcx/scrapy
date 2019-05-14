# -*- encoding:utf-8 -*-
'''面对对象最重要的概念是类和实例，类是抽象的模板，实例是根据类创建出来的一个个具体的对象，
每个对象都有相同的方法，但各自的数据可能不同'''

#%%定义类,类名通常是大写开头的单词，后面跟(object)，表明该类是从哪个类继承下来的
class Student(object):
    pass

Student


#%%根据Student类创建实例，创建实例是通过类名+()实现的
bart=Student()
bart


#%%可以自由地给一个实例变量绑定属性
bart.name='Bart'
bart.name


#%%类可以起到模板的作用，在创建实例的时候，可将必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法，在创建实例的时候，将属性绑上去
#__init__方法的第一个参数永远是self,表示创建的实例本身，所以在方法内部，可将各种属性绑定到实例上
#有__init__方法之后，实例就不能传入空的参数了，必须传入与__init__方法匹配的参数
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

bart=Student('Bob',12)
bart.name
bart.score


#%%数据封装
#每个实例拥有各自的数据之后，可以通过函数来访问这些数据
def print_score(std):
    print('{0}:{1}'.format(std.name,std.score))

print_score(bart)

#%%也可以直接在类的内部定义访问数据的函数，这就是将数据封装起来了，这种函数叫做类的方法
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('{0}:{1}'.format(self.name,self.score))

bart=Student('Bob',12)
bart.print_score()

