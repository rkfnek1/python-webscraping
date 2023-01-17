import requests
#res = requests.get("https://naver.com")
res = requests.get("https://google.com")
res.raise_for_status()
#print("응답코드 : ", res.status_code) #200 이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제")

print(len(res.text))
with open("mygoogl.html", "w", encoding="utf8") as f:
    f.write(res.text)