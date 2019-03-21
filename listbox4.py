import tkinter
win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")

#========支持多选========
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()
for i in [1,2,3,4,5,6,7,8,9,10]:
    lb.insert(tkinter.END,i)











win.mainloop()