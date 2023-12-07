import  json

# 1. 将python对象编码成json字符串
users = {'name':'westos', "age":18, 'city':'西安'}
json_str = json.dumps(users)
with open('doc/hello.json', 'w') as f:
    # ensure_ascii=False:中文可以成功存储
    # indent=4： 缩进为4个空格
    json.dump(users, f, ensure_ascii=False, indent=4)
    print("存储成功")
print(json_str, type(json_str))

# 2. 将json字符串解码成python对象
with open('doc/hello.json') as f:
    python_obj = json.load(f)
    print(python_obj, type(python_obj))
