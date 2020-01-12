Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name='telusko'
>>> name[-3]
's'
>>> nums=[25,12,36,95,14]

>>> nums
[25, 12, 36, 95, 14]
>>> nums[4]
14
>>> nums[-4]
12
>>> names=['vishal','navin','jones']
>>> names
['vishal', 'navin', 'jones']
>>> values=[9.5,vishal,25]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    values=[9.5,vishal,25]
NameError: name 'vishal' is not defined
>>> values=[9.5,'vishal',250]
>>> values
[9.5, 'vishal', 250]
>>> nums+names
[25, 12, 36, 95, 14, 'vishal', 'navin', 'jones']
>>> nums>names
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    nums>names
TypeError: '>' not supported between instances of 'int' and 'str'
>>> mil=[nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['vishal', 'navin', 'jones']]
>>> nums.append(50)
>>> nums
[25, 12, 36, 95, 14, 50]
>>> nums.insert(2,999*);
SyntaxError: invalid syntax
>>> nums.insert(2,999*)
SyntaxError: invalid syntax
>>> nums.insert(2,999)
>>> nums
[25, 12, 999, 36, 95, 14, 50]
>>> nums.remove(14)
>>> nums
[25, 12, 999, 36, 95, 50]
>>> nums.pop(5)
50
>>> nums.pop()
95
>>> del nums(2:)
SyntaxError: invalid syntax
>>> del nums[2:]
>>> nums
[25, 12]
>>> nums.extend([29,12,14,36])
>>> min(nums)
12
>>> max(nums)
36
>>> sum(names)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sum(names)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(nums)
128
>>> nums.sort()
>>> nuus
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    nuus
NameError: name 'nuus' is not defined
>>> nums
[12, 12, 14, 25, 29, 36]
>>> nums.pop(1)
12
>>> nums
[12, 14, 25, 29, 36]
>>> nums.count()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nums.count()
TypeError: count() takes exactly one argument (0 given)
>>> nums.count(2)
0
>>> nums.index()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    nums.index()
TypeError: index() takes at least 1 argument (0 given)
>>> nums.clear()
>>> nums
[]
>>> nums=[25,36,95,14,12,26]
>>> nums.remove(95,12,14)nums
SyntaxError: invalid syntax
>>> nums.remove(95,12,14)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    nums.remove(95,12,14)
TypeError: remove() takes exactly one argument (3 given)
>>> nums.pop(2,4,3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    nums.pop(2,4,3)
TypeError: pop() takes at most 1 argument (3 given)
>>> Traceback (most recent call last):
	
SyntaxError: invalid syntax
>>> 
s
