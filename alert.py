from urllib.request import urlopen
from bs4 import BeautifulSoup

from ssl_sending import sendMail

search = {}
search['merge_point'] = ['머지포인트', '머지 포인트']

url = {}
url['gmarket'] = {}
url['gmarket']['happy_money'] = 'https://browse.gmarket.co.kr/search?keyword=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88+5%EB%A7%8C%EC%9B%90'
url['gmarket']['book_and_life'] = 'https://browse.gmarket.co.kr/search?keyword=%EB%B6%81%EC%95%A4%EB%9D%BC%EC%9D%B4%ED%94%84+5%EB%A7%8C%EC%9B%90'
url['gmarket']['merge_point'] = 'https://browse.gmarket.co.kr/search?keyword=%EB%A8%B8%EC%A7%80%ED%8F%AC%EC%9D%B8%ED%8A%B8'

url['auction'] = {}
url['auction']['happy_money'] = 'http://browse.auction.co.kr/search?keyword=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88+5%EB%A7%8C%EC%9B%90&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88+5%EB%A7%8C%EC%9B%90&acode=SRP_SU_0100&arraycategory=&encKeyword=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88+5%EB%A7%8C%EC%9B%90'
url['auction']['book_and_life'] = 'https://browse.auction.co.kr/search?keyword=%EB%B6%81%EC%95%A4%EB%9D%BC%EC%9D%B4%ED%94%84+5%EB%A7%8C%EC%9B%90&itemno=&nickname=&encKeyword=%25EB%25B6%2581%25EC%2595%25A4%25EB%259D%25BC%25EC%259D%25B4%25ED%2594%2584%25205%25EB%25A7%258C%25EC%259B%2590&arraycategory=&frm=&dom=auction&isSuggestion=No&retry='
url['auction']['merge_point'] = 'http://browse.auction.co.kr/search?keyword=%EB%A8%B8%EC%A7%80%ED%8F%AC%EC%9D%B8%ED%8A%B8&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EB%A8%B8%EC%A7%80%ED%8F%AC%EC%9D%B8%ED%8A%B8&acode=SRP_SU_0100&arraycategory=&encKeyword=%EB%A8%B8%EC%A7%80%ED%8F%AC%EC%9D%B8%ED%8A%B8'

url['eleven'] = {}
url['eleven']['happy_money'] = 'https://search.11st.co.kr/Search.tmall?kwd=%25ED%2595%25B4%25ED%2594%25BC%25EB%25A8%25B8%25EB%258B%2588%25205%25EB%25A7%258C%25EC%259B%2590'
url['eleven']['book_and_life'] = 'https://search.11st.co.kr/Search.tmall?kwd=%25EB%25B6%2581%25EC%2595%25A4%25EB%259D%25BC%25EC%259D%25B4%25ED%2594%2584%25205%25EB%25A7%258C%25EC%259B%2590'
url['eleven']['merge_point'] = 'https://search.11st.co.kr/Search.tmall?kwd=%25EB%25A8%25B8%25EC%25A7%2580%25ED%258F%25AC%25EC%259D%25B8%25ED%258A%25B8'

url['wemake'] = {}
url['wemake']['happy_money'] = 'https://search.wemakeprice.com/search?search_cate=top&keyword=%ED%95%B4%ED%94%BC%EB%A8%B8%EB%8B%88%205%EB%A7%8C%EC%9B%90&isRec=1&_service=5&_type=3'
url['wemake']['book_and_life'] = 'https://search.wemakeprice.com/search?search_cate=top&keyword=%EB%B6%81%EC%95%A4%EB%9D%BC%EC%9D%B4%ED%94%84%205%EB%A7%8C%EC%9B%90&isRec=1&_service=5&_type=3'
url['wemake']['merge_point'] = 'https://search.wemakeprice.com/search?search_cate=top&keyword=%EB%A8%B8%EC%A7%80%ED%8F%AC%EC%9D%B8%ED%8A%B8&isRec=1&_service=5&_type=3'


alert_str = ''


def send(text):
	sendMail('louis.tw.kim@gmail.com', ['louis.tw.kim@gmail.com', 'properitas95@gmail.com'], text)

def alert(market_name, content, rate):
	global alert_str
	alert_str += f'{market_name}에서 {content} 상품권 {rate} 할인 중 입니다.\n'

