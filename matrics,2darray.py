from numpy import *
arr1=array([
        [1,2,3,4,4,8],
        [5,6,7,8,2,7]

     ])
'''
arr2=arr1.flatten() # 2d in 1d
arr3=arr2.reshape(3,4)
arr4=arr3.reshape(2,2,3)
print(arr4)
'''
'''
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
'''
#m=matrix(arr1)
m=matrix('1 2 3;4 5 6 ; 7 8 9')
print(m)
print(diagonal(m))
print(m.max())
m1=matrix('1 2 3 ; 4 5 6 ;7 8 9')
m2=matrix('3 4 5 ; 6 7 8 ;9 10 11')
m3=m1*m2
m4=m1+m2
print(m1)
print(m2)
print(m3)
print(m4)
