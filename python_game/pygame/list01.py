import tkinter
FNT = ("Times New Roman", 30)

class GameCharacter:
    def __init__(self, job, life, imgfile):
        self.job = job
        self.life = life
        self.img = tkinter.PhotoImage(file=imgfile)
    
    def draw(self):
        canvas.create_image(200, 280, image=self.img)
        canvas.create_text(300, 400, text=self.job, font=FNT, fill="red")
        canvas.create_text(300, 480, text=self.life, font=FNT, fill="blue")
        
root = tkinter.Tk()
root.title("tkinter를 사용한 객체지향 프로그래밍")
canvas = tkinter.Canvas(root, width=400, height=500, bg="white")
canvas.pack()

character = GameCharacter("검사", 200, r"C:\Users\Blackstorm_plecios\Desktop\python_game\pygame\swordsman.png")
character.draw()

root.mainloop()