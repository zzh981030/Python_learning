"""
补充pycharm快速复制一行的快捷键: ctrl + d
需求: 分数score
    1). 90=<score<=100, grade=A
    2). 80=<score<90, grade=B
    3). score<80, grade=C
"""
score = int(input('成绩:'))
if 90<=score<=100:
    print("等级是A")
elif 80<=score<90:   # elif 满足第二个条件做什么操作
    print("等级是B")
else:
    print("等级是C")