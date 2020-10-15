import urllib.request
import urllib.parse
import socket
import urllib.error
# data=bytes(urllib.parse.urlencode({'word','hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://baidu.com',data=data)
# response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())
# print(type(response))
# print(response.read().decode('utf-8'))
# print(response.getheaders())
# print(response.status)

try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
