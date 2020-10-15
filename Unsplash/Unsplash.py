import requests
import json

ids=[]
i=0
def get_Html(url):
    headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
    except:
        print('爬取图片失败！')
        return None

def get_ID(html):
    js=json.loads(html)
    for j in js:
        ids.append(j['id'])

def get_Image(url):
    global i
    for u in url:
        r=requests.get(u)
        f=open('img/'+ids[i]+'.jpg','ab')
        f.write(r.content)
        print('正在保存第{}张照片'.format(i+1))
        i+=1
    print('全部照片已保存完毕，共{}张照片'.format(i+1))

def main():
    urls=[]
    img_urls=[]
    for i in range(10):
        url='https://unsplash.com/napi/collections/1065976/photos?page='+str(i)+'&per_page=10&order_by=latest'
        urls.append(url)
    for url in urls:
        html=get_Html(url)
        get_ID(html)
    for id in ids:
        url_id='https://unsplash.com/photos/'+id+'/download'
        img_urls.append(url_id)
    get_Image(img_urls)

main()