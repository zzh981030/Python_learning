# s = input('输入字符串:')
s = "westos"
result = "回文字符串" if s == s[::-1] else "不是回文字符串"
# print(s + "是" + result)
print(f"{s} 是 {result}")
print(s[-1])  # s
print(s[:-1])  # westo
print(s[::-1])  # sotsew
