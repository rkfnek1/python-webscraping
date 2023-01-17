import requests
import json
import datetime

# 슬랙 메세지 공유를 가능 하게 해주는 함수 (모듈 대신 사용하는 코드)
def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel, "text": text ,"attachments": attachments})

# 정리한 뉴스 텍스트 슬랙 봇으로 공유   
def test_message():
    Token = 'xoxb-2632799608037-3400993070864-lxhhYJQB4QdynU1KELxiJ734' # 공유하는 슬랙의 봇 토큰
    # Token2 = 'xoxb-3335002115717-3343261330306-CRxaElDQkAaN9MaOZDwHnl0c'
    
    now = datetime.datetime.now() # 현재 날짜 구하기
    # yesterday = now - datetime.timedelta(1) # 어제 날짜 구하기 (days=1)
    # yesterday_date = yesterday.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
    yesterday_date = now.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
    
    file = open(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\뉴스.txt', 'r', encoding="utf-8-sig")
    str2 = yesterday_date + ' 게임 뉴스 입니다.'
    
    while True: # 모든 줄 출력을 위해 while을 사용
        lines = file.read()
        if not lines : break
    
        attach_dict = {
            'color' : "#ff0000",
            # 'author_name' : "게임 뉴스 봇",
            # 'title' : "test",
            # 'title_link' : "https://www.thisisgame.com/webzine/news/nboard/263/" + news_link,
            'text' : f"{lines}"
        } # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력

        attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
            
        # notice_message(Token, "#qa_private_news", str2, attach_list)
        notice_message(Token, "#공통_잡담", str2, attach_list)
        # notice_message(Token, "##qa_private_news", str2, attach_list)
        # notice_message(Token2, "#bot", str2, attach_list)


test_message()