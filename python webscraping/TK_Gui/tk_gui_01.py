import tkinter
from tkinter import *

def button_clicked():
    # print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
# my_label.grid(column=0, row=0)

button = Button(text="button", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

label = Button(text="Label", command=button_clicked)
label.grid(column=0, row=0)

New_Button = Button(text="New Button", command=button_clicked)
New_Button.grid(column=2, row=0)

entry = Button(text="Entry", command=button_clicked)
entry.grid(column=4, row=3)


my_label["text"] = "New Text"
my_label.config(text="New Text")


input = Entry(width=10)
print(input.get())
# input.pack(side="left")
input.grid(column=2, row=2)



window.mainloop()