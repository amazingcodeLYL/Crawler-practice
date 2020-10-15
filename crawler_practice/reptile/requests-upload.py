import requests
file={'uploadFile':open('C:/Users/acer/PycharmProjects/untitled/1.jpg','rb')}
r=requests.post('http://pythonscraping.com/files/processing2.php',files=file)
print(r.text)