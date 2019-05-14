# -*- encoding:utf-8 -*-

#%%给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    def __init__(self,name):
        self.name=name

s=Student('Bob')
s.score=90


#%%如果类本身需要绑定一个属性，可以在class中定义属性，这种属性是类属性，归类所有,但是任何实例都可以访问到
class Student(object):
    name='Student'

s=Student()
print(s.name)
print(Student.name)


#%%给实例绑定一个属性
s.name='Michel'
print(s.name)

print(Student.name)


#%%删除实例的属性
del s.name
print(s.name)

