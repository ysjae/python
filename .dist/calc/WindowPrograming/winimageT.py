from tkinter import *
window=Tk()

window.title("냥이")
photo = PhotoImage(file="C:\\Users\\LG\\Desktop\\python실습\\.dist\\calc\\WindowPrograming\\cass.gif")
photo2 = PhotoImage(file="C:\\Users\\LG\\Desktop\\python실습\\.dist\\calc\\WindowPrograming\\kass.gif")
label1=Label(window,image=photo)
label2=Label(window,image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
window.mainloop()