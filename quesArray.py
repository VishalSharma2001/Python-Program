from array import *

arr=array('i',(25,52,36,45))
k=arr[2]
for i in arr:
    if i==k:
        arr[2]=0
        break

print(arr)
   

'''
arr=array('i',(25,52,36,45))
n=3
for i in arr:
    print(arr[n])
    n=n-1
   
'''
'''
   #In Built function 
arr=array('i',(25,52,36,45))
arr.reverse()
print(arr)
'''