def gmarket_crawler(content):
	market = 'gmarket'

	html = urlopen(url[market][content]) 

	bsObject = BeautifulSoup(html,"html.parser")

	# Existance Checker -------------------------------------
	if content in search.keys():
		is_here = False
		
		for div in bsObject.find_all('a'):
			cls = div.get('class')
			if cls is None:
				continue
	
			if 'link__item' in cls:
				for k, v in search['content'].items():
					if v in div.text:
						is_here = True
						break
		if is_here:
			alert(market, content, '판매')
	# Rate Checker -------------------------------------
	else:
		for div in bsObject.find_all('div'):
			cls = div.get('class')
			if cls is None:
				continue

			if 'box__discount' in cls:
				div_str = div.text.split('text__value\">')[0]
				div_str = div_str.split('할인률')[1]
				div_str = div_str.split('%')[0]
				div_int = int(div_str)
				if div_int > 7:
					alert(market, content, str(div_int) + '%')
				break



def auction_crawler(content):
	market = 'auction'

	html = urlopen(url[market][content]) 

	bsObject = BeautifulSoup(html, "html.parser") 
	
	# Existance Checker -------------------------------------
	if content in search.keys():
		is_here = False
		
		for div in bsObject.find_all('strong'):
			cls = div.get('class')
			if cls is None:
				continue

			if 'text--title' in cls:
				for k, v in search['content'].items():
					if v in div.text:
						is_here = True
						break
		if is_here:
			alert(market, content, '판매')
	
	# Rate Checker -------------------------------------
	else:
		for div in bsObject.find_all('strong'):
			cls = div.get('class')
			if cls is None:
				continue
	
			if 'text--discount' in cls:
				div_int = int(div.text)
				if div_int > 7:
					alert(market, content, str(div_int) + '%' )
				break


def eleven_crawler(content):
	market = 'eleven'

	html = urlopen(url[market][content]) 

	bsObject = BeautifulSoup(html, "html.parser")
	
	# Existance Checker -------------------------------------
	if content in search.keys():
		is_here = False
		
		for div in bsObject.find_all('div'):
			cls = div.get('class')
			if cls is None:
				continue
	
			if 'c_prd_name_row_1' in cls:
				for k, v in search['content'].items():
					if v in div.text:
						is_here = True
						break
		
		if is_here:
			alert(market, content, '판매')

	# Rate Checker -------------------------------------
	else:
		for div in bsObject.find_all('div'):
			div_str = str(div)
			if 'pricePrefix\":\"최저가' in div_str:
				div_str = div_str.split('\"finalPrc\":\"')[1]
				div_str = div_str.split('\",\"')[0]
				div_str = div_str.replace(',','')
				div_int = int(div_str)
				if div_int < 46500:
					alert(market, content, div_int)
				break





def wemake_crawler(content):
	market = 'wemake'

	html = urlopen(url[market][content]) 

	bsObject = BeautifulSoup(html, "html.parser", from_encoding="iso-8859-1") 
	print('here')

	# Existance Checker -------------------------------------
	if content in search.keys():
		print('no')
		is_here = False
		
		for div in bsObject.find_all('a'):
			cls = div.get('class')
			if cls is None:
				continue
	
			if 'link__item' in cls:
				for k, v in search['content'].items():
					if v in div.text:
						is_here = True
						break
		if is_here:
			alert(market, content, '판매')
	# Rate Checker -------------------------------------
	else:
		print(bsObject.encode('cp949'))
		for div in bsObject.find_all('div'):
			print('*'*100)
			print(div)
			cls = div.get('class')
			if cls is None:
				continue
			print(cls)

			print(div.text.decode('iso-8859-1'))

			if 'price_info' in cls:
				div_str = div.text.split('\=sale\">')[0]
				div_str = div_str.split('%')[1]
				div_int = int(div_str)
				print(div_int)
				if div_int > 7:
					alert(market, content, str(div_int) + '%')
				break





def main():
	global alert_str

	gmarket_crawler('happy_money')
	gmarket_crawler('book_and_life')
	gmarket_crawler('merge_point')
	
	auction_crawler('happy_money')
	auction_crawler('book_and_life')
	auction_crawler('merge_point')

	eleven_crawler('happy_money')
	eleven_crawler('book_and_life')
	eleven_crawler('merge_point')

	'''
	wemake_crawler('happy_money')
	wemake_crawler('book_and_life')
	wemake_crawler('merge_point')
	'''

	print(alert_str)
	if alert_str:
		send(alert_str)


if __name__ == '__main__':
	main()
