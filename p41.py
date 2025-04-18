class student:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def update(self,mark4):
        self.mark1=mark4
x=int(input('Enter mark1 : '))
y=int(input('Enter mark2 : '))
z=int(input('Enter mark3 : '))
obj1=student(x,y,z)
obj1.update(4)
print(obj1.mark1)

