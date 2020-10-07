import requests


def gethtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '_main_':
    url = ''
    print(gethtmltext(url))
