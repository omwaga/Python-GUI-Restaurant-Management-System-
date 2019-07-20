from tkinter import*
import tkinter.messagebox
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
Items_F = Frame(MenuFrame, bg='powder blue', bd = 10)
Items_F.pack(side=TOP)
Drinks_F = Frame(Items_F, bg='powder blue', bd = 10)
Drinks_F.pack(side=LEFT)

Cakes_F = Frame(Items_F, bg='powder blue', bd = 10)
Cakes_F.pack(side=RIGHT)
Cost_F = Frame(MenuFrame, bg='powder blue', bd = 4)
Cost_F.pack(side=BOTTOM)



ReceiptCal_F = Frame(root, bg='powder blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg='powder blue', bd=3,relief=RIDGE, width=300, height=200)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg='cadet blue', bd=3,relief=RIDGE, width=300, height=300)
Receipt_F.pack(side=BOTTOM)


#===================calculator functions==============================================================
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

#===============================================Exit Function======================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


#===================================================Reset the inputs================================
def Reset():
    # ========================================Dinks Reset===================================
    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffeee.set("0")
    E_Cappucino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    # ========================================Cakes Reset================================================
    E_School_Cake.set("0")
    E_Sunny_AO_Cake.set("0")
    E_Jonathan_YO_Cake.set("0")
    E_West_African_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Cake.set("0")
    E_QueenPark_Chocolate_Cake.set("0")

    # ========================================Reset Calculator Variables============================================================
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    Latta.configure(state=DISABLED)
    Espresso.configure(state=DISABLED)
    Iced_Latta.configure(state=DISABLED)
    Vale_Coffee.configure(state=DISABLED)
    Cappuccino.configure(state=DISABLED)
    African_Coffee.configure(state=DISABLED)
    American_Coffee.configure(state=DISABLED)
    Ice_Cappuccino.configure(state=DISABLED)

    SchoolCake.configure(state=DISABLED)
    Sunny_AO_Cake.configure(state=DISABLED)
    Jonathan_YO_Cake.configure(state=DISABLED)
    West_African_Cake.configure(state=DISABLED)
    Lagos_Chocolate_Cake.configure(state=DISABLED)
    Kilburn_Chocolate_Cake.configure(state=DISABLED)
    Carlton_Hill_Cake.configure(state=DISABLED)
    Queen_Park_Cake.configure(state=DISABLED)

    DateofOrder.set("")
    Receipt_Ref.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set(0)

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

#========================================Calculator Variables============================================================
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

#=======================================Functionality buttons variables======================================
DateofOrder = StringVar()
Receipt_Ref= StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

#=====================================Drinks Variables=========================================================
E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffeee = StringVar()
E_Cappucino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

#======================================Cakes Variables=============================================================
E_School_Cake = StringVar()
E_Sunny_AO_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Cake = StringVar()
E_QueenPark_Chocolate_Cake = StringVar()

#========================================Dinks set method===================================
E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffeee.set("0")
E_Cappucino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

#========================================Cakes set Method================================================
E_School_Cake.set("0")
E_Sunny_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Cake.set("0")
E_QueenPark_Chocolate_Cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))#Set Date
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
txtLatta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                 textvariable=E_Latta)
txtLatta.grid(row=0, column=1)
txtEsspresso = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_Espresso)
txtEsspresso.grid(row=1, column=1)
IcedLatta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                  textvariable=E_Iced_Latta)
IcedLatta.grid(row=2, column=1)
ValeCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                   textvariable=E_Vale_Coffeee)
ValeCoffee.grid(row=3, column=1)
txtCappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=E_Cappucino)
txtCappuccino.grid(row=4, column=1)
AfricanCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=E_African_Coffee)
AfricanCoffee.grid(row=5, column=1)
AmericanCoffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=E_American_Coffee)
AmericanCoffee.grid(row=6, column=1)
IceCappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=E_Iced_Cappuccino)
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
txtSchoolCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=E_School_Cake)
txtSchoolCake.grid(row=0, column=1)
txtSunnyCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_Sunny_AO_Cake)
txtSunnyCake.grid(row=1, column=1)
txtJonathanCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                        textvariable=E_Jonathan_YO_Cake)
txtJonathanCake.grid(row=2, column=1)
txtAfricanCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=E_West_African_Cake)
txtAfricanCake.grid(row=3, column=1)
txtLagosCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_Lagos_Chocolate_Cake)
txtLagosCake.grid(row=4, column=1)
txtKilburnCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=E_Kilburn_Chocolate_Cake)
txtKilburnCake.grid(row=5, column=1)
txtCarltonCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=E_Carlton_Hill_Cake)
txtCarltonCake.grid(row=6, column=1)
txtQueenCake = Entry(Cakes_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                     textvariable=E_QueenPark_Chocolate_Cake)
txtQueenCake.grid(row=7, column=1)


#=================================Total Cost================================================================
lblCostofDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text="Cost of Drinks\t  ", bg="powder blue", fg="black")
lblCostofDrinks.grid(row=0, column=0, sticky=W)

txtCostofDrinks = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F, font=('arial', 14, 'bold'), text="Service Charge\t  ", bg="powder blue", fg="black")
lblCostofCakes.grid(row=1, column=0, sticky=W)

txtCostofCakes = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=CostofCakes)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text="Service Charge\t  ", bg="powder blue", fg="black")
lblServiceCharge.grid(row=2, column=0, sticky=W)

txtServiceCharge = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)


#=================================Payment Information=======================================================
lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text="Paid Tax\t  ", bg="powder blue", fg="black")
lblPaidTax.grid(row=0, column=2, sticky=W)

txtPaidTax = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text="Sub Total\t  ", bg="powder blue", fg="black")
lblSubTotal.grid(row=1, column=2, sticky=W)

txtSubTotal = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text="Total Cost\t  ", bg="powder blue", fg="black")
lblTotalCost.grid(row=2, column=2, sticky=W)

txtTotalCost = Entry(Cost_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                   bg="white", justify='right', textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)


#===================================Receipt==================================================================
txtReceipt = Text(Receipt_F, width=46, height=12,bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#===================================buttons===================================================================
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Total",
                  bg="Powder Blue").grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Receipt",
                  bg="Powder Blue").grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Reset",
                  bg="Powder Blue", command=Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'), width=4, text="Exit",
                  bg="Powder Blue", command=iExit).grid(row=0, column=3)
root.mainloop()