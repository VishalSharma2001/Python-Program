Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup=(24,36,14,25)
>>> tup
(24, 36, 14, 25)
>>> vis=(24,36,14,25)
>>> tup
(24, 36, 14, 25)
>>> vis
(24, 36, 14, 25)
>>> tup[1]
36
>>> tup.count(24)
1
>>> s={22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[2]
TypeError: 'set' object does not support indexing
>>> 
