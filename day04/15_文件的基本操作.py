# 1. 打开文件
"""
mode:
    r: 只能读文件
    w: 只能写入(清空文件内容)
    a+: 读写(文件追加写入内容)
"""
f = open('doc/hello.txt',mode='a+')
# 2. 文件读写操作
f.write('java\n')
# 3. 关闭文件
f.close()