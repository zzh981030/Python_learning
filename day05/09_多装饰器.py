from functools import  wraps
def is_login(f):
    # @wraps(f)
    def wrapper1(*args, **kwargs):
        print('is_login, 用户是否登录')
        result = f(*args, **kwargs)
        return  result
    return  wrapper1

def is_permission(f):
    # @wraps(f)
    def wrapper2(*args, **kwargs):
        print('is_permission, 用户是否有权限')
        result = f(*args, **kwargs)
        return  result
    return  wrapper2

# 规则: 执行装饰器内容是从上到下。 被装饰的顺序是从下到上。
@is_login           # show_hosts=is_login(wrapper2)   show_hosts=wrapper1
@is_permission      # show_hosts = is_permission(show_hosts) show_hosts=wrapper2
def show_hosts():
    print("显示所有的云主机")


"""
--: show_hosts()
1). wrapper1()
2). wrapper2()
3). show_hosts()
"""
show_hosts()
