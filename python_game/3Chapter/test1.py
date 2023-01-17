from cProfile import label
import calendar
import datetime
import random
from threading import main_thread
import tkinter
import tkinter.messagebox
import tkinter.font
import tkinter.messagebox

# print(calendar.isleap(2022))
# print(datetime.date.today())


# d = datetime.datetime.now()
# print(d.hour)
# print(d.minute)
# print(d.second)

# today = datetime.date.today()
# birth = datetime.date(1989, 7, 12)

# print(today - birth)

# r = random.random()
# print(r)

# rs = random.randint(1, 5)
# print(rs)

# cis = ["가위", "바위", "보"]

# srp = random.choice(cis)

# print(srp)

# cnt = 0
# while True:
#     r = random.randint(1, 100)
#     print(r)
#     cnt = cnt + 1
#     if r == 77:
#         break
# print(str(cnt) + "획득")

# mj =["말 이름은?", "새 이름은?", "물고기 이름은?"]
# jd = ["루비", "닭", "붕어"]
# for i in range(3):
#     print(mj[i])
#     ans = input()
#     if ans == jd[i]:
#         print("정답")
#     else:
#         print("오답")


# ans = input()
# if ans == "사자" or ans == "호랑이":
#     print("정답")
# else:
#     print("오답")

# pl_pso = 1
# pc_pso = 1
# def board():
#     print("." * (pl_pso -1) + "p" + "."* (30 - pl_pso) + "Goal")
#     print("." * (pc_pso -1) + "c" + "."* (30 - pc_pso) + "Goal")

# board()
# while True:
#     input()
#     pl_pso = pl_pso + random.randint(1, 6)
#     if pl_pso > 30:
#         pl_pso = 30
#     board()
#     if pl_pso == 30:
#         print("p 승리")
#         break
#     input()
#     pc_pso = pc_pso + random.randint(1, 6)
#     if pc_pso > 30:
#             pc_pso = 30
#     board()
#     if pc_pso == 30:
#         print("c 승리")
#         break

# alp = ["a", "b", "c", "d", "e", "f", "g"]
# r = random.choice(alp)
# alp_1 = ""
# for i in alp:
#     if i != r:
#         alp_1 = alp_1 + i
# print(alp_1)
# st = datetime.datetime.now()
# ans = input("정답은?")
# if ans == r:
#     print("정답")
#     et = datetime.datetime.now()
#     print(str((et - st).seconds) + "초")
# else:
#     print("오답")

# def click_btn():
#     button["text"] = "클릭완"

# root = tkinter.Tk()
# root.title("윈도우 창")
# root.geometry("800x600")
# lable = tkinter.Label(root, text="글씨", font=("돋움체", 24))
# lable.place(x=10, y=10)
# button = tkinter.Button(root, text="클릭", font=("돋움체", 24), command=click_btn)
# button.place(x=200, y=100)
# root.mainloop()

# root = tkinter.Tk()
# root.title("윈도우 창")
# canvas = tkinter.Canvas(root, width=400, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\3d.png")
# canvas.create_image(200, 300, image=gazou)
# root.mainloop()

# def click_btn():
#     label["text"] = random.choice(["대흉", "흉", "소길", "중길", "대길"])
#     label.update()
    
# root = tkinter.Tk()
# root.title("뽑기")
# root.resizable(False, False)

# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()

# gazou = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\3d.png")
# canvas.create_image(180, 300, image = gazou)

# label = tkinter.Label(root, text="??", font=("돋움체", 120), bg="white")
# label.place(x=350, y=100)

# button = tkinter.Button(root, text="뽑기", font=("돋움체", 36), command=click_btn, fg="skyblue")
# button.place(x=360, y=400)

# root.mainloop()

# def click_btn():
#     txt = entry.get()
#     button["text"] = txt
    
# def click_btn2():
#     text.insert(tkinter.END, "몬스터가 나타났다!")

# root = tkinter.Tk()
# root.title("윈도우 창")
# root.geometry("400x200")

# # entry = tkinter.Entry(width = 20)
# # entry.place(x = 20, y = 20)

# button = tkinter.Button(text="문자열", command=click_btn2)
# button.pack()
# text = tkinter.Text()
# text.pack()
# # button.place(x = 20, y = 100)

# root.mainloop()

# def check():
#     if cval.get() == True:
#         print("체크")
#     else:
#         print("미체크")

# def click_btn():
#     tkinter.messagebox.showinfo("정보", "버튼 누름")

