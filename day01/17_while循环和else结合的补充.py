"""
while 条件表达式:
    满足条件执行的内容
else:
    不满足条件执行的内容

for i in range(2):
    循环时执行的语句
else:
    没有for可以遍历的值时，执行的语句

"""
try_count = 1
while try_count <= 3:
    print(f"第{try_count}次开始尝试登录")
    try_count += 1
else:
    print("尝试登录次数大于3次")