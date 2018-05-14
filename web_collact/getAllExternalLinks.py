from urllib.request import urlopen

# 收集网站上发现的所有外链列表
from bs4 import BeautifulSoup

from reptile.web_collact.data_collact2 import splitAddress, getInternalLinks

allExtlinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl[0]))
    externalLinks = getAllExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtlinks:
            allExtlinks.add(link)
            print(link)
    for link in internalLinks:
        if link in allIntLinks:
            print("即将获取链接的url是:" + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("https://oreily.com")
