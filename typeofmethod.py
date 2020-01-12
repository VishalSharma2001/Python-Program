class school:

    school="BKBIET"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        #return(self.m1+self.m2+self.m3)/3
        print((self.m1+self.m2+self.m3)/3)
    @classmethod
    def schoolname(cls):
        print(cls.school)
    @staticmethod
    def info():
        print("HEY sir...")

    def compare(self):
        if self.m1>self.m2 and self.m1>self.m3:
            print("m1 is greater")
        elif self.m2>self.m3:
            print("m2 is greater")
        else:
            print("m3 is greater")


        
s1=school(85,72,72)
s2=school(92,65,85)
s1.avg()
s2.avg()
#print(s1.avg())
#print(s2.avg())
school.schoolname()
s1.info()
s1.compare()
        
