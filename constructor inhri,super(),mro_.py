class A:
    def __init__(self,mamma):
        print(mamma,"this is feature of constructor A")
    def feature1(self):
        print("this is feature 1")
    def feature2(self):
        print("this is feature 2")
class B(A):
    
    def __init__(self):
        super.__init__('B')
        print("this is feature of constructor B")
    def feature3(self):
        print("this is feature 3")
    def feature4(self):
        print("this is feature 4")
a=B()
a.feature3()
