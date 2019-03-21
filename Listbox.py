import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")

'''
列表框控件，可以包含一个或者多个文本框
'''

#创建一个Listbox
lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()
for i in [1,2,3,4,5,6]:
    #按顺序添加
    lb.insert(tkinter.END,i)
#在开始添加
lb.insert(tkinter.ACTIVE,"one")
lb.insert(tkinter.END,[1,2,3,4,5])

#删除 args 开始索引 结束索引
#没有参数2 只删除第一个索引的一个数
# lb.delete(0,3)
# lb.delete(3)


#选中
# lb.select_set(1,3)
#取消选中
# lb.select_clear(2)


print(lb.size())
print(lb.get(2))
#返回当前的索引项
print(lb.curselection())

print(lb.selection_includes(2))







win.mainloop()