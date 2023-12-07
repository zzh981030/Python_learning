from collections import  defaultdict

# 默认字典，设置默认value
d = defaultdict(int)
d['views'] += 1
d['transfer'] += 1
print(d)

d = defaultdict(list)
d['allow_users'].append('westos')
d['deny_users'].extend(['user1', 'user2'])
print(d)

d = defaultdict(set)
d['love_movies'].add("黑客帝国")
d['dislike_movies'].update({'前任3', '电影xxxx'})
print(d)


