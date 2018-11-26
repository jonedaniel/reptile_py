s1 = "123?456"
print(s1.split("?"))


def urlGen():
    L = []
    base_str = "http://tieba.baidu.com/f?kw=&ie=utf-8&pn="
    for i in range(0, 1):
        L.append(base_str + (i * 50).__str__())
    return L

# print(urlGen())

def cookieGen():
    cookieDict = {}
    cookie = "BAIDUID=DDF721070B9ACEF2F277E1E83038DAF4:FG=1; BIDUPSID=DDF721070B9ACEF2F277E1E83038DAF4; PSTM=1541930660; delPer=0; H_PS_PSSID=26522_1450_21095_27408; pgv_pvi=868277248; pgv_si=s20770816; ZD_ENTRY=google; TIEBA_USERTYPE=d7b21ecc53a321b49d75d8ac; TIEBAUID=cb23caae14130a0d384a57f1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1543241356; wise_device=0; bdshare_firstime=1543241365847; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1543241421"
    for item in cookie.split(';'):
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookieDict[key] = value
    return cookieDict

print(cookieGen())