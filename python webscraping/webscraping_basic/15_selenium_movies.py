import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=ko&gl=kr"
# headers = {
#     "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
#     "Accept-Language":"ko-KR,ko"
#     }
headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"}
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    #f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력