from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 获取imageLocation的url，并下载
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,"lxml")
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"data/logo.jpg")