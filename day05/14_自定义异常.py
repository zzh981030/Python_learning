# 自定义的异常
class AgeError(ValueError):
    pass


age = int(input('age:'))
if 0<age<150:
    print(age)
else:
    # 抛出异常
    raise AgeError("年龄必须在0~150之间")