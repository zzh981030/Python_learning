# python中input接收的是字符串， 如果接收整型数， 需要通过int转成整型数。
age = int(input("年龄:"))
# 需求: 如果年龄大于18岁， 输出成年， 否则输出未成年。
# 注意点: 冒号和缩进是python的语法规范。
if age > 18:
    print("成年")
else:
    print("未成年")