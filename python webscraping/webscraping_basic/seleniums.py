from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
import time
import pyautogui
import os
from bs4 import BeautifulSoup
import shutil
import requests
import openpyxl
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, 
QHBoxLayout, QGridLayout, QTextEdit, QLineEdit, QCheckBox, QRadioButton, QComboBox, QProgressBar, QSlider, QDial, QGroupBox, QMenu, QTabWidget, QCalendarWidget, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, QInputDialog, QFrame, QColorDialog,
QSizePolicy, QFontDialog, QMessageBox, QLCDNumber)
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime, QCoreApplication, QBasicTimer, pyqtSignal, QObject
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont, QPixmap, QColor
from PyQt5.QtWidgets import *
import sys

# username = "본인 아이디 입력" # 아이디
# userpw = "본인 패스워드 입력" # 패스워드
hashTag = "검색어" # 검색어
savename = "사진"
# N = 5 # 스크롤 몇번 내릴지 결정
# M = 31 # 이미지 몇개 다운로드 받을지 설정

# loginUrl = "https://www.instagram.com/" # 인스타그램 로그인 Url
# tagUrl = "https://www.instagram.com/explore/tags/" + hashTag + "/" # 해시태그
tagUrl = "https://www.instagram.com/explore/tags/"

# driver = wd.Chrome(executable_path = r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\chromedriver.exe")
# browser.maximize_window()
# driver.implicitly_wait(5)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label = QLabel("원하는 URL 입력", self) # URL 입력 라벨 출력
        label.move(30, 25) # 라벨 출력 위치 설정
        self.qle_1 = QLineEdit(self) # 한줄 문자열 위젯 생성
        self.qle_1.move(124, 20) # 위젯 출력 위치 설정
        self.qle_1.setText("")
        
        label = QLabel("검색할 해시태그 입력", self) # URL 입력 라벨 출력
        label.move(300, 25) # 라벨 출력 위치 설정
        self.qle_6 = QLineEdit(self) # 한줄 문자열 위젯 생성
        self.qle_6.move(423, 20) # 위젯 출력 위치 설정
        self.qle_6.setText("")
        
        label = QLabel("아이디 입력", self)
        label.move(30, 60)
        self.qle_2 = QLineEdit(self)
        self.qle_2.move(100, 55)  
        
        label = QLabel("비밀번호 입력", self)
        label.move(300, 60)
        self.qle_3 = QLineEdit(self)
        self.qle_3.setEchoMode(QLineEdit.Password) # 비밀번호 암호화 (*표시)
        self.qle_3.move(380, 55)
        self.qle_3.setText("")
        
        label = QLabel("스크롤 횟수", self)
        label.move(30, 98)
        self.qle_4 = QLineEdit(self)
        self.qle_4.move(100, 93)
        self.qle_4.setText("")
        
        label = QLabel("다운로드 개수", self)
        label.move(30, 127)
        self.qle_5 = QLineEdit(self)
        self.qle_5.move(113, 121)
        self.qle_5.setText("")
        
        # self.text_edit = QTextEdit(self) # 편집기 위젯 생성
        # self.text_edit.setGeometry(50, 100, 500, 200) # 편집기 위젯 위치 및 크기 설정
        # self.text_edit.setEnabled(False)
        
        btn1 = QPushButton(self) # 푸쉬 버튼 위젯 생성
        btn1.move(30, 320) # 버튼 출력 위치 설정
        btn1.setText("크롤링 시작") # 버튼에 "오픈 저장" 텍스트 노출
        btn1.clicked.connect(self.instra_crawling) # 버튼이 눌리면 btn1_clicked 함수 실행
        
        self.setWindowTitle("인스타그램 이미지 크롤링") # 윈도우창 타이틀 이름
        self.setGeometry(500, 500, 600, 400) # 윈도우창이 출력되는 위치 및 크기 설정
        self.show() # 윈도우창 보여주기

    def instra_crawling(self):
        # opts = Options()
        # opts.add_argument("headless")
        # driver = wd.Chrome(executable_path = r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\chromedriver.exe")
        driver = wd.Chrome(executable_path = r"./chromedriver.exe")
        # driver = wd.Edge(executable_path= r'./msedgedriver.exe')
        driver.implicitly_wait(5)
        
        inp = self.qle_1.text() # 한줄 문자열 위젯에 등록된 글씨를 텍스트로 저장해 inp 변수로 지정
        inp_2 = self.qle_2.text()
        inp_3 = self.qle_3.text()
        inp_6 = self.qle_6.text()
        inp_7 = tagUrl + inp_6
        inp_4 = int(self.qle_4.text())
        inp_5 = int(self.qle_5.text())
        
        try:
            res = requests.get(inp) # res 변수에 inp 변수 담기
            res.raise_for_status # 접속이 문제 없는지 확인
            driver.get(inp)
            time.sleep(4)
        except:
            res2 = requests.get(inp_7) # res 변수에 inp 변수 담기
            res2.raise_for_status # 접속이 문제 없는지 확인
            driver.get(inp_7)
            time.sleep(4)
        
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div[1]/a").click()
        time.sleep(2)
        
        # res_2 = requests.get(inp_2)
        driver.find_element_by_name("username").send_keys(inp_2) # 유저 아이디 입력
        time.sleep(1)
        # res_3 = requests.get(inp_3)
        driver.find_element_by_name("password").send_keys(inp_3) # 유저 비밀번호 입력
        
        pyautogui.press("enter") # 엔터키 누르기
        driver.implicitly_wait(5)
        
        try:
            driver.find_element_by_class_name("_ac8f").click()
            time.sleep(2)
        
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
            time.sleep(2)
        except:
            print("실행안됨")
        
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        
        imglist = []
        
        for i in range(0, inp_4):
            # insta = soup.select(".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
            insta = soup.select("._aabd._aa8k._aanf")
            # insta = soup.select("._ac7v._aang")
            
            for i in insta:
                print("https://www.instagram.com" + i.a["href"])
                # imgUrl = i.select_one(".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd").img["src"]
                imgUrl = i.select_one("._aagu").img["src"]
                imglist.append(imgUrl)
                imglist = list(set(imglist))
                html = driver.page_source
                soup = BeautifulSoup(html, "lxml")
                # insta = soup.select("._ac7v._aang")
                # insta = soup.select(".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
                insta = soup.select("._aabd._aa8k._aanf")
            
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(6)
            
        n = 0
        
        for i in range(0, inp_5):
            # print(n)
            image_url = imglist[n]
            resp = requests.get(image_url, stream=True)
            local_file = open(r"./Instagram_crawling/" + savename + str(n) + ".jpg", "wb")
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            
            n += 1
            del resp
        
        driver.close()

    # 인스타그램 페이지 이동
    # def login(self):
    #     inp = self.qle_1.text() # 한줄 문자열 위젯에 등록된 글씨를 텍스트로 저장해 inp 변수로 지정
        
    #     res = requests.get(inp) # res 변수에 inp 변수 담기
    #     res.raise_for_status # 접속이 문제 없는지 확인
    #     # soup = BeautifulSoup(res.text, "lxml")
    
    #     # driver.get("https://www.instagram.com/") # 인스타그램 로그인 페이지 접속
    #     # driver.get("https://www.instagram.com/hs_kim_95/") # 접속할 인스타그램 Url
    #     driver.get(inp)
    #     time.sleep(2)
        
    #     driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div[1]/a").click()
    #     time.sleep(2)
        
    #     driver.find_element_by_name("username").send_keys(username) # 유저 아이디 입력
    #     time.sleep(1)
    #     driver.find_element_by_name("password").send_keys(userpw) # 유저 비밀번호 입력
        
    #     pyautogui.press("enter") # 엔터키 누르기
    #     driver.implicitly_wait(5)
        
    #     try:
    #         driver.find_element_by_class_name("_ac8f").click()
    #         time.sleep(2)
        
    #         driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    #         time.sleep(2)
    #     except:
    #         print("실행안됨")

    # 이미지 저장
    # def img():
        # html = driver.page_source
        # soup = BeautifulSoup(html, "lxml")
        
        # imglist = []
        
        # for i in range(0, N):
        #     # insta = soup.select(".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
        #     insta = soup.select("._aabd._aa8k._aanf")
        #     # insta = soup.select("._ac7v._aang")
            
        #     for i in insta:
        #         print("https://www.instagram.com" + i.a["href"])
        #         # imgUrl = i.select_one(".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd").img["src"]
        #         imgUrl = i.select_one("._aagu").img["src"]
        #         imglist.append(imgUrl)
        #         imglist = list(set(imglist))
        #         html = driver.page_source
        #         soup = BeautifulSoup(html, "lxml")
        #         # insta = soup.select("._ac7v._aang")
        #         # insta = soup.select(".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
        #         insta = soup.select("._aabd._aa8k._aanf")
            
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(6)
            
        # n = 0
        
        # for i in range(0, M):
        #     # print(n)
        #     image_url = imglist[n]
        #     resp = requests.get(image_url, stream=True)
        #     local_file = open(r"./skirr/" + savename + str(n) + ".jpg", "wb")
        #     resp.raw.decode_content = True
        #     shutil.copyfileobj(resp.raw, local_file)
            
        #     n += 1
        #     del resp
        
        # driver.close()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())
