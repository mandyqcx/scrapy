# -*- encoding:utf-8 -*-

'''当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。'''

#%%子类继承父类
class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    pass

dog=Dog()
dog.run()


#%%对子类增加一些方法
class Dog(Animal):
    def shout(self):
        print('I am a dog')

dog=Dog()
dog.shout()


#%%当子类和父类都有相同的方法的时候，子类的方法覆盖了父类的方法
class Dog(Animal):
    def run(self):
        print('a dog is runing')

    def shout(self):
        print('I am a dog')

dog=Dog()
dog.run()


#%%当定义了一个class的时候，实际上定义了一种数据类型
#a,b,c分别对应list,Animal,Dog类型
a=list()
b=Animal()
c=Dog()

isinstance(a,list)
isinstance(b,Animal)
isinstance(c,Dog)


#%%Dog可以看成是Animal类型，但是Animal不能看成是Dog类型
isinstance(b,Dog)
isinstance(c,Animal)


#%%多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())

#%%任何依赖于Animal作为参数的函数或者方法都可以不修改地正常运行
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
# 这就是多态真正的威力：调用方只管调用，不管细节，
# 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：

#对扩展开放：允许新增Animal子类；

#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
