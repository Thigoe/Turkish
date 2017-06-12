import urllib.request
import time
import os
from bs4 import BeautifulSoup

while True:
	try:
		kargoTipi = input('1 - MNG \n2 - Yurtiçi\n3 - Sürat Kargo\nSeçiminiz: ')
		os.system("cls")
		kargoKodu = input('Kargo kodu: ')
		if kargoTipi is '1':
			while True:
				os.system("cls")
				url = 'http://service.mngkargo.com.tr/iactive/popup/kargotakip.asp?k=' + kargoKodu
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
				dolar = parsed_html.find("div", {"class": "takip-genel-sonhareketkurye1"})
				os.system("cls")
				print(dolar.string)
				time.sleep(30)
		if kargoTipi is '2':
			while True:
				os.system("cls")
				url = 'http://selfservis.yurticikargo.com/reports/SSWDocumentDetail.aspx?DocId=' + kargoKodu
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
				dolar = parsed_html.findAll("table", {"class": "tableForm"})
				durum = dolar[2].findAll("td")
				os.system("cls")
				print(durum[1].string)
				time.sleep(30)
		if kargoTipi is '3':
			while True:
				os.system("cls")
				url = 'http://www.suratkargo.com.tr/kargoweb/bireysel.aspx?action=Getir&no=' + kargoKodu
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
				dolar = parsed_html.find("table", id="ASPxRoundPanel1_gridviewparca")
				durum = dolar.findAll("td")
				os.system("cls")
				print(durum[6].string + ' - ' + durum[7].string)
				time.sleep(30)
		print('Try again.')
	except:
		print('Error, try again.')