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
import colorama #配置字体颜色的包

count = 10
right_count = 0
for i in range(count):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol = random.choice(["+", "-", "*"])
    if symbol == "+":
        result = num1 + num2
    elif symbol == "-":
        result = num1 - num2
    elif symbol == "*":
        result = num1 * num2
    question = f"{num1} {symbol} {num2} = ?"
    print(question)
    user_answer = int(input("Answer:"))
    if user_answer == result:
        print(colorama.Fore.GREEN+"Right"+colorama.Style.RESET_ALL)#配置字体颜色+Right+清除字体样式
        right_count += 1
    else:
        print(colorama.Fore.RED + "Error" + colorama.Style.RESET_ALL)#配置字体颜色+Error+清除字体样式
print("Right percent: %.2f%%" %(right_count/count*100))


