import requests
import openpyxl
from bs4 import BeautifulSoup

##################################################################
# 만들어진 엑셀 파일은 py파일이 있는 폴더의 최상단 폴더에 만들어짐
# 엑셀 파일은 최상단 폴더에만 존재하면됨
##################################################################

# wb = openpyxl.Workbook(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping') # 새로운 엑셀 열기
wb = openpyxl.load_workbook(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\디바이스.xlsx') # 만들어져 있는 엑셀 오픈

sheet = wb.active # 현재 Active Sheet 얻기

# sheet.append(["디바이스", "System_chip", "Processor", "GPU", "RAM", "Internal_storage", "Device_type", "OS", "Size", "Resolution"]) # 타이틀 이름 입력 (엑셀 파일 최초로 만들때만 사용)

# 정보를 불러올 사이트 입력
url = "https://www.phonearena.com/phones/Google-Pixel-6_id11732" # url 정보 입력 (새로운 디아비스의 url을 여기다 입력)

res = requests.get(url) # res 변수에 url 담기
res.raise_for_status # 접속이 문제 없는지 확인
soup = BeautifulSoup(res.text, "lxml") # BeautifulSoup 변수 생성

# selector 정보로 디바이스 정보 획득
# Phone = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_quickSpecs > header > h1').text
# Phone2 = Phone.rstrip() # 뒤에 공백 제거
Phone = soup.select_one('body > article > div.layout__page_breadcrumbs > ul > li.active > span').text
Phone2 = Phone.rstrip() # 뒤에 공백 제거

Processor = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(2) > td').text
Processor2 = Processor.rstrip() # 뒤에 공백 제거

GPU = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(3) > td').text
GPU2 = GPU.rstrip() # 뒤에 공백 제거

System_chip = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(1) > td').text
System_chip2 = System_chip.rstrip() # 뒤에 공백 제거

RAM = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(4) > td').text
RAM2 = RAM.rstrip() # 뒤에 공백 제거

Internal_storage = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(5) > td').text
Internal_storage2 = Internal_storage.rstrip() # 뒤에 공백 제거

Device_type = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(6) > td').text
Device_type2 = Device_type.rstrip() # 뒤에 공백 제거

OS = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(3) > table > tbody > tr:nth-child(7) > td').text
OS2 = OS.rstrip() # 뒤에 공백 제거

Size = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(1) > table > tbody > tr:nth-child(1) > td').text
Size2 = Size.rstrip() # 뒤에 공백 제거

Resolution = soup.select_one('body > article > div.layout__page_main > section.page__section.page__section_specs > section > div.widgetSpecs > section:nth-child(1) > table > tbody > tr:nth-child(2) > td').text
Resolution2 = Resolution.rstrip() # 뒤에 공백 제거

sheet.append([Phone2, System_chip2, Processor2, GPU2, RAM2, Internal_storage2, Device_type2, OS2, Size2, Resolution2]) # 변수 이름 입력으로 디바이스 정보 입력

wb.save(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\디바이스.xlsx') # 엑셀 파일 세이브
wb.close() # 엑셀 파일 닫기
