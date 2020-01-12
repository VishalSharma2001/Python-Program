'''
class computer:
    def confic(self):
        #for i in range(5):
            print("4gb,500gb,celerion")
            

com1=computer()
computer.confic(com1)
com1.confic() #also use


com2=computer()
computer.confic(com2)
for i in range(10000):
    com2.confic()

'''
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def confic(self):
        print("The confic is:",self.cpu,self.ram)
            

com1=computer("i3","4gb")
com2=computer("i5","8gb")


com1.confic()
com2.confic()

