# 需求: 输出数字从0-100
"""
range(0, 101) 生成0-100的数值
for num in range(0, 101)
- num=0
- num=1
....
- num=100
"""
# range(start, end)指的是从start开始倒end-1结束
# range(num)指的是从0开始倒num-1结束
# range(start, end, step), 指的是从start开始倒end-1结束， 步长为step
for num in range(0, 101):
    print(num)