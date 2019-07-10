from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

Frame1 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
Frame1.pack(side=LEFT)

Frame2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
Frame2.pack(side=RIGHT)

#Getting the local machine time
localtime = time.asctime(time.localtime(time.time()))

#information
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblTime.grid(row=1, column=0)

#calculator


def btnclick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)
def btncleardisplay():
    global operator
    operator=""
    text_Input.set("")
def btnequalsinput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

txtDisplay = Entry(Frame2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)


btn9 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="9", bg="powder blue", command=lambda: btnclick(9)).grid(row=2,column=2)
btn8 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="8", bg="powder blue", command=lambda: btnclick(8)).grid(row=2,column=1)
btn7 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="7", bg="powder blue", command=lambda: btnclick(7)).grid(row=2,column=0)
btn6 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="6", bg="powder blue", command=lambda: btnclick(6)).grid(row=3,column=0)
btn5 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="5", bg="powder blue", command=lambda: btnclick(5)).grid(row=3,column=1)
btn4 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="4", bg="powder blue", command=lambda: btnclick(4)).grid(row=3,column=2)
btn3 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="3", bg="powder blue", command=lambda: btnclick(3)).grid(row=4,column=0)
btn2 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="2", bg="powder blue", command=lambda: btnclick(2)).grid(row=4,column=1)
btn1 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="1", bg="powder blue", command=lambda: btnclick(1)).grid(row=4,column=2)
btn0 = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="0", bg="powder blue", command=lambda: btnclick(0)).grid(row=5,column=0)

btnAddition = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="+", bg="powder blue", command=lambda: btnclick("+")).grid(row=5, column=1)
btnSubtraction = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="-", bg="powder blue", command=lambda: btnclick("-")).grid(row=5, column=2)
btnMultiplication = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="*", bg="powder blue", command=lambda: btnclick("*")).grid(row=6, column=0)
btnDivision = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="/", bg="powder blue", command=lambda: btnclick("/")).grid(row=6, column=1)
btnEquals = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="=", bg="powder blue", command=lambda : btnequalsinput()).grid(row=7, column=0)
btnClear = Button(Frame2, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="CLEAR", bg="powder blue", command=lambda : btncleardisplay()).grid(row=7, column=1)
root.mainloop()