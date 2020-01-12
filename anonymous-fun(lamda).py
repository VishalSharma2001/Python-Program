'''
f=lambda a:a*a
result=f(5)
print(result)

#print(f(5))
g=lambda s,t : s+t
result=g(5,6)
print(result)
'''
from functools import reduce
nums=[3,2,6,8,4,6,2,9]
'''def eneb(n):
       return n%2==0
'''
'''
def dou(n):
     return n*2
'''
'''
def red(a,b):
    return a+b
    '''
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
double=list(map(lambda n:n*2,evens))
print(double)
su=reduce(lambda a,b:a+b,double)
print(su)
