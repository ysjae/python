from tkinter import *
import random

blist=[None]*9
nlist=["bear.gif","bee.gif","cupid.gif","dog.gif","dog2.gif","sun.gif","sun2.gif","tractor.gif","unicorn.gif"]
plist=[None]*9
i,k=0,0
xp,yp=0,0
n=0

random.shuffle(nlist)


window=Tk()
window.geometry("210,210")

for i in range (9):
    plist[i]== PhotoImage(file="C:\\Users\\LG\\Desktop\\python실습\\.dist\\calc\\WindowPrograming\\"+nlist[i])
    blist[i]=Button(window,image=plist[i])

for i in range (3):
    for k in range (3):
        blist[n].place(x=xp,y=yp)
        n+=1
        xp+=70
    xp=0
    yp+=70
    
window.mainloop()