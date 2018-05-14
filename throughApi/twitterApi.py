import json

from twitter import *

t = Twitter(auth=OAuth("783989194800574464-hK3zxWjlR640B4Kr2vte0x8dVn8s922","NeX6JaghArdrxSZvffv3CybPVyh4hNCI0Yy3A2weSvlga","tzExx5mGIeaABvGEwrQR5xIqR","t9oM58aAf5fywkNKvnVJnuZXFvNPkwX8Kj5HTBCKrxbLJkTguG"))

# 获取一个包含#python标签的推文json列表
# pythonTweets = t.search.tweets(q="#python")
# print(pythonTweets)

# 使用api发一篇推文

# statusUpdate = t.statuses.update(status='hello,world')
# print(statusUpdate)

# 获取推文，设置推文数量来限制条数
pythonStatuses = t.statuses.user_timeline(screen_name='trump',count=5)
print(pythonStatuses)

# Twitter Api 文档： https://github.com/sixohsix/twitter