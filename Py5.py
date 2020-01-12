Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=5

>>> num
5
>>> id(num)
1926183232
>>> a=10
>>> id(a)
1926183312
>>> id(10)
1926183312
>>> b=a
>>> id(b)
1926183312
>>> k=10
>>> id(k)
1926183312
>>> k=a
>>> b=100
>>> a=k
>>> id(100)
1926184752
>>> id(b)
1926184752
>>> pi=3.14
>>> peint(pi)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    peint(pi)
NameError: name 'peint' is not defined
>>> print(pi)
3.14
>>> PI=2.14
>>> pi=2.14
>>> pype(pi)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pype(pi)
NameError: name 'pype' is not defined
>>> type(pi)
<class 'float'>
>>> 
