import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")

'''
radiobutton
'''

def updata():
    print(r.get())
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,r.get())

r = tkinter.IntVar() #一组单选框要绑定同一个变量
# r = tkinter.StringVar()

radio1 = tkinter.Radiobutton(win,text = "one",value=1,variable = r,command = updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text = "two",value =2,variable = r,command = updata)
radio2.pack()

text = tkinter.Text(win,width =20,height = 10)
text.pack()









win.mainloop()