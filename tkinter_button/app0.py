import tkinter
import time
from tkinter import messagebox


def action(event):

    print("start") #追記
    
    text_message.set("実行中です。しばらくお待ちください。")
    time.sleep(10)
    text_message.set("入力を行い、Actを押してください。")
    messagebox.showinfo("message", "正常終了です")

    print("終了") #追記

root = tkinter.Tk()
root.title(u"Test App")

Button_act = tkinter.Button(text="Act", width=100)
Button_act.grid(row = 0, column = 0)
Button_act.bind("<1>", action)

text_message = tkinter.StringVar()
text_message.set("入力を行い、Actを押してください。")
label_info = tkinter.Label(textvariable = text_message, font = ("", 10,"bold"), justify = "left")
label_info.grid(row = 1, column = 0)

tkinter.mainloop()