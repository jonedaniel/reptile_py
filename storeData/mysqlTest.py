from urllib.request import urlopen

from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', db='pydb', charset='utf8')
cur = conn.cursor()


def insertPageIfNotExists(url):
    cur.execute("select * from pages where url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("insert into pages (url) values (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    cur.execute("select * from links where fromPageId = %s and toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("insert into links(fromPageId, toPageId) values (%s,%s)", (int(fromPageId), int(toPageId)))
        conn.commit()


pages = set()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # 遇到一个新页面，加入集合并搜索里面的词条链接
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel + 1)


getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
