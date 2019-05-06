class MyClass:
    @staticmethod #静态方法
    def smeth():
        print('This is a static method')

    @classmethod #类方法
    def cmeth(cls):
        print('This is a class method of',cls)

