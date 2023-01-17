from email import header
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    
    # 광교 제품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외합니다.")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    
    # 애플 제움 제외
    if "Apple" in name:
        print("<Apple 상품 제외 합니다>")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
    # 평점 출력
    rate = item.find("em", attrs={"class":"rating"}) 
    if rate:
        rate = rate.get_text()
    else:
        print("<평점 없는 상품 제외합니다.>")
        continue
    
    # 평점수 출력
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) 
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] #가로 제외
    else:
        print("<평점수 없는 상품 제외합니다.>")
        continue
    
    # 평점 4.5점 이상 리뷰수 100개 이상 제품만 조회
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)