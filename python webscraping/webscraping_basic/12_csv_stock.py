import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액1-200.csv"
f = open(filename, "a", encoding="utf-8-sig", newline="") # newline을 하는 이유는 불필요한 엔터를 하지않기 위해 사용
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # 타이틀 널기
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page)) # str(page)는 페이지를 늘려주는 기능
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    date_rosws = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in date_rosws:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)