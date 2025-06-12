from tkinter import*
from tkinter import messagebox

def KeyE(event):
    messagebox.showinfo("키보드 이벤트","눌린키:"+chr(event.keycode))

window=Tk()

window.bind("<Shift-Up>",KeyE)
window.bind("<Shift-Down>",KeyE)
window.bind("<Shift-Left>",KeyE)
window.bind("<Shift-Right>",KeyE)

window.mainloop()