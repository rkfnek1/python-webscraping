import time, win32con, win32api, win32gui

# 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = '회사'

# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)
    
# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    
# # 채팅방 열기
def open_chatroom(chatroom_name):
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1) # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)
    
def main():
    open_chatroom(kakao_opentalk_name) # 채팅방 열기
    
    file = open(r'C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\뉴스.txt', 'r', encoding="utf-8-sig")
    
    while True: # 모든 줄 출력을 위해 while을 사용
        lines = file.read()
        if not lines : break
        text = f"{lines}"

    kakao_sendtext(kakao_opentalk_name, text)    # 메시

if __name__ == '__main__':
    main()