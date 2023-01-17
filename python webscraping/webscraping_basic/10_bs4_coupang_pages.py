import requests
import re
from bs4 import BeautifulSoup

headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"}

for i in range(1, 6):
    print("현재 페이지 :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:
        
        # 광교 제품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("광고 상품 제외합니다.")
            continue # 제외 시켜주는 기능
        
        name = item.find("div", attrs={"class":"name"}).get_text() #제품명
        
        # 애플 제움 제외
        if "Apple" in name:
            # print("<Apple 상품 제외 합니다>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        # 평점 출력
        rate = item.find("em", attrs={"class":"rating"}) 
        if rate:
            rate = rate.get_text()
        else:
            # print("<평점 없는 상품 제외합니다.>")
            continue
        
        # 평점수 출력
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) 
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1] # [1:-1] 가로제외
        else:
            # print("<평점수 없는 상품 제외합니다.>")
            continue
        
        # 제품 링크 받아오기
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
        # 평점 4.5점 이상 리뷰수 100개 이상 제품만 조회
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄긋기