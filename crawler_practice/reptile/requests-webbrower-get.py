import requests
import webbrowser
param={"wd":"莫烦python"}
r=requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)