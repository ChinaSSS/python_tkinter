import tkinter
win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")


#绑定变量
lbv = tkinter.StringVar()

#不支持鼠标移动选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()
for i in [1,2,3,4,5,6]:
    #按顺序添加
    lb.insert(tkinter.END,i)
#在开始添加
lb.insert(tkinter.ACTIVE,"one")
lb.insert(tkinter.END,[1,2,3,4,5])

#打印当前列表中的选项
print(lbv.get())
#改变选项
# lbv.set(("1","2"))

#绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>",myPrint)  #绑定事件














win.mainloop()