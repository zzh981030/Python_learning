"""
with语句:
"""
# ****with语句
with open('doc/test.txt', 'w+') as f:
    f.write('hello world\n') # 写入文件
    f.seek(0, 0)      # ****: 移动指针到文件最开始
    print("当前指针的位置:", f.tell())
    f.seek(0, 2)      # 移动指针到文件末尾
    print("当前指针的位置:", f.tell())
    print(f.read())         # 读取文件内容


