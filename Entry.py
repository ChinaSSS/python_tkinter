import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+0")  #小写x  长宽  x ,y 坐标




'''
输入控件 ，显示简单的文本内容
'''
#绑定变量
e = tkinter.Variable()

#密文显示 show = "*"

entry = tkinter.Entry(win, textvariable = e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("ironman is a good man ")
#取值
print(e.get())

win.mainloop()
