"""
技能需求:
    1. 文件操作
    2. 字符串的分割操作
    3. 字典操作
功能需求:词频统计
    1. 读取song.txt文件   with open(filename) as f: content=f.read()
    2. 分析文件中的每一个单词，统计每个单词出现的次数。{"hello":2, "python":1, "java":1}
    - 分析文件中的每一个单词
    content = "hello python hello java"
    words = content.split()
    - 统计每个单词出现的次数- {"hello":2, "python":1, "java":1}
    # words = ['hello', 'python', 'hello', 'java']
    3. 获取出现次数最多的5个单词

"""
# 1. 加载文件中所有的单词
with open('doc/song.txt') as f:
    words = f.read().split()
# 2. 统计
from collections import  Counter
counter = Counter(words)
result = counter.most_common(5)
print(result)
 
# # 2. 统计
# result = {}
# for word in words:
#     if word in result:
#         # result[word] = result[word] + 1
#         result[word] += 1
#     else:
#         result[word] = 1
#
# # *小拓展: 友好打印信息
# import pprint
# pprint.pprint(result)
#


