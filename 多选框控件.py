import tkinter

win = tkinter.Tk()
win.title = "ironman"
win.geometry("400x400+200+100")

'''
checkButton 多选框控件
'''

def updata():
    message = ""
    if hobby1.get() == True:
        message += "you love me\n"
    if hobby2.get() == True:
        message += "i love you \n"
    if hobby3.get() == True:
        message += "you love me and love you \n"
    text.delete(0.0,tkinter.END) #清空text中的所有内容
    text.insert(tkinter.INSERT,message)

#绑定变量
hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text = "you love me",variable = hobby1,command = updata)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text = " i love you",variable = hobby2,command = updata)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text = "you love me and i love you ",variable = hobby3,command = updata)
check3.pack()


text = tkinter.Text(win,width = 20,height = 10)
text.pack()





win.mainloop()