class A:
    def feature1(self):
        print("this is feature 1")
    def feature2(self):
        print("this is feature 2")

class B(A):                             #single inheritance
    def feature3(self):
        print("this is feature 3")
    def feature4(self):
        print("this is feature 4")

    
class C(B):                             #multi-level inheritance
    def feature5(self):
        print("this is feature 5")
    def feature6(self):
        print("this is feature 6")

class D:
    def feature7(self):
        print("this is feature 7")
    def feature8(self):
        print("this is feature 8")
class E(A,D):                           #multiple inheritance
    def feature9(self):
        print("this is feature 9")
    def feature10(self):
        print("this is feature 10")
    




a=A()
b=B()
c=C()
d=D()
e=E()
a.feature1()
a.feature2()
b.feature3()
b.feature4()
b.feature2()
b.feature1()
c.feature1()
c.feature2()
c.feature3()
c.feature5()
e.feature1()
e.feature9()
e.feature8()
