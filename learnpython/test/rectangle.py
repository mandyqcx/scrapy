class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def set_size(self,size):
        self.width,self.height=size
    def get_size(self):
        return self.width,self.height

if __name__=='__main__':
    r=Rectangle()
    r.width=10
    r.height=5
    print(r.get_size())
    r.set_size((150,100))
    print(r.width)
    print(r.height)

