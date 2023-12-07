age = int(input('age:'))
if 0<age<150:
    print(age)
else:
    # 抛出异常
    raise ValueError("年龄必须在0~150之间")