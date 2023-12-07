"""
异常处理机制:
    else:没有异常时，执行的内容
    finally： 总会执行的内容
"""
try:
    a = 1
    print(b)
except NameError as e:
    print('0-name error')
except KeyError:
    print('4-key error')
except Exception as e:
    print('1-exception')
else:
    print('2-no error')
finally:
    print('3-run code')