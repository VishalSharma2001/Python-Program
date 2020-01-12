'''
class student:
    
    def __init__(self):
        name=input("Enter the name:")
        self.name=name
s1=student()
print(s1.name)
'''
class student:

    def __init__(self):
        name=input("Enter the name:")
        age=int(input("Enter the age:"))
        self.name=name
        self.age=age
        # self.lap=self.laptop()     #Inner class call in the main class  

    def  show(self):
        print(s1.name,s1.age)
        # self.lap.show()            #Inner class call in the main class 
    class laptop:

        def __init__(self):
            brand=input("Enter the name of brand:")
            cpu=input("Enter the name of cpu:")
            ram=int(input("Enter the ram :"))
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
        
s1=student()
s1.show()
lap=student.laptop()               #class call in the outside of class 
lap.show()                         #class call in the outside of class 

