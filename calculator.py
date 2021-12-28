from tkinter import *
from tkinter import font

base = Tk()
base.title("Calculator")
base.geometry('392x500+30+40')
base.resizable(0,0)
base.configure(background='white')

#Display label
label = Label(base,height=7, width=41,anchor= 'se')
label.place(x=30,y=30)
company_label =Label(base,text='Masio', bd=5, relief='groove', height=3, width=19,  bg='white',fg='red')
company_label.place(x=30,y=172)

#glabal variable
num =''

# Functions
def display(number):

    global num
    num = num+str(number)
    label['text'] = num


def equals():
        try:
            global num
            result= eval(num)
            label['text'] = result
        except:
            label['text'] = 'Error'
def clear():
    global num
    num = ''
    label['text']=num
def backspace():
    global num
    num = num[:-1]
    label['text']=num

#adding buttons

times15 = font.Font(family='times', size=15, weight='bold')
btn1= Button(text=1, bd=1, height=2, width=5, font=times15,bg='#A9A9A9',command=lambda: display(1))
btn2 = Button(text=2, bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display(2))
btn3 = Button(text=3, bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display(3))
btn4= Button(text=4, bd=1, height=2, width=5, font=times15,bg='#A9A9A9',command=lambda: display(4))
btn5 = Button(text=5, bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display(5))
btn6 = Button(text=6, bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display(6))
btn7= Button(text=7, bd=1, height=2, width=5, font=times15,bg='#A9A9A9',command=lambda: display(7))
btn8 = Button(text=8, bd=1, height=2, width=5,font=times15, bg='#A9A9A9',command=lambda: display(8))
btn9 = Button(text=9, bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display(9))
btn0= Button(text=0, bd=1, height=2, width=5, font=times15,bg='#A9A9A9',command=lambda: display(0))
btndot = Button(text='.', bd=1, height=2, width=5,font=times15,bg='#A9A9A9',command=lambda: display('.'))
btnequal = Button(text='=', bd=1, height=2, width=5,font=times15, bg='blue', fg='white',command=equals)
btnClear = Button(text='AC', bd=1, height=2, width=5,font=times15,bg='#D3D3D3',command=clear)

btnback = Button(text='c', bd=1, height=2, width=5,font=times15,command=backspace)
btndiv = Button(text='/', bd=1, height=2, width=5,font=times15,command=lambda: display('/'))
btnmult = Button(text='x', bd=1, height=2, width=5,font=times15,command=lambda: display('*'))
btnsub = Button(text='-', bd=1, height=2, width=5,font=times15,command=lambda: display('-'))
btnsum = Button(text='+', bd=1, height=2, width=5,font=times15,bg='orange',command=lambda: display('+'))
#button alignment
btn1.place(x=30,y=358)
btn2.place(x=115,y=358)
btn3.place(x=200,y=358)
btn4.place(x=30,y=296)
btn5.place(x=115,y=296)
btn6.place(x=200,y=296)
btn7.place(x=30,y=234)
btn8.place(x=115,y=234)
btn9.place(x=200,y=234)
btn0.place(x=30,y=420)
btndot.place(x=115,y=420)
btnequal.place(x=200,y=420)
btnClear.place(x=200,y=172)
btnback.place(x=285,y=172)
btndiv.place(x=285,y=358)
btnmult.place(x=285,y=296)
btnsub.place(x=285,y=234)
btnsum.place(x=285,y=420)

base.mainloop()
