import requests
import time
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

# 设置要爬取的网页 URL
url = 'https://deep-forest-club.wikidot.com/major'

# 发送 HTTP 请求,获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
 # 使用 BeautifulSoup 解析网页内容
 soup = BeautifulSoup(response.text, 'html.parser')
 import requests
 from bs4 import BeautifulSoup

 def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

 links = get_all_links(url)

 print(links)
 # 使用 BeautifulSoup 解析网页内容
 soup = BeautifulSoup(response.text, 'html.parser')

 # 打印网页中的所有文本信息
 print(soup.prettify())
else:
 print(f'请求失败,状态码: {response.status_code}')

 # 添加进度条
 for i in tqdm(range(100)):
     # 模拟爬取操作
     time.sleep(0.1)

# 保存网页快照
if not os.path.exists('web_snapshots'):
 os.mkdir('web_snapshots')
with open(f'web_snapshots/web_snapshot_{time.time()}.html', 'w', encoding='utf-8') as f:
 f.write(str(soup))

print('网页快照已保存')

for i, url in enumerate(url):
  response = requests.get(url)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      with open(f'web_snapshots/web_snapshot_{i}_{time.time()}.html', 'w', encoding='utf-8') as f:
          f.write(str(soup))
      print(f'网页快照已保存: web_snapshot_{i}_{time.time()}.html')
  else:
      print(f'请求失败,状态码: {response.status_code}')