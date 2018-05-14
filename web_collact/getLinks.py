import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 采集整个网站 1. 生成网站地图 2. 收集数据
# 避免一个页面被采集多次,链接去重是非常重要的

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']  # 这就是新页面
                print("新页面:" + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("/wiki")

print(pages)
