'''
n=int(input("Enter the Number="))
for i in range(2,n):
    if n%i==0:
        print("The Number is not prime")
        break
else:
    print("The Number is prime")
'''

n=int(input("enter the Number of element want="))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
      

