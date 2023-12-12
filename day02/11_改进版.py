"""
 设计一个程序，用来实现帮助小学生进行算术运算练习，
 它具有以下功能：
 提供基本算术运算(加减乘)的题目，每道题中的操作数是随机产生的，
 练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确
 并显示出相应的信息。最后显示正确率。

1+2=?
3*6=?
"""
import random

count = 10
right_count = 0
for i in range(count):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol = random.choice(["+", "-", "*"])#随机选择加减乘符号
    result = eval(f"{num1}{symbol}{num2}")#计算结果
    question = f"{num1} {symbol} {num2} = ?"#打印出问题
    print(question)
    user_answer = int(input("Answer:"))
    if user_answer == result:
        print("Right")
        right_count += 1
    else:
        print("Error")
print("Right percent: %.2f%%" %(right_count/count*100))

    
