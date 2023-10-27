import requests
from tkinter import *

def make_request():
    url = entry.get()
    response = requests.get(url)
    text.delete(1.0, END)  # 清空文本框内容
    text.insert(END, response.text)  # 在文本框中显示请求结果

root = Tk()
root.title("HTTP GET Request")

label = Label(root, text="请输入 URL：")
label.pack()
entry = Entry(root, width=50)
entry.pack()

button = Button(root, text="确定", command=make_request)
button.pack()

text = Text(root, height=20, width=80)
text.pack()

root.mainloop()