def greet():
    print("Good Morning")
    print("vishal")
'''
def add(x,y):
    c=x+y
    print(c)
add(2,3)
'''
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
greet()
result1,result2 =add_sub(3,5)
print(result1,result2)
