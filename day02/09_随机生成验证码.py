"""
>>> # 需求: 生成100个验证码， 每个验证码由2个数字和2个字母组成。
>>>
>>>
>>>
>>> import random
>>> random.choice("0123456789")
'6'
>>> random.choice("0123456789") + random.choice('0123456789')
'84'
>>> random.choice("0123456789") + random.choice('0123456789') + random.choice('abcdef')
'16b'
>>> import string
>>> string.digits
'0123456789'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> random.sample(string.ascii_letters, 4)
['z', 'N', 'u', 't']
>>> random.sample(string.ascii_letters, 4)
['c', 'q', 'X', 'f']
>>> random.sample(string.ascii_letters, 4)
['D', 'b', 'e', 'A']
>>> "".join(random.sample(string.ascii_letters, 4))
'aMUF'
>>> "".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4))
'95sGFj'
>>> "".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4))
'17TlIb'
>>> "".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4))
'50uvqM'
>>> "".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4))
'09MCDW'
>>> "".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4))
'83Wntf'
>>> for i in range(100):
...     print("".join(random.sample(string.digits, 2)) + "".join(random.sample(string.ascii_letters, 4)))
...
53SJbP
83dRcm
"""