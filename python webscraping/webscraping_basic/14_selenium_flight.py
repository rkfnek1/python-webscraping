import time
from cv2 import BORDER_WRAP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge("./msedgedriver.exe") # "./msedgedriver.exe" 마이크로 소프트 엣지 브라우저 실행
browser.maximize_window()

#사이트 이동 이동
url = ("https://www.aerok.com/kr")
browser.get(url) # url로 이동

time.sleep(4)

# 가는날 선택 클릭
# browser.find_element_by_link_text("출발일").click()
# browser.find_element_by_class_name("criteria-dates-0").click()
browser.find_element_by_id("criteria-dates-0").click()
time.sleep(1)

# 해당 달의 일 선택 - [0]이번달, [1]다음달
# browser.find_elements_by_link_text("10")[1].click() # 텍스트 클릭
browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div[3]/div[4]/button/span").click()
time.sleep(1)
# browser.find_elements_by_link_text("16")[1].click()
browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div[4]/div[5]/button/span").click()
time.sleep(1)

# 적용 버튼 클릭
browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/button[2]").click()
time.sleep(1)

# 예약하기 버튼 클릭
browser.find_element_by_xpath("//*[@id='main-content']/div[2]/div/section[3]/section/div/div[2]/div[1]/div/div[2]").click()
# time.sleep(4)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='route-0']/div[2]/article[1]/section/div[1]/div")))
    print(elem.text)
    #성공했을 때 동작 수행
finally:
    browser.quit()

# 출력된 결과중 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='route-0']/div[2]/article[1]/section/div[1]/div")
# print(elem.text)