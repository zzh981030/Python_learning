'''
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，
只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。
然后再把这些数从大到小排序，按照排好的顺序去找同学做调查。
请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
'''

import random
import pprint

n = int(input("输入n:"))
s = set()
for i in range(n):
    s.add(random.randint(1, 1000))#每次生成一个随机数并添加到集合s中，如果有重复则会去重
pprint.pprint(sorted(s, reverse=True))#对上一步产生的 去重过后的集合s进行从大到小排序
print(len(s))