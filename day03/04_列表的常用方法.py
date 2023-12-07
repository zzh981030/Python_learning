# 1. 增加
# 1-1). 追加
li = [1, 2, 3]
li.append(4)
print(li)
# 1-2). 在列表开头添加
li = [1, 2, 3]
li.insert(0, 'cat')
print(li)
# 1-2). 在索引2前面添加元素cat
li = [1, 2, 3]
li.insert(2, 'cat')
print(li)
# 1-3). 一次追加多个元素
li = [1, 2, 3]  # 添加4， 5， 6
li.extend([4, 5, 6])
print(li)

# 2. 修改: 通过索引和切片重新赋值的方式。
li = [1, 2, 3]
li[0] = 'cat'
li[-1] = 'westos'
print(li)
li = [1, 2, 3]
li[:2] = ['cat', 'westos']
print(li)

# 3. 查看: 通过索引和切片查看元素。 查看索引值和出现次数。
li = [1, 2, 3, 1, 1, 3]
print(li.count(1))   # 3
print(li.index(3))   # 2

# 4. 删除
# 4-1). 根据索引删除
li = [1, 2, 3]
# 将pop方法的结果存储到delete_num变量中。
delete_num = li.pop(-1)
print(li)
print("删除的元素是:", delete_num)

# 4-2). 根据value值删除
li = [1, 2, 3]
li.remove(1)
print(li)

# 4-3). 全部清空
li = [1, 2, 3]
li.clear()
print(li)


# 5. 其他操作
li = [18, 6, 99, 56]
li.reverse()  # 类似于li[::-1]
print(li)

# sort排序默认由小到大。 如果想由大到小排序，设置reverse=True
li.sort(reverse=True)
print(li)

li1 = li.copy()
print(id(li), id(li1))
print(li, li1)