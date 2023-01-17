import random
import requests
import json
import datetime
import sys

# 슬랙 메세지 공유를 가능 하게 해주는 함수 (모듈 대신 사용하는 코드)
def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel, "text": text ,"attachments": attachments})

def lunch_message():
    Token = 'xoxb-2632799608037-3495705867026-eecZaP8ZeTH0UByAHr4uYL2v' # 공유하는 슬랙의 봇 토큰
    # Token2 = 'xoxb-3335002115717-3343261330306-CRxaElDQkAaN9MaOZDwHnl0c'
    
    now = datetime.datetime.now() # 현재 날짜 구하기
    # yesterday = now - datetime.timedelta(1) # 어제 날짜 구하기 (days=1)
    yesterday_date = now.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
    
    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    day = datetime.datetime.today().weekday()
    today = days[day]
    
    #######################################################################################################################################################
    lunch = ["발해 양꼬치", "전티마이 베트남 쌀국수", "미가라멘", "현대옥", "버거 스캔들", "청담동 마녀김밥", "텬고", "그리너", "83순대국", "비아김밥", "버텍스 미국식 덮밥", "육대장", "은행골", "킹스부대찌개", "슬로우캘리", "달그락", "매반생면"]
    # lunch = ["발해 양꼬치", "텬고", "미가라멘"]
    
    file = open(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\전날 점심.txt', 'r', encoding="utf-8-sig") # 파일 열기 (처음 사용할 때는 전날 점심.txt 직접 만들어 줘야함)
    # file = open(r'\\blackstorm_res\BlackStorm_Share\QA\봇\전날 점심.txt', 'r', encoding="utf-8-sig")
    
    lines = file.read() # 전날 점심 메뉴 읽어오기
    lines_2 = lines.rstrip("\n") # 불러온 텍스트 뒤에 \n제거
    # lines_2 = lines.rstrip()
    
    lunch.remove(lines_2) # 불러온 전날 점심 메뉴 lunch 리스트에서 제거
    
    random.shuffle(lunch) # lunch 리스트 섞기
    c = random.choice(lunch) # 섞인 lunch 리스트에서 하나 선택
    
    sys.stdout = open('전날 점심.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
    print(c)
    sys.stdout.close() # 메모장으로 저장
    #######################################################################################################################################################
    
    #######################################################################################################################################################
    bh = "발해 양꼬치" # 가게 이름 변수 생성
    bh_1 = ["짜장면", "짬뽕", "새우볶음밥", "마파두부덮밥"] # 메뉴 리스트 생성
    
    # jg = "찌개마을" 
    # jg_1 = ["김치찌개", "된장찌개"]
        
    # Chinese_food = "셰프 짬뽕"
    # Chinese_food_1 = ["짬뽕", "짜장면", "간짜장", "볶음밥", "짜장밥", "짬뽕밥"]
        
    rice_noodles = "전티마이 베트남 쌀국수"
    rice_noodles_1 = ["소고기쌀국수", "볶음밥"]
        
    ramen = "미가라멘"
    ramen_1 = ["돈코츠라멘", "미소라멘", "소유라멘", "시오버터라멘", "나가사키짬뽕", "얼큰짬뽕", "치킨가라아게동", "가츠동", "에비동", "차슈동"]
        
    hd = "현대옥"
    hd_1 = ["전주끓이는식콩나물국밥", "전주남부시장식 콩나물국밥", "얼큰돼지국밥", "황태콩나물국밥", "오색나물콩나물국밥", "순한두부찌개", "현대옥순대국밥", "현대옥순한두부찌개", "현대옥콩나물밥", "전주비빔밥", "현대옥스테이크"]
        
    burgerscandal = "버거 스캔들"
    burgerscandal_1 = ["스캔들버거 세트", "피쉬앤치즈버거 세트", "레전드치킨버거 세트", "아메리칸 치즈버거 세트"]
        
    kimbap = "청담동 마녀김밥"
    kimbap_1 = ["마녀김밥", "야채김밥", "계란마녀김밥", "고추김밥", "멸치김밥", "참치김밥", "핫도그김밥", "묵은지김밥", "묵참김밥", "마녀떡볶이", "마녀쫄면", "마녀라면", "묵은지 라면"]
        
    Tengo = "텬고"
    Tengo_1 = ["텬고 국물 떡볶이", "텬고 치브 떡볶이", "텬고 치즈라볶이", "텬고 라볶이"]
        
    Greener = "그리너"
    Greener_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    kimbap2 = "비아김밥"
    kimbap2_1 = ["일반 라면", "표고라면", "미역 너구리", "야채김밥", "참치김밥", "치즈김밥", "김치김밥", "야땡김밥(야채+땡초)", " 참땡(참치+땡초)", " 김땡(김치+땡초)", "멸땡(멸치+땡초)", " 왕계란김밥", "크래미김밥", "돈가스김밥", "왕새우김밥", "스팸김밥", "고추장진미김밥", "간장진미김밥", "소고기김밥", "계란김치김밥", "참치치즈김밥", "참치김치김밥", "고추장진미치즈김밥", " 고추장진미새우김밥", "고기없는채소김밥(키토)", "채소김밥고기많이(키토)", "왕계란키토"]
        
    vertex = "버텍스 미국식 덮밥"
    vertex_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    yuggyejang = "육대장"
    yuggyejang_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    eunhaeng_gol = "은행골"
    eunhaeng_gol_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    budaejjigae = "킹스부대찌개"
    budaejjigae_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    SlowCali = "슬로우캘리"
    SlowCali_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    # Gyodong = "교동짬뽕"
    # Gyodong_1 = []
        
    # bonjug = "본죽&비빔밥 카페"
    # bonjug_1 = []
        
    # Subway = "서브웨이"
    # Subway_1 = []
        
    sundae = "83순대국"
    sundae_1 = "식대 가격 초과로 메뉴 추천 제외"
        
    # Burger_King = "버거킹"
    # Burger_King_1 = []
    
    dalgeulag = "달그락"
    dalgeulag_1 = "식대 가격 초과로 메뉴 추천 제외"
    
    Maeban_Saengmyeon = "매반생면"
    Maeban_Saengmyeon_1 = "식대 가격 초과로 메뉴 추천 제외"
    
    if c == bh: # 변수 c에 지정된 가게와 변수 bh에 생성된 가게 이름 비교
        random.shuffle(bh_1) # 메뉴 리스트 섞기
        bh_2 = random.choice(bh_1) # 섞인 lunch 리스트에서 메뉴 선택
        bh_3 = random.choice(bh_1) # 섞인 lunch 리스트에서 메뉴 선택
        n = bh_2 # 선택된 메뉴 변수로 지정
        s = bh_3 # 선택된 메뉴 변수로 지정
    # elif c == Chinese_food:
    #     random.shuffle(Chinese_food_1) # 메뉴 리스트 섞기
    #     Chinese_food_2 = random.choice(Chinese_food_1)
    #     Chinese_food_3 = random.choice(Chinese_food_1)
    #     n = Chinese_food_2
    #     s = Chinese_food_3
    elif c == ramen:
        random.shuffle(ramen_1) # 메뉴 리스트 섞기
        ramen_2 = random.choice(ramen_1)
        ramen_3 = random.choice(ramen_1)
        n = ramen_2
        s = ramen_3
    elif c == rice_noodles:
        random.shuffle(rice_noodles_1) # 메뉴 리스트 섞기
        rice_noodles_2 = random.choice(rice_noodles_1)
        rice_noodles_3 = random.choice(rice_noodles_1)
        n = rice_noodles_2
        s = rice_noodles_3
    elif c == hd:
        random.shuffle(hd_1)
        hd_2 = random.choice(hd_1)
        hd_3 = random.choice(hd_1)
        n = hd_2
        s = hd_3
    elif c == burgerscandal:
        random.shuffle(burgerscandal_1)
        burgerscandal_2 = random.choice(burgerscandal_1)
        burgerscandal_3 = random.choice(burgerscandal_1)
        n = burgerscandal_2
        s = burgerscandal_3
    elif c == kimbap:
        random.shuffle(kimbap_1)
        kimbap_2 = random.choice(kimbap_1)
        kimbap_3 = random.choice(kimbap_1)
        n = kimbap_2
        s = kimbap_3
    elif c == dalgeulag:
        n = dalgeulag_1
        s = dalgeulag_1
    elif c == Maeban_Saengmyeon:
        n = Maeban_Saengmyeon_1
        s = Maeban_Saengmyeon_1
    elif c == Tengo:
        while today == "월요일":
            lunch2 = ["발해 양꼬치", "전티마이 베트남 쌀국수", "미가라멘", "현대옥", "버거 스캔들", "청담동 마녀김밥", "그리너", "83순대국", "비아김밥", "텬고", "버텍스 미국식 덮밥", "육대장", "은행골", "킹스부대찌개", "슬로우캘리", "달그락", "매반생면"]
            # lunch2 = ["발해 양꼬치", "텬고", "미가라멘"]
            
            file = open(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\전날 점심.txt', 'r', encoding="utf-8-sig") # 파일 열기 (처음 사용할 때는 전날 점심.txt 직접 만들어 줘야함)
            lines = file.read() # 전날 점심 메뉴 읽어오기
            
            lines_2 = lines.rstrip("\n") # 불러온 텍스트 뒤에 \n제거
            lunch2.remove(lines_2) # 불러온 전날 점심 메뉴 lunch 리스트에서 제거
            
            random.shuffle(lunch2) # lunch 리스트 섞기
            c = random.choice(lunch2) # 섞인 lunch 리스트에서 하나 선택
            break
    if c == Tengo:
        random.shuffle(Tengo_1)
        Tengo_2 = random.choice(Tengo_1)
        Tengo_3 = random.choice(Tengo_1)
        n = Tengo_2
        s = Tengo_3
    elif c == Greener:
        n = Greener_1
        s = Greener_1
    elif c == sundae:
        n = sundae_1
        s = sundae_1
    elif c == kimbap2:
        random.shuffle(kimbap2_1)
        kimbap2_2 = random.choice(kimbap2_1)
        kimbap2_3 = random.choice(kimbap2_1)
        n = kimbap2_2
        s = kimbap2_3
    elif c == vertex:
        n = vertex_1
        s = vertex_1
    elif c == yuggyejang:
        n = yuggyejang_1
        s = yuggyejang_1
    elif c == eunhaeng_gol:
        n = eunhaeng_gol_1
        s = eunhaeng_gol_1
    elif c == budaejjigae:
        n = budaejjigae_1
        s = budaejjigae_1
    elif c == SlowCali:
        n = SlowCali_1
        s = SlowCali_1
    elif c == bh:
        random.shuffle(bh_1) # 메뉴 리스트 섞기
        bh_2 = random.choice(bh_1) # 섞인 lunch 리스트에서 메뉴 선택
        bh_3 = random.choice(bh_1) # 섞인 lunch 리스트에서 메뉴 선택
        n = bh_2 # 선택된 메뉴 변수로 지정
        s = bh_3 # 선택된 메뉴 변수로 지정
    elif c == ramen:
        random.shuffle(ramen_1) # 메뉴 리스트 섞기
        ramen_2 = random.choice(ramen_1)
        ramen_3 = random.choice(ramen_1)
        n = ramen_2
        s = ramen_3
    elif c == rice_noodles:
        random.shuffle(rice_noodles_1) # 메뉴 리스트 섞기
        rice_noodles_2 = random.choice(rice_noodles_1)
        rice_noodles_3 = random.choice(rice_noodles_1)
        n = rice_noodles_2
        s = rice_noodles_3
    elif c == hd:
        random.shuffle(hd_1)
        hd_2 = random.choice(hd_1)
        hd_3 = random.choice(hd_1)
        n = hd_2
        s = hd_3
    elif c == burgerscandal:
        random.shuffle(burgerscandal_1)
        burgerscandal_2 = random.choice(burgerscandal_1)
        burgerscandal_3 = random.choice(burgerscandal_1)
        n = burgerscandal_2
        s = burgerscandal_3
    elif c == kimbap:
        random.shuffle(kimbap_1)
        kimbap_2 = random.choice(kimbap_1)
        kimbap_3 = random.choice(kimbap_1)
        n = kimbap_2
        s = kimbap_3
    elif c == dalgeulag:
        n = dalgeulag_1
        s = dalgeulag_1
    elif c == Maeban_Saengmyeon:
        n = Maeban_Saengmyeon_1
        s = Maeban_Saengmyeon_1
        #######################################################################################################################################################
        
    str2 = yesterday_date + ' 점심 추천 입니다.'
        
    while True: # 모든 줄 출력을 위해 while을 사용
        attach_dict = {
            'color' : "#ff0000",
            # 'author_name' : f"추천 가게 : {c}",
            'title' : f"추천 가게 : {c}",
            # 'title_link' : "https://www.thisisgame.com/webzine/news/nboard/263/" + news_link,
            'text' : f"추천 메뉴\n팀장님 : {n}\n사원 : {s}"
        } # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력

        attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
                
        notice_message(Token, "#qa_private", str2, attach_list)
        # notice_message(Token2, "#bot", str2, attach_list)
        break

lunch_message()