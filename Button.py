import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("ironman")
#设置大小和位置
win.geometry("400x400+200+0")  #小写x  长宽  x ,y 坐标


def zhang():
    print("i love you ")

#创建button
button = tkinter.Button(win, text = "按钮",command = zhang,width =5 , height = 5)
button.pack()

button2 = tkinter.Button(win, text = "退出",command =win.quit,width =3 , height = 4)
button2.pack()


win.mainloop()

