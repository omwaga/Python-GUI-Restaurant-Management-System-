from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")
root.configure(background="Cadet Blue")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

MenuFrame = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
MenuFrame.pack(side=LEFT)


#Getting the local machine time
localtime = time.asctime(time.localtime(time.time()))

#information
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System",bg="cadet blue", fg="Cornsilk", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, bg="cadet blue", fg="Cornsilk", bd=10, anchor='w')
lblTime.grid(row=1, column=0)


#===========Menu Frame=========================

Drinks_F = Frame(MenuFrame, bg='powder blue', bd = 10)
Drinks_F.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg='powder blue', bd = 4)
Cost_F.pack(side=BOTTOM)

Cakes_F = Frame(MenuFrame, bg='powder blue', bd = 10)
Cakes_F.pack(side=RIGHT)
Cost_F = Frame(MenuFrame, bg='powder blue', bd = 4)
Cost_F.pack(side=LEFT)



ReceiptCal_F = Frame(root, bg='powder blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg='powder blue', bd=3,relief=RIDGE, width=300, height=200)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg='cadet blue', bd=3,relief=RIDGE, width=300, height=300)
Receipt_F.pack(side=BOTTOM)


#===================calculator==============================================================
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


txtDisplay = Entry(Cal_F, font=('arial', 10, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn9 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="9", bg="powder blue", command=lambda: btnclick(9)).grid(row=2,column=2)
btn8 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="8", bg="powder blue", command=lambda: btnclick(8)).grid(row=2,column=1)
btn7 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="7", bg="powder blue", command=lambda: btnclick(7)).grid(row=2,column=0)
btn6 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="6", bg="powder blue", command=lambda: btnclick(6)).grid(row=3,column=0)
btn5 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="5", bg="powder blue", command=lambda: btnclick(5)).grid(row=3,column=1)
btn4 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="4", bg="powder blue", command=lambda: btnclick(4)).grid(row=3,column=2)
btn3 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="3", bg="powder blue", command=lambda: btnclick(3)).grid(row=4,column=0)
btn2 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="2", bg="powder blue", command=lambda: btnclick(2)).grid(row=4,column=1)
btn1 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="1", bg="powder blue", command=lambda: btnclick(1)).grid(row=4,column=2)
btn0 = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="0", bg="powder blue", command=lambda: btnclick(0)).grid(row=5,column=0)

btnAddition = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="+", bg="powder blue", command=lambda: btnclick("+")).grid(row=2, column=3)
btnSubtraction = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="-", bg="powder blue", command=lambda: btnclick("-")).grid(row=3, column=3)
btnMultiplication = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="*", bg="powder blue", command=lambda: btnclick("*")).grid(row=4, column=3)
btnDivision = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="/", bg="powder blue", command=lambda: btnclick("/")).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="=", bg="powder blue", command=lambda : btnequalsinput()).grid(row=5, column=2)
btnClear = Button(Cal_F, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'),
            text="CLEAR", bg="powder blue", command=lambda : btncleardisplay()).grid(row=5, column=3)


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16= IntVar()

#===================Drinks==========================================================================================
Latta = Checkbutton(Drinks_F, text='Latta', variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=0, sticky=W)
Espresso = Checkbutton(Drinks_F, text='Espresso', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=1, sticky=W)
Iced_Latta = Checkbutton(Drinks_F, text='Iced Latta', variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=2, sticky=W)
Vale_Coffee = Checkbutton(Drinks_F, text='Vale Coffee', variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=3, sticky=W)
Cappuccino = Checkbutton(Drinks_F, text='Cappuccino', variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=4, sticky=W)
African_Coffee = Checkbutton(Drinks_F, text='African Coffee', variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=5, sticky=W)
American_Coffee = Checkbutton(Drinks_F, text='American Coffee', variable=var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=6, sticky=W)
Ice_Cappuccino = Checkbutton(Drinks_F, text='Iced Cappuccino', variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=7, sticky=W)


#==================================Entry for Drinks==========================================================
txtLatta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtLatta.grid(row=0, column=1)
txtEsspresso = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtEsspresso.grid(row=1, column=1)
IcedLatta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
IcedLatta.grid(row=2, column=1)
ValeCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
ValeCoffee.grid(row=3, column=1)
txtCappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtCappuccino.grid(row=4, column=1)
AfricanCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
AfricanCoffee.grid(row=5, column=1)
AmericanCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
AmericanCoffee.grid(row=6, column=1)
IceCappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
IceCappuccino.grid(row=7, column=1)

#======================================cakes=========================================================================================
SchoolCake = Checkbutton(Cakes_F, text='School Cake\t\t\t', variable=var9, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=0, sticky=W)
Sunny_AO_Cake = Checkbutton(Cakes_F, text='Sunday O Cake', variable=var10, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=1, sticky=W)
Jonathan_YO_Cake = Checkbutton(Cakes_F, text='Jonathan O Cake', variable=var11, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=2, sticky=W)
West_African_Cake = Checkbutton(Cakes_F, text='West African Cake', variable=var12, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=3, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(Cakes_F, text='Lagos Chocolate Cake', variable=var13, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=4, sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(Cakes_F, text='Kilburn Chocolate Cake', variable=var14, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=5, sticky=W)
Carlton_Hill_Cake = Checkbutton(Cakes_F, text='Carlton Hill Chocolate Cake', variable=var15, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=6, sticky=W)
Queen_Park_Cake = Checkbutton(Cakes_F, text='Queens Park Chocolate Cake', variable=var16, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    bg="powder blue").grid(row=7, sticky=W)


#==================================Entry for Cakes==========================================================
txtSchoolCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtSchoolCake.grid(row=0, column=1)
txtSunnyCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtSunnyCake.grid(row=1, column=1)
txtJonathanCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtJonathanCake.grid(row=2, column=1)
txtAfricanCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtAfricanCake.grid(row=3, column=1)
txtLagosCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtLagosCake.grid(row=4, column=1)
txtKilburnCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtKilburnCake.grid(row=5, column=1)
txtCarltonCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtCarltonCake.grid(row=6, column=1)
txtQueenCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
txtQueenCake.grid(row=7, column=1)

#===================================Receipt==================================================================
txtReceipt = Text(Receipt_F, width=46, height=12,bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#===================================buttons===================================================================
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Total",
                  bg="Powder Blue").grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Receipt",
                  bg="Powder Blue").grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Reset",
                  bg="Powder Blue").grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Exit",
                  bg="Powder Blue").grid(row=0, column=3)
root.mainloop()