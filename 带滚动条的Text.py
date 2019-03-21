import tkinter

win = tkinter.Tk()
win.title("ironman")
# win.geometry("400x400+200+100")

'''
文本控件，用于显示多行文本
'''

str = '''aaaaaaaaaaaaaaaaaaaaaaa
         bbbbbbbbbbbbbbbbbbbbbbb
         cccccccccccccccccccccccc
         ddddddddddddddddddddddddd
         eeeeeeeeeeeeeeeeeeeeeeeee
         fffffffffffffffffffffffffff
         gggggggggggggggggggggggg
         wwwwwwwwwwwwwwwwwwwwwwwwwww
         afgsdfa adsfgfgfdfashffhafhhhhlafsjjfasf
         fasdhagjfajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
         lllllllllllllllllllllllllllllllllllllllllllllllllllll
         afddddddddddddddddddddddddddddddddddddddddddddddddddddd
         jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
         fffffffffffffffffffffffffffffffffffffffffffffffffffff
         fffffffffffffffffffffffffffffffffffffffffffffffffff
         fffffffffffffffffffffffffffffffffffffffffffffff
         '''
#创建滚动条
scroll = tkinter.Scrollbar()
scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)

text = tkinter.Text(win, width = 20, height = 8)
text.pack(side = tkinter.LEFT , fill = tkintre.Y)
text.insert(tkinter.INSERT,str)

#关联
scroll.config(command = text.yview) #滚动条 关联文本
text.config(yscrollcommand = scroll.set) #文本关联滚动条










win.mainloop()
