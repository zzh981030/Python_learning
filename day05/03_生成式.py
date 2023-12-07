# 需求: 生成100个验证码(4个字母组成的验证码)
import  string
import  random
codes = []
for count in range(100):
    code = "".join(random.sample(string.ascii_letters, 4))
    codes.append(code)
print(codes)

# 列表生成式优化版
codes = ["".join(random.sample(string.ascii_letters, 4)) for i in range(100)]
print(codes)

# 需求: 找出1-100之间可以被3整除的数。
nums = []
for num in range(1, 101):
    if num % 3 == 0:
        nums.append(num)
print(nums)
# 优化版
nums = [num for num in range(1, 101) if num % 3 == 0]
print(nums)

# 集合生成式
result = {i**2 for i in range(10)}
print(result)

# 字典生成式
result = {i:i**2 for i in range(10)}
print(result)

