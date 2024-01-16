import time, win32con, win32api, win32gui
import sys
import requests
import re
import time
import datetime
import sys
from bs4 import BeautifulSoup
from tokenize import Token

# 당일 날짜 구하기
def day():
    now = datetime.datetime.now() # 현재 날짜 구하기
    yesterday_date = now.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
    str2 = yesterday_date + ' 게임 뉴스 입니다.'
    print(str2)
    print()

# 디스이즈 게임 전체 뉴스 수집
def thisisgame_slack_Share():
    print("[디스이즈 게임]")
    
    for i in range(1):
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
            # news_day = news.find("span", attrs={"class":"date"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("div", attrs={"class":"summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            print()
            # print(f"뉴스날짜 : {news_day}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.thisisgame.com/webzine/news/nboard/263/" + news_link))
            print()
            
# 인벤 게임 뉴스 수집
def inven_slack_Share():
    print()
    print("[인벤]")
    
    for i in range(1):
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
            # news_day = news.find("span", attrs={"info"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
            # news_summary = news.find("span", attrs={"class":"cols summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치
            
            # news_day1 = news_day.strip() # 양측 공백 제거
            # lstrip() 좌측 공백 제거
            # rstrip() 우측 공백 제거

            print()
            # print(f"뉴스날짜 : {news_day1}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format(news_link))
            print()

# 경향게임스 뉴스 슬랙 공유
def khgames_slack_Share():
    print()
    print("[경향게임스 뉴스]")
    
    for i in range(1):
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
            
            # news_day2 = news_day.strip() # 양측 공백 제거
            
            print()
            # print(f"뉴스날짜 : {news_day2}")
            print(f"뉴스제목 : {news_name}")
            print("뉴스링크 : {}".format("https://www.khgames.co.kr/" + news_link))
            print()

# 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = '너울방'

# 팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)
    
# 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    
# 채팅방 열기
def open_chatroom(chatroom_name):
    # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1) # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)

def main():
    open_chatroom(kakao_opentalk_name) # 채팅방 열기
    
    file = open(r'C:\Users\rkfne\OneDrive\바탕 화면\Pythonbot\뉴스.txt', 'r', encoding="utf-8-sig")
    
    while True: # 모든 줄 출력을 위해 while을 사용
        lines = file.read()
        if not lines : break
        text = f"{lines}"

    kakao_sendtext(kakao_opentalk_name, text) # 메시지 전송

if __name__ == '__main__':
    sys.stdout = open('뉴스.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
    day()
    thisisgame_slack_Share()
    inven_slack_Share()
    khgames_slack_Share()
    sys.stdout.close() # 메모장으로 저장
    main()