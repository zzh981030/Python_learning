"""
Leetcode 二叉树的题目, 大部分需要用递归。
需求: 求n的阶乘。 n!=n*(n-1)*(n-2)*......1
# 方法1: for循环
res = 1
n = 3  # 3!=3*2*1=1*2*3=6
for i in range(1,n+1):
    res = res * i # res=1*1*2*3
print(res)
# 2. 方法2: 递归
- 递归的规律
- 退出递归的条件
3! = 3 * 2! = 3 * 2 * 1! = 6
n! = n*(n-1)!
"""
def f(n):
    """计算阶乘"""
    if n == 1:
        return  1
    return n * f(n-1)
print(f(5))

