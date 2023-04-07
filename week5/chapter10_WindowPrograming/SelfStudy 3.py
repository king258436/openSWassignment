from tkinter import *
from time import *

fnameList = ["a.gif", "b.gif", "c.gif",
            "d.gif", "e.gif", "f.gif",
            "g.gif", "h.gif", "j.gif"]
photoList = [None]*9
num = 0


def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
        photo = PhotoImage(
            file="/Users/wonsick/Documents/ImageFile/"+fnameList[num])
        pLabel.configure(image=photo)
        tLabel.configure(text=fnameList[num])
        pLabel.image = photo


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(
        file="/Users/wonsick/Documents/ImageFile/"+fnameList[num])
    pLabel.configure(image=photo)
    tLabel.configure(text=fnameList[num])
    pLabel.image = photo



window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="/Users/wonsick/Documents/ImageFile/" + fnameList[0])
tLabel = Label(window, text=fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
tLabel.place(x=325,y=10)
pLabel.place(x=15, y=50)

window.mainloop()
