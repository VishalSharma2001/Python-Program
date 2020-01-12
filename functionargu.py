'''
def update(x):
    print(id(x))    
    x=8
    print(id(x))
    print("X=",x)




a=10
print(id(a))
update(a)
print("a=",a)
'''
'''
def update(li):
    print(id(li))    
    li[1]=15
    print(id(li))
    print(li)




li=[10,30,20]
print(id(li))
update(li)
print(li)
'''
'''
def sum(a,b):
    c=a+b
    return c
res=sum(6,5)
print(ress)
'''

'''
def person(name,age=19):
    print(name)
    print(age)
persion("vishal",18)
persion(age=15,name='kimi')
'''
'''
def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
sum(1,2,5,8)
'''
'''
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(1,2,5,8)

'''
'''
def person(name,*data):
    print(name,end="")
    print(data)
person('vishal',28,"surajgarh",978581)
   '''
'''
def person(name,**data):
    print(name)
    print(data)
person('vishal',age=28,city="surajgarh",mob=978581)
'''
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('vishal',age=28,city="surajgarh",mob=978581)
               












    












