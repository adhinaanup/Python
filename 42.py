# create a class called animals
# and create attributes like color, size
# create method get to get the value of the attributes and set to set a new value for the attributes
# create a class method and instance method

class animals:
    def __init__(self,color,size):
        self.color=color
        self.size=size
    def get(self):
        print('Color : ',self.color,'Size : ',self.size)
    def set(self,color,size):
        self.color=color
        self.size=size

    @classmethod
    def info(cls):
        return 'Animals'

a=animals('Brown','Large')
a.get()
a.set('White','Small')
a.get()
print(animals.info())

