import urllib.request
import urllib
import os
from bs4 import BeautifulSoup

if os.name == 'nt':
	def clear():
		os.system('cls')
else:
	def clear():
		os.system('clear')

clear()
while True:
	try:
		numara = input('Numara (05XX...): ')
		url = 'https://www.kimbunumara.com/searchz.php'
		values = {"token_1" : "1tDe0f7XLWhZHyaqGK104Cgn2296Aj8Ziay0OtY5",
				  "token_2" : "2tSe0f7XLWhZGyaqGK104Cen3696Aj8Ziay0OtY5",
				  "mainpage" : "false",
				  "numara" : numara,
				  "captcha" : "",
				  "iagree" : "true",
				  "action" : "lookup_number"}
		ahmet = urllib.parse.urlencode(values)
		req = urllib.request.Request(
			url,
			ahmet.encode(),
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
				'Content-type': 'application/x-www-form-urlencoded',
			}
		)
		crawler = urllib.request.urlopen(req)
		content = crawler.read()
		parsed_html = BeautifulSoup(content, "html.parser")
		checkSuccess = parsed_html.find("span", {"class": "resultClick_success"})
		if checkSuccess is not None:
			isimHam = parsed_html.find("td")
			isim = str(isimHam).replace("<td>", "")
			isim = str(isim).replace("</td>", "")
			clear()
			print(isim + '\n')
		else:
			clear()
			print('Not found.\n')
	except:
		print('Error, try again.\n')