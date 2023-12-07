# 需求: 输出数字从0-100
"""
count=0, while 0<=100, print(0)  count+=1
count=1, while 1<=100, print(1) count+=1
....
count=99 while 99 <=100, print(99) count+=1
count=100 while 100 <=100, print(100) count+=1
count=101 while 101 <=100(x)
"""
#count = 0
count = int(input())
while count <= 100:
    print(count) # 0
    # count = count + 1
    count += 1