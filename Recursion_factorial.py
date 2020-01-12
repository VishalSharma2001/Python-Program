import sys
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()
greet()
'''
#recursion fact 
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=5
print(factorial(num))
'''
'''
#Normal factorial
def fact(x):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=5
print(fact(n))
'''
'''
res=fact(n)
print(res)
'''
