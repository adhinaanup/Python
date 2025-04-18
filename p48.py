class employ:
    def __init__(self,salary,position,name):
        self.salary=salary
        self.__position=position
        self.__salary=name
    def show(self,e):
        if self.__position=='manager':
            print(e.__position)
        else:
            print('unautharized access')
    def update(self,o,u):
        if self.__position=='manager':
            o.__salary=u
            print(o.__salary)
        else:
            print('unautharized acccess')
c1=employ(1000,'manager','shana')
c2=employ(500,'salesman','naseeha')
c1.show(c2)
c1.update(c2,10000)