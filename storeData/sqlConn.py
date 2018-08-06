import pymysql
conn = pymysql.connect(host="127.0.0.1",user='root',passwd="admin",db="new-tech-learn",charset="utf8")
cur = conn.cursor()

cur.execute("select * from my_order")
result = cur.fetchall()
print(result.__len__())
for row in result:
    print(row)
cur.close()
conn.close()