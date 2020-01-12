from numpy import *
'''
arr1=array([1,2,3,4,5])
arr1=arr1+2
print(arr1)
'''
'''
arr1=array([1,2,3,45,5])
#print(sin(arr1))
#print(cos(arr1))
#print(log(arr1))
#print(max(arr1))
print(sort(arr1))
'''
'''
arr1=array([1,2,3,4,5])
arr2=array([24,13,24,55,51])
arr3=arr1+arr2
print(arr3)
#print(concatenate([arr1,arr2]))
'''
'''
arr1=array([1,2,3,4,5])
arr2=arr1.view()
arr1[1]=5
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
'''
'''
arr1=array([1,2,3,4,5])
arr2=arr1.copy()
arr1[1]=5
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
'''
 #assignment1
'''
arr=array([1,2,3,4,5])
for i in arr:
     arr=i+5
     print(arr)    
'''
#assignment2
'''
arr1=array([1,2,3,4,5])
arr2=array([24,13,24,55,51])
k=0
j=0
for i in range(5):
    arr3=arr1[k]+arr2[j]
    k+=1
    j+=1
    print(arr3)
'''






