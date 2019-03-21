import tkinter
win = tkinter.Tk()
win.title("ironman")
# win.geometry("400x400+200+100")

#extended 可以使listbox 支持shift and ctrl
#按住shift可以连选
#按住ctrl可以多选
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    lb.insert(tkinter.END,i)
#创建滚动条
sc = tkinter.Scrollbar(win)
sc['command'] = lb.yview
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)












win.mainloop()