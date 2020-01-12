Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=2.5
>>> num
2.5
>>> type(num)
<class 'float'>
>>> num=6+9i
SyntaxError: invalid syntax
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> a=5.6
>>> b=int(a)
>>> b=a3
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b=a3
NameError: name 'a3' is not defined
>>> b=a
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> k=float(b)
>>> type(k)
<class 'float'>
>>> k
5.0
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> num=6+9s
SyntaxError: invalid syntax
>>> b<k
True
>>> bool=b<k
>>> bool
True
>>> bool=b>k
>>> bool
False
>>> int(a)
5
>>> int(false)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(False)
0
>>> int(True)
1
>>> str='navin'
>>> st='a'
>>> type(st)
<class 'str'>
>>> vishal+str
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    vishal+str
NameError: name 'vishal' is not defined
>>> str
'navin'
>>> str+st
'navina'
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,21,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> d={'navin':'samsung,'rahul':'iphone','kiran':'oneplus'}
       
SyntaxError: invalid syntax
>>> d={'navin':'samsung','rahul':'iphone','kiran':'oneplus'}
       
>>> d
       
{'navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus'}
>>> d.keys()
       
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values()
       
dict_values(['samsung', 'iphone', 'oneplus'])
>>> d['rahul']
       
'iphone'
>>> d.get('navin')
       
'samsung'
>>> d.items()
       
dict_items([('navin', 'samsung'), ('rahul', 'iphone'), ('kiran', 'oneplus')])
>>> d.setdefault()
       
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d.setdefault()
TypeError: setdefault expected at least 1 arguments, got 0
>>> d.clear()
       
>>> d
       
{}
>>> d={'navin':'samsung','rahul':'iphone','kiran':'oneplus'}
       
>>> 
