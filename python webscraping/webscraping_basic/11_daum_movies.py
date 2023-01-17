import requests
from bs4 import BeautifulSoup



for year in range(2020, 2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status() # 안되는 것을 확인하는 코드 
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"}) # 클래스 속성 가져오기
    
    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"): # //로 시작한다면
            image_url = "httsp:" + image_url
                    
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status() # 안되는 것을 확인하는 코드 
        
        # 이미지 저장
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
            
        if idx >= 4:
            break