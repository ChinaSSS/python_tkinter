import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+0")  #小写x  长宽  x ,y 坐标

def showinfo():
    print(entry.get())

entry = tkinter.Entry(win,)
entry.pack()

button = tkinter.Button(win,text = "按钮",command = showinfo)
button.pack()





win.mainloop()
