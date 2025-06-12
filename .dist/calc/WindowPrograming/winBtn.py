from tkinter import *
from time import*

nlist=["bear.gif","bee.gif","cupid.gif","dog.gif","dog2.gif","sun.gif","sun2.gif","tractor.gif","unicorn.gif"]
plist=[None]*9
n=0

def cN():
    global n
    n+=1
    if n>8:
        n=0
    photo=PhotoImage(file="gif/"+nlist[n])
    pLabel.configure(image=photo)
    pLabel.image=photo

def cP():
    global n
    n-=1
    if n<0:
        n=8
    photo=PhotoImage(file="gif/"+nlist[n])
    pLabel.configure(image=photo)
    pLabel.image=photo
    
    
window=Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnP=Button(window,text="<< 이전",command=cP)
btnN=Button(window,text="다음>>",command=cN)
Label1=Label(window,text=nlist[n])

photo=PhotoImage(file="gif/"+nlist[0])
pLabel=Label(window,image=photo)

btnP.place(x=250,y=10)
btnN.place(x=400,y=10)
pLabel.place(x=15,y=50)
Label1.place(x=320,y=10)
window.mainloop()