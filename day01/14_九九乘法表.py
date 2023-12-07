"""
i      j
1       1
2       1,2
3       1, 2, 3
...
9       1, 2, 3, ...9
"""
# 如何让print不换行呢? print('xxx', end=' ')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j*i}", end=' ')
    # i=1, i=2, i=3, 开始换行
    print()