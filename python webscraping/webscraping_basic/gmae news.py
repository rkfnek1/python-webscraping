from asyncore import loop
from hashlib import new
from attr import attr
import requests # HTTP 라이브러리
import re # 정규식 라이브러리
import sys
import datetime
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup # HTML정보로 부터 원하는 데이터를 가져오기 쉽게, 비슷한 분류의 데이터별로 나누어주는 라이브러리
# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# sys.stdout = open('헤드라인.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈

# 디즈이즈 게임 전체뉴스를 불러오는 코드의 함수
def thisisgame():
    for i in range(1, 2):
        # print("현재 페이지 :", i)
        url = "https://www.thisisgame.com/webzine/news/nboard/263/?page={}".format(i)
        
        res = requests.get(url) # res 변수에 url 담기
        res.raise_for_status # 접속이 문제 없는지 확인
        soup = BeautifulSoup(res.text, "lxml") # BeautifulSoup 변수 생성
        
        # news_list = soup.find_all("div", attrs={"class":re.compile("^article-list-part")})
        news_list = soup.find_all("li", attrs={"class":re.compile("^list-one article")})
        
        print("디스이즈 게임 전체뉴스")
        
        for news in news_list:
            news_name = news.find("div", attrs={"class":"subject"}).get_text()
            news_link = news.find("a")["href"]
            news_day = news.find("span", attrs={"class":"date"}).get_text()
            news_summary = news.find("div", attrs={"class":"summary"}).get_text()
            
            print()
            print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.thisisgame.com/webzine/news/nboard/263/" + news_link))
            print(f"뉴스 내용 요약 : {news_summary}")
            print("-"*100) # 줄긋기
            
        # sys.stdout.close() # 메모장으로 저장



now = datetime.datetime.now()
# today = now - datetime.timedelta(days=1)
today_date = now.strftime('%Y.%m.%d')

# # browser = webdriver.Chrome() # "./chromedriver.exe" 크롬 실행
# browser = webdriver.Edge("./msedgedriver.exe") # "./msedgedriver.exe" 마이크로 소프트 엣지 브라우저 실행

def thisisgame_1():
    for i in range(1, 2):
        # print("현재 페이지 :", i)
        url = "https://www.thisisgame.com/webzine/news/nboard/263/?page={}".format(i)
        
        res = requests.get(url) # res 변수에 url 담기
        res.raise_for_status # 접속이 문제 없는지 확인
        soup = BeautifulSoup(res.text, "lxml") # BeautifulSoup 변수 생성
        
        # news_list = soup.find_all("div", attrs={"class":re.compile("^article-list-part")})
        news_list = soup.find("div", attrs={"class":("news-list")}).find_all("li", limit=3)
        # print(news_list)
        
        print("디스이즈 게임 전체뉴스")
        
        for news in news_list:
            news_name = news.find("div", attrs={"class":"subject"}).get_text()
            news_link = news.find("a")["href"]
            news_day = news.find("span", attrs={"class":"date"}).get_text()
            news_summary = news.find("div", attrs={"class":"summary"}).get_text()
                
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.thisisgame.com/webzine/news/nboard/263/" + news_link))
            print(f"뉴스날짜 : {news_day}")

# 인벤 게임 뉴스 슬랙 공유       
def inven_slack_Share():
    # Token = 'xoxb-2632799608037-3400993070864-lxhhYJQB4QdynU1KELxiJ734' # 회사 슬랙 봇 토큰
    Token2 = 'xoxb-3335002115717-3343261330306-CRxaElDQkAaN9MaOZDwHnl0c' # 개인 슬랙 봇 토큰
    str3 = '' 
    
    print()
    print("인벤 뉴스")
    
    for i in range(1, 4):
        url = "https://www.inven.co.kr/webzine/news/?page={}".format(i)
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("td", attrs={"class":re.compile("^left name game-review-no-score")})
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        # print(news_list)
        
        for news in news_list:
            news_name = news.find("span", attrs={"class":"cols title"}).get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"info"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format(news_link))
            # print(f"뉴스 내용 요약 : {news_summary}")
            print("-"*100) # 줄긋기
                       
            # attach_dict = {
            #     'color' : "#ff0000",
            #     'author_name' : "인벤 게임 뉴스",
            #     'title' : f"뉴스제목 : {news_name}",
            #     'title_link' : "https://www.thisisgame.com/webzine/news/nboard/263/" + news_link,
            #     'text' : f"뉴스날짜 : {news_day}",
            #     'fields': [
            #         {
            #             'title' : f"뉴스요약 : {news_summary}"
            #         }
            #     ]
            # } # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력

            # attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
            
            # notice_message(Token2, "#bot", str3, attach_list)
            
# 경향게임스 뉴스 슬랙 공유       
def khgames_slack_Share():
    # Token = 'xoxb-2632799608037-3400993070864-lxhhYJQB4QdynU1KELxiJ734' # 회사 슬랙 봇 토큰
    Token2 = 'xoxb-3335002115717-3343261330306-CRxaElDQkAaN9MaOZDwHnl0c' # 개인 슬랙 봇 토큰
    str3 = '' 
    
    print()
    print("경향게임스 뉴스")
    
    for i in range(1, 2):
        url = "https://www.khgames.co.kr/news/articleList.html?page={}&total=70684&sc_section_code=&sc_sub_section_code=S2N69&sc_serial_code=&sc_area=&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm".format(i)
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("div", attrs={"class":re.compile("^view-cont")})
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        # print(news_list)
        
        for news in news_list:
            news_name = news.find("a").get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"class":"byline"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.khgames.co.kr/" + news_link))
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기
            print()
            
# 경향게임스 뉴스 슬랙 공유       
def mobileindex_slack_Share():
    print()
    print("")
    
    for i in range(1, 1):
        url = "https://www.mobileindex.com/mi-chart/weekly-rank/revenue"
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("span", attrs={"class":re.compile("^app-name")})
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        print(news_list)
        
        for news in news_list:
            news_name = news.find("span").get_text # 써치된 모든 요소에서 기사 이름 써치
            news_name2 = news.find_all("/html/body/div[2]/article/div/div[3]/section/table/tbody/tr[1]/td[2]/span/span/span[1]").get_text
        
            
            # news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            # news_day = news.find("span", attrs={"class":"byline"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            # print(f"뉴스날짜 : {news_day}")
            # print(f"뉴스제목 : {news_name}")
            # print("뉴스링크 : {}".format("https://www.khgames.co.kr/" + news_link))
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기
            print()
            

url = "https://www.mobileindex.com/mi-chart/weekly-rank/revenue"

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline을 하는 이유는 불필요한 엔터를 하지않기 위해 사용
writer = csv.writer(f)

title = "순위 | 앱명 | 순위 변동 | 마켓별 매출 순위".split("\t") # 타이틀 널기
writer.writerow(title)

for page in range(1, 1):
    res = requests.get(url + str(page)) # str(page)는 페이지를 늘려주는 기능
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
        
    date_rosws = soup.find("table", attrs={"class":"flake-ui table second small rect   bordered  "}).find("tbody").find_all("tr")
    print(date_rosws)
    for row in date_rosws:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 스킵
                continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)