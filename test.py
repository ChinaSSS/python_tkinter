import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("600x400+200+100")

e = tkinter.Variable()
#entry
entry = tkinter.Entry(win,width=50,textvariable=e)
entry.pack()
e.set("i love you, so i want to know your ideas!!!")

#单选框
def showdata():
    text.delete(0.0,tkinter.END)
    if r.get() == 1:
        text.insert(tkinter.INSERT,"it would be together")
    else:
        text.insert(tkinter.INSERT,"ok you love me")

r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win,text="yes",value=1,variable=r,command=showdata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text="no",value=2,variable=r,command=showdata)
radio2.pack()

#Text
text = tkinter.Text(win,width=50,height=1)
text.pack()

#按钮
def but():
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,"before quit,please say love me.")

button = tkinter.Button(win,width=6,height=1,text="quit",command=but)
button.pack()

#lable
lable = tkinter.Label(win,
                      text="youaresobeautiful",
                      bg="red",
                      fg="black",
                      font=("宋体",20),
                      )
lable.pack()








win.mainloop()