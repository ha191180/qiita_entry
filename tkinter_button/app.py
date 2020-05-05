import tkinter
import threading
import time
from tkinter import messagebox

class Button(tkinter.Button):
    def __init__(self):
        super().__init__(
            master=None,
            text="Act",
            width=100,
            command=self.Button_click
            )

    def Button_click(self):
        text_message.set("実行中です。しばらくお待ちください。")
        thread = threading.Thread(target = tmp)
        thread.start()

def tmp():
    Button_act["state"] = tkinter.DISABLED
    try:
        time.sleep(10)
    except Exception:
        messagebox.showwarning("warning", "エラーです")
    else:
        messagebox.showinfo("message", "正常終了です")
    finally:
        text_message.set("入力を行い、Actを押してください。")
        Button_act["state"] = tkinter.NORMAL

root = tkinter.Tk()
root.title(u"Test App")

Button_act = Button()
Button_act.grid(row = 0, column = 0)

text_message = tkinter.StringVar()
text_message.set("入力を行い、Actを押してください。")
label_info = tkinter.Label(textvariable = text_message, font = ("", 10,"bold"), justify = "left")
label_info.grid(row = 1, column = 0)

tkinter.mainloop()