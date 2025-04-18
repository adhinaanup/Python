#inheritance#
class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
       print("feature 2 is working")
class B:
    def feature1(self):
        print('feature 3 is working')
    def feature4(self):
        print(self.m1+self.m2+self.m3)
class C(A,B):
  def feature5(self):
      print(self.m1*50)
c1=C()
c1.feature1()
class C(B):
    def feature5(self):
        print(self.m1*50)
b1=B()
b1.feature1()# init method
class A:
    def __init__(self):
        print('a is working')
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def __init__(self):

        super().__init__()
        print('b is working')
    def feature1(self):
        super().feature1()
        print("feature 3 is working")
    def feature4(self):
        print(self.m1+self.m2+self.m3)
b1=B()
b1.feature1()
class C(B,A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print(self.m1+self.m2+self.m3)
a=A()
b=B()
c=C()
c.feature1()#\same method in parent and child class
class A:
    def __init__(self):
        print('a is working')
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B:
    def __init__(self):
        print('b is working')
    def feature1(self):
        print("feature 3 is working")
    def feature4(self):
        print(self.m1+self.m2+self.m3)
class C(B,A):
    def feature1(self):
        print("feature 3 is working")
    def feature4(self):
        print(self.m1+self.m2+self.m3)
c1=C()
c1.feature1()