# root = tkinter.Tk()
# root.title("윈도우 창")
# root.geometry("400x200")

# cval = tkinter.BooleanVar()
# cval.set(False)

# cbtn = tkinter.Checkbutton(text="체크 박스", variable=cval, command=check)
# cbtn.pack()

# btn = tkinter.Button(text="누름", command=click_btn)
# btn.pack()

# root.mainloop()

# KEKKA = ["전생에 고양이었을 가능성은 매우 낮습니다.", "보통 사람입니다.", "특별히 이상한 곳은 없습니다.", "꽤 고양이다운 구석이 있습니다.", "고양이와 비슷한 성격 같습니다.", "고양이와 근접한 성격입니다.", "전생에 고양이었을지도 모릅니다.", "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."]

# def click_btn():
#     pts = 0
#     for i in range(7):
#         if bvar[i].get() == True:
#             pts = pts + 1
#     nekodo = int(100 * pts / 7)
#     text.delete("1.0", tkinter.END)
#     text.insert("1.0", "<진단결과>\n당신의 고양이 지수는" + str(nekodo) + "%입니다. \n" + KEKKA[pts])

# root = tkinter.Tk() 
# root.title("윈도우 창")
# root.resizable(False, False)

# canvas = tkinter.Canvas(root, width = 800, height = 600)
# canvas.pack()

# gezou = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\3d.png")
# canvas.create_image(140, 200, image=gezou)

# button = tkinter.Button(text="진단", font=("돋움체", 32), bg="lightgreen", command=click_btn)
# button.place(x = 400, y = 480)

# text = tkinter.Text(width = 40, height = 5, font=("돋움체", 16))
# text.place(x = 320, y = 30)

# bvar = [None] * 7
# cbtn = [None] * 7

# ITEM = ["높은 곳이 좋다", "공을 보면 굴리고 싶다", "깜짝 놀마녀 털이 곤두선다", "쥐구멍이 마음에 든다", "개에게 적대감을 느낀다.", "생선 뼈를 발라 먹고 싶다.", "밤, 기운이 난다"]

# for i in range(7):
#     bvar[i] = tkinter.BooleanVar()
#     bvar[i].set(False)
#     cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("돋움체", 12), variable=bvar[i], bg="#dfe") 
#     cbtn[i].place(x=400, y=160 + 40 * i)

# root.mainloop()

# tmr = 0

# def count_up():
#     global tmr
#     tmr = tmr + 1
#     label["text"] = tmr
#     root.after(1000, count_up)
    
# root = tkinter.Tk()
# root.title("키코드 얻기")

# label = tkinter.Label(font=("돋움체", 80))
# label.pack()

# root.after(1000, count_up)
# root.mainloop()

# key = ""
# def key_down(e):
#     global key
#     key = e.keysym
#     # key = e.keycode
#     # print("KEY:", str(key))
    
# def key_up():
#     global key
#     key = ""
    
# cx = 400
# cy = 300

# def main_proc():
#     global cx, cy
#     if key == "Up":
#         cy = cy - 20
#     if key == "Down":
#         cy = cy + 20
#     if key == "Left":
#         cx = cx - 20
#     if key == "Right":
#         cx = cx + 20
#     canvas.coords("MYCHR", cx, cy)
#     root.after(100, main_proc)
    
#     # label["text"] = key``
#     # root.after(100, main_proc)

# root = tkinter.Tk()
# root.title("캐릭터 이동")

# root.bind("<KeyPress>", key_down)
# root.bind("<KeyRelease>", key_up)

# canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
# canvas.pack()

# img = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\mimi_cat.png")
# canvas.create_image(cx, cy, image=img, tag="MYCHR")

# # label = tkinter.Label(font=("돋움체", 80))
# # label.pack()

# main_proc()

# root.mainloop()


key = ""
def key_down(e):
    global key
    key = e.keysym
    
def key_up(e):
    global key
    key = ""
    
mx = 1
my = 1
yuka = 0

def main_proc():
    global mx, my, yuka
    if key == "Shift_L" and yuka > 1:
        canvas.delete("PAINT")
        mx = 1
        my = 1
        yuka = 1
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
    if key == "Up" and maze[my - 1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        yuka = yuka + 1
        canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0, tag="PAINT")
    canvas.delete("MYCHR")
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("클리어", "모든 바닥 칠함")
    else:
        root.after(300, main_proc)

root = tkinter.Tk()
root.title("미로")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width=0)
            
img = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\mimi_s.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
main_proc()

root.mainloop()