import requests
from bs4 import BeautifulSoup
import os
headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url='https://www.mzitu.com/all/'
start_html=requests.get(all_url,headers=headers)
# print(start_html.text)
Soup=BeautifulSoup(start_html.text,'lxml')
all_a=Soup.find('div',class_='all').find_all('a')
all_a.pop(0)
for a in all_a:
    title=a.get_text()
    path=str(title).strip() #去掉空格
    os.makedirs(os.path.join("D:\mzitu", path))
    #创建一个存放套图的文件夹
    os.chdir("D:\mzitu\\"+path)
    #切换到上面创建的文件夹
    href=a['href']
    #取出a标签的href标签
    html=requests.get(href,headers=headers)
    html_Soup=BeautifulSoup(html.text,'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        img_html=requests.get(page_url,headers=headers)
        img_Soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_Soup.find('div',class_='main-image').find('img')['src']
        # 查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
        name=img_url[-9:-4]
        #获取URL的倒数第四至第九位做图片的名字
        img=requests.get(img_url,headers=headers)
        f=open(name+'.jpg','ab')
        #写入多媒体文件必须b参数
        f.write(img.content)
        f.close()
