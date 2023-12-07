"""
给定一个整形数组， 将数组中所有的0移动到末尾， 非0项保持不变；
    - 输入: 数组的记录;0 7 0 2
    - 输出: 调整后数组的内容; 7 2 0 0

0 7 0 2  -before sort
=====
1 0 1 0  - rule: (1 if num==0 else 0)
0 0 1 1
=====
7 2 0 0  -after sort
"""
nums = [0, 7, 0, 2]
nums.sort(key=lambda num: 1 if num==0 else 0)
print(nums)


# 需求: 将所有的偶数排前面，所有的奇数排后面。
nums = [0,7,0,2]
nums.sort(key=lambda num: 0 if num%2==0 else 1)
print(nums)