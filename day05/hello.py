"""
hello 模块的说明文档
"""
digits = '012345679'

#__all__当用户使用from module import * 时，需要导入的内容、
__all__ = ['digits']

def login():
    print('login...')

#当模块内部执行时，需要执行的代码。 当模块被导入，则不执行
if __name__ == '__main__':
    print(__name__)
    # 当模块内部执行__name__的值为__main__.
    # 当模块被导入时，__name__的值为hello(模块名)