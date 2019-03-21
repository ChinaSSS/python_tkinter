import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")

'''
Label : 标签控件，显示文本
'''

#win 父窗体
#text 显示文本内容
#bg 背景色
#fg 字体颜色
#wraplength 指定text文本中的多宽换行，
#justify 指定对其方式
#anchor 位置 n(north) e(east) w(west)西 s(south) center
label = tkinter.Label(win,
                      text="ironman",
                      bg = "green",
                      fg = "red",
                      font =("黑体",20),
                      width = 10,
                      height = 4,
                      wraplength = 100,
                      justify = "left",
                      anchor = "center")
#显示出来
label.pack()





win.mainloop()