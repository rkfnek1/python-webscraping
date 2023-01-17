import requests
import openpyxl
import json
import re
import time
import datetime
import sys
import csv
from bs4 import BeautifulSoup

wb = openpyxl.Workbook() # 새로운 엑셀 열기

sheet = wb.active # 현재 Active Sheet 얻기

# sheet.append(["제품명", "gpu chip", "Released", "Bus", "Memory", "GPU clock", "Memory clock", "Shaders / TMUs / ROPs"]) # 타이틀 이름 입력 (엑셀 파일 최초로 만들때만 사용)

url = "https://www.techpowerup.com/gpu-specs/?eol=Active&sort=name"
        
res = requests.get(url) # res 변수에 url 담기
res.raise_for_status # 접속이 문제 없는지 확인
soup = BeautifulSoup(res.text, "lxml") # BeautifulSoup 변수 생성
    

for i in range(1):
    news_list = soup.find_all("span", attrs={"class":re.compile("^prdname")}) # 기사에 대한 모든 요소 정보를 써치
    # gpu_list = soup.find_all("li", {id : "rk4524"})
    print(news_list)
    # news_list = soup.find("div", attrs={"class":("news-list")}).find_all("li", limit=5) # 설정한 갯수만큼만 기사를 써치
        
#     for news in news_list:
#         # news_name = news.find("a")["href"] # 써치된 모든 요소에서 기사 이름 써치
#         amd_gpu = news.find("td", attrs={"class":"vendor-AMD"}).get_text()
#         amd_gpu2 = amd_gpu.rstrip()
#         #list > table > tbody:nth-child(3)
        
#         intel_gpu = news.find("td", attrs={"class":"vendor-Intel"}).get_text()
#         intel_gpu2 = intel_gpu.rstrip()
        
#         nvidia_gpu = news.find("td", attrs={"class":"vendor-NVIDIA"}).get_text()
#         nvidia_gpu = nvidia_gpu.rstrip()
        
#         # news_link = news.find("a")["href"] # 써치된 모든 요소에서 기사 링크 써치
#         # news_day = news.find("span", attrs={"class":"date"}).get_text() # 써치된 모든 요소에서 기사 날짜 써치
#         # news_summary = news.find("div", attrs={"class":"summary"}).get_text() # 써치된 모든 요소에서 기사 요약 내용을 텍스트로 써치


# # wb = openpyxl.load_workbook(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\PC.xlsx') # 만들어져 있는 엑셀 오픈
 
# sheet.append([amd_gpu2]) # 변수 이름 입력으로 디바이스 정보 입력
# sheet.append([intel_gpu2])

# wb.save(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\PC.xlsx') # 엑셀 파일 세이브
# wb.close() # 엑셀 파일 닫기