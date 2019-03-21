import tkinter

win = tkinter.Tk()
win.title("ironman")
win.geometry("400x400+200+100")

'''
文本控件，用于显示多行文本
'''

str = '''aaaaaaaaaaaaaaaaaaaaaaa
         bbbbbbbbbbbbbbbbbbbbbbb'''
text = tkinter.Text(win, width = 20, height = 4)
text.pack()
text.insert(tkinter.INSERT,str)










win.mainloop()
