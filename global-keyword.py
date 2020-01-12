'''
a=10
def something():
    a=15
    print(a)
something()
print(a)
'''
'''
a=10
def something():
    global a 
    a=15
    print(a)
something()
print(a)
'''
a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print(a)
    globals()['a']=15
something()
print(a)
