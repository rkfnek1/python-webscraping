import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")


cartoonlist = soup.find_all("a", attrs={"class":"title"})


# 네이버 실시간 인기 급상승 순위 불러오기
# rank = rank1.find_next_siblings("li")
# print(rank1.a.get_text())
# for ranks in rank:
#     print(ranks.a.get_text())


for cartoon in cartoonlist:
    titles = cartoon.get_text()
    # link = "https://comic.naver.com" + cartoon.a["href"]
    print(titles)