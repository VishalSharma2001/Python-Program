Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=2
>>> y=3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/y
0.6666666666666666
>>> x=2
>>> x=x+2
>>> x
4
>>> x+=2
>>> x
6
>>> x*=3
>>> x
18
>>> a,b=5,6
>>> a
5
>>> b
6
>>> n=7
>>> n
7
>>> n=-n
>>> n
-7
>>> -n
7
>>> n
-7
>>> n
-7
>>> -n
7
>>> n=7
>>> a
5
>>> b
6
>>> a<b
True
>>> bool(a<b)
True
>>> bool(True)
True
>>> bool(1)
True
>>> a>b
False
>>> a==b
False
>>> a=6
>>> a==b
True
>>> a<=b
True
>>> a>=b
True
>>> a
6
>>> b
6
>>> b=7
>>> a=b
>>> bool(a=b)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    bool(a=b)
TypeError: bool() takes no keyword arguments
>>> a==b
True
>>> bool(a==b)
True
>>> a!=b
False
>>> a=b
>>> b=7
>>> a
7
>>> a=
SyntaxError: invalid syntax
>>> a=6
>>> a!=6
False
>>> a!=b
True
>>> a=5
>>> b=4
>>> a<8 and b<5
True
>>> a<8 and b<2
False
>>> a<8 or b<5
True
>>> x=Ture
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x=Ture
NameError: name 'Ture' is not defined
>>> x=True
>>> x
True
>>> not x
False
>>> x=not x
>>> x
False
>>> 
