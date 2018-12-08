import urllib.request
import os
import json
from bs4 import BeautifulSoup

diziTipi = input('1 - Çukur \n2 - İstanbullu Gelin\nSeçiminiz: ')
os.system("clear")
while (diziTipi is not '1') & (diziTipi is not '2'):
	print("Olmadı pek, bi daha...\n")
	diziTipi = input('1 - Çukur \n2 - İstanbullu Gelin\nSeçiminiz: ')
	os.system("clear")
if diziTipi is '1':
	url = 'https://puhutv.com/cukur-detay'
if diziTipi is '2':
	url = 'https://puhutv.com/istanbullu-gelin-detay'
req = urllib.request.Request(
	url,
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	}
)
crawler = urllib.request.urlopen(req)
content = crawler.read()
parsed_html = BeautifulSoup(content, "html.parser")
bolumList = parsed_html.findAll("a", {"class": "episode-item seasons__episode-item"})
for index, bolum in enumerate(bolumList):
	finalUrl = 'https://puhutv.com/api/slug' + bolumList[int(index)].get('href')
	req = urllib.request.Request(
	finalUrl,
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	}
	)
	crawler = urllib.request.urlopen(req)
	content = crawler.read()
	jsonData = json.loads(content)
	bolumId = jsonData['data']['id']
	bolumTarih = jsonData['data']['created_at']
	print(index + 1, ' - ', bolum.find("div", {"class": "episode-item__title"}).string, ' - ', bolumTarih[:10], ' - ', bolumId)
bolumSecim = int(input('\nSeçiminiz: ')) - 1
os.system("clear")
finalUrl = 'https://puhutv.com/api/slug' + bolumList[int(bolumSecim)].get('href')
req = urllib.request.Request(
	finalUrl,
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	}
)
crawler = urllib.request.urlopen(req)
content = crawler.read()
jsonData = json.loads(content)
bolumId = jsonData['data']['id']
finalUrl2 = 'https://puhutv.com/api/assets/' + str(bolumId) + '/videos'
req = urllib.request.Request(
	finalUrl2,
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	}
)
crawler = urllib.request.urlopen(req)
content = crawler.read()
jsonData = json.loads(content)
test = jsonData['data']['videos'][4]['url']
while test.find('hmac=') is not -1:
	req = urllib.request.Request(
		finalUrl2,
		data=None,
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	crawler = urllib.request.urlopen(req)
	content = crawler.read()
	jsonData = json.loads(content)
	test = jsonData['data']['videos'][4]['url']
os.system('wget \"' + test + '\" -O \"/home/w3rtig0/Downloads/' + str(bolumId) + '.mp4\"')
