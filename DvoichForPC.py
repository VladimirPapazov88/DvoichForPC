from tkinter import *

def encode(k):
    global answ
    answ = str()
    if k // 2 != 0:
        encode(k // 2)
    csl = k % 2
    answ+=str(csl)
    # print(csl, sep="", end="")
        
def decode():
    k = int(txt.get())
    leng = len(str(k))
    kstr = ''.join(reversed(str(k)))
    answ = 0
    for x in range(0, leng):
        if (kstr!="0"):
            answ = (int(kstr[x])*(2**x))+answ
    lbl.configure(text=answ)

def clcencode():
    text = txt.get()
    encode(int(text))
    lbl.configure(text=answ)
    

window = Tk()
window.title("Dvoich for PC by VladimirPapazov88")
window.geometry('1500x100')

txt = Entry(window, width=17, font=("Arial", 24))
txt.grid(column=0, row=0)

btn = Button(window, text="encode", command=clcencode)
btn.grid(column=1, row=0)

btn = Button(window, text="decode", command=decode)
btn.grid(column=2, row=0)

lbl = Label(window, text="answ", font=("ArialBold", 24))
lbl.grid(column=3, row=0)

a = input("Press q to exit\n")




    
