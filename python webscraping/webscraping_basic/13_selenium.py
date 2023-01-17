import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome() # "./chromedriver.exe" 크롬 실행
browser = webdriver.Edge("./msedgedriver.exe") # "./msedgedriver.exe" 마이크로 소프트 엣지 브라우저 실행

#네이버 이동
browser.get("https://naver.com")

# 선택한 부분의 값을 불러 올때 사용 (class_name)
# elem = browser.find_element_by_class_name("link_login")

# 선택한 부분의 값을 불러 올때 사용 (id)
# elem = browser.find_element_by_id("query")

# 선택한 부분의 값을 불러 올때 사용 (xpath)
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")

# 선택한 부분의 값을 불러 올때 사용 (tag_name)
# elem = browser.find_element_by_tag_name("a")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login").click()
time.sleep(1)

# 아이디 및 비밀번호 입력
browser.find_element_by_id("id").send_keys("rkfnek1")
time.sleep(1)
browser.find_element_by_id("pw").send_keys("vkrns1")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("btn_login").click()
time.sleep(1)

# 아이디 번경
# browser.find_element_by_id("id").clear() # 입력된 텍스 삭제
# browser.find_element_by_id("id").send_keys("naver_1")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 브라우저 전체 종료