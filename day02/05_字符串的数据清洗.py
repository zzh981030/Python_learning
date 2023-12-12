"""
数据清洗的思路:
    lstrip: 删除字符串左边的空格(指广义的空格: \n, \t, ' ')
    rstrip: 删除字符串右边的空格(指广义的空格: \n, \t, ' ')
    strip: 删除字符串左边和右边的空格(指广义的空格: \n, \t, ' ')
    replace: 替换函数， 删除中间的空格， 将空格替换为空。replace(" ", )
    >>> " hello ".strip()
    'hello'
    >>> " hello ".lstrip()
    'hello '
    >>> " hello ".rstrip()
    ' hello'
    >>> " hel    lo ".replace(" ", "")
    'hello'

    """