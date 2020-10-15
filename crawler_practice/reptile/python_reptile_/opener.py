from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
proxy_handler=ProxyHandler({
    'http':'http://1.192.242.5:9999',
    'https':'https://1.192.241.115:9999'
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
