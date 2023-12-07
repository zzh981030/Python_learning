# startswith
url = 'http://www.baidu.com'
if url.startswith('http'):
    # 具体实现爬虫，感兴趣的话可以看request模块。
    print(f'{url}是一个正确的网址，可以爬取网站的代码')

# endswith:
# 常用的场景: 判断文件的类型
filename = 'hello.png'
if filename.endswith('.png'):
    print(f'{filename} 是图片文件')
elif filename.endswith('mp3'):
    print(f'{filename}是音乐文件')
else:
    print(f'{filename}是未知文件')

# pycharm常用的快捷键:
#   如何查看方法的源代码和解释说明: ctrl键按住，
#   鼠标移动到你想要查看方法的位置，点击即可进入源码及方法说明