import time, win32con, win32api, win32gui
import datetime

kakao_opentalk_name = "회사"
def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
# hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit20W", None)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

now = datetime.datetime.now() # 현재 날짜 구하기
# yesterday = now - datetime.timedelta(1) # 어제 날짜 구하기 (days=1)
# yesterday_date = yesterday.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
yesterday_date = now.strftime('%Y.%m.%d') # 날짜를 년.월.일로 표시 (문자로 변환)
file = open(r'C:\Users\rkfne\OneDrive\바탕 화면\Pythonbot\뉴스.txt', 'r', encoding="utf-8-sig")
str2 = yesterday_date + ' 게임 뉴스 입니다.'

while True: # 모든 줄 출력을 위해 while을 사용
    lines = file.read()
    if not lines : break
    text = f"{lines}"

kakao_sendtext(text)