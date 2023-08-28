import requests
import json
import re
import time
import datetime
import sys
from bs4 import BeautifulSoup
from tokenize import Token
from openpyxl import Workbook

# 디스이즈 게임 전체 뉴스 수집
def thisisgame_slcak_Share():
    print("디스이즈 게임")
    
    for i in range(1, 4):
        # print("현재 페이지 :", i)
        url = "https://www.thisisgame.com/webzine/news/nboard/263/?page={}".format(i)
        
        res = requests.get(url) # res 변수에 url 담기
        res.raise_for_status # 접속이 문제 없는지 확인
        soup = BeautifulSoup(res.text, "lxml") # BeautifulSoup 변수 생성
        
        news_list = soup.find_all("li", attrs={"class":re.compile("^list-one article")}) # 기사에 대한 모든 요소 정보를 써치
        # news_list = soup.find("div", attrs={"class":("news-list")}).find_all("li", limit=5) # 설정한 갯수만큼만 기사를 써치
        
        for news in news_list:
            news_name = news.find("div", attrs={"class":"subject"}).get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"class":"date"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("div", attrs={"class":"summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.thisisgame.com/webzine/news/nboard/263/" + news_link))
            print()
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기

# 인벤 게임 뉴스 수집
def inven_slack_Share():
    print()
    print("인벤")
    
    for i in range(1, 4):
        url = "https://www.inven.co.kr/webzine/news/?page={}".format(i)
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("td", attrs={"class":re.compile("^left name game-review-no-score")}) # 기사에 대한 모든 요소 정보를 써치
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        # print(news_list)
        
        for news in news_list:
            news_name = news.find("span", attrs={"class":"cols title"}).get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"info"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            news_day1 = news_day.strip() # 양측 공백 제거
            # lstrip() 좌측 공백 제거
            # rstrip() 우측 공백 제거
            
            print()
            print(f"뉴스날짜 : {news_day1}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format(news_link))
            print()
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기

# 루리웹 게임 뉴스 수집
def ruliweb_slack_Share():
    print()
    print("루리웹")
    
    for i in range(1, 4):
        url = "https://bbs.ruliweb.com/news/own?&page={}".format(i)
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("div", attrs={"class":re.compile("^row widget widget_thumbnail horizontal")}) # 기사에 대한 모든 요소 정보를 써치
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        
        for news in news_list:
            news_name = news.find("strong", attrs={"class":"title"}).get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"create_time"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format(news_link))
            print()
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기

# 경향게임스 뉴스 슬랙 공유
def khgames_slack_Share():
    print()
    print("경향게임스 뉴스")
    
    for i in range(1, 3):
        url = "https://www.khgames.co.kr/news/articleList.html?page={}&total=70684&sc_section_code=&sc_sub_section_code=S2N69&sc_serial_code=&sc_area=&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm".format(i)
        
        res = requests.get(url)
        res.raise_for_status
        soup = BeautifulSoup(res.text, "lxml")
        
        news_list = soup.find_all("div", attrs={"class":re.compile("^view-cont")}) # 기사에 대한 모든 요소 정보를 써치
        # news_list = soup.find("div", attrs={"class":"list"}).find_all("td", limit=1)
        # print(news_list)
        
        for news in news_list:
            news_name = news.find("a").get_text() # 써치된 모든 요소에서 기사 이름 써치
            news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
            news_day = news.find("span", attrs={"class":"byline"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            news_day2 = news_day.strip() # 양측 공백 제거
            
            print()
            print(f"뉴스날짜 : {news_day2}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.khgames.co.kr/" + news_link))
            # print(f"뉴스 내용 요약 : {news_summary}")
            # print("-"*100) # 줄긋기
            print()

if __name__ == "__main__":
    sys.stdout = open('뉴스.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
    thisisgame_slcak_Share()
    inven_slack_Share()
    ruliweb_slack_Share()
    khgames_slack_Share()
    sys.stdout.close() # 메모장으로 저장