class computer:
    def __init__(self):
        self.name="vishal"
        self.age=28

    def update(self):
        self.age="18"

    def compare(self,c2):
        if self.name==c2.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.name="kim"
#c1.update()
print(c1.name,c1.age)
print(c2.name,c2.age)
if c1.age==c2.age:
    print("same")
else:
    print("different")
if c1.compare(c2):
    print("again same")
else:
    print("again different")
    
