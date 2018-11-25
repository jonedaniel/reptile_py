s1 = "123?456"
print(s1.split("?"))


def urlGen():
    L = []
    base_str = "http://tieba.baidu.com/f?kw=&ie=utf-8&pn="
    for i in range(0, 1):
        L.append(base_str + (i * 50).__str__())
    return L

print(urlGen())