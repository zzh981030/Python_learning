
# 类(Class)
class Cat:
    # 属性：一般是名词，eg: name, age, gender.....
    name = 'name'
    kind = 'kind'
    # 方法: 一般情况是动词, eg: create, delete, eating, run......
    def eat(self):
        print('cat like eating fish.....')

# 对象(Object):对类的实例化(具体化)
fentiao = Cat()
fentiao.name = 'tudou'
fentiao.kind = 'blue'
fentiao.eat()

print(Cat)  # <class '__main__.Cat'>
print(fentiao) # <__main__.Cat object at 0x00E9FD70>