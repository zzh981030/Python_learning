"""
>>> s = "hello westos"
>>> s.find("llo")
2
>>> s.index("llo")
2
>>> s.find("xxx")
-1
>>> s.index("xxx")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> # find如果找到子串， 则返回子串开始的索引位置。 否则返回-1
>>> # index如果找到子串，则返回子串开始的索引位置。否则报错(抛出异常).
>>>
>>> s.count("xxx")
0
>>> s.count("l")
2
>>> s.count("o")
2
"""