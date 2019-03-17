import requests
#伪装成chrome
hd = {'user-agent':'Chrome/10'}
d= requests.head('https://www.douban.com/',headers=hd)
print(d.status_code)
d.encoding=d.apparent_encoding
print(d.headers)