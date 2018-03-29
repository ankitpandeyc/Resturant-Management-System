from tkinter import *
import random
import time;

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")
text_Input=StringVar()
operator=""

rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Veg_Meal=StringVar()
NonVeg_Meal=StringVar()
Kababs=StringVar()
SubTotal=StringVar()
Total=StringVar()
Tax=StringVar()
Cost=StringVar()
Drinks=StringVar()
ServiceCharges=StringVar()
Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
  #Time
localtime=time.asctime(time.localtime(time.time()))
  #Info
lb1Info=Label(Tops,font=('arial',50,'bold'),text="Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
lb1Info.grid(row=0,column=0)
lb1Info=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lb1Info.grid(row=1,column=0)
  #Calculator
def btnClick(numbers):
    global operator
    operator=operator +str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
def Ref():
    x=random.randint(12909,99999)
    randomRef=str(x)
    rand.set(randomRef)
    CoF=float(Fries.get())
    CoD=float(Drinks.get())
    CoK=float(Kababs.get())
    CoBurger=float(Burger.get())
    CoVeg_Meal=float(Veg_Meal.get())
    CoN_Veg=float(NonVeg_Meal.get())

    CostofFries=CoF*1.25
    CostofDrinks=CoD*1.1
    CostofKababs=CoK*2.0
    CostofBurger=CoBurger*1.75
    CostofVM=CoVeg_Meal*2.5
    CostofNVM=CoN_Veg*2.75

    CostofMeal="$", str('%.2f' %(CostofVM+CostofNVM+CostofFries+CostofDrinks+CostofKababs+CostofBurger))
    PayTax=((CostofVM+CostofNVM+CostofFries+CostofDrinks+CostofKababs+CostofBurger)*0.75)
    TotalCost=(CostofVM+CostofNVM+CostofFries+CostofDrinks+CostofKababs+CostofBurger)
    Ser_Charges=TotalCost/99
    Service = "$", str('%.2f' % Ser_Charges)
    OverAllCost="$", str('%.2f' % (PayTax +TotalCost +Ser_Charges))
    PaidTax= "$", str('%.2f'% PayTax)

    Ser_Charges.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Veg_Meal.set("")
    NonVeg_Meal.set("")
    Kababs.set("")
    SubTotal.set("")
    Total.set("")
    Tax.set("")
    Cost.set("")
    Drinks.set("")
    Ser_Charges.set("")

        
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

                     #================================================
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=2)
Product=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
Divide=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)

                     #=======================================================
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Veg_Meal=StringVar()
NonVeg_Meal=StringVar()
Kababs=StringVar()
SubTotal=StringVar()
Total=StringVar()
Tax=StringVar()
Cost=StringVar()
Drinks=StringVar()
ServiceCharges=StringVar()
lb1Reference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lb1Reference.grid(row=0,column=0)
textReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
textReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="French Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
textFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
textFries.grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="French Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
textBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
textBurger.grid(row=2,column=1)

lblveg_meal=Label(f1,font=('arial',16,'bold'),text="Veg Meal",bd=16,anchor='w')
lblveg_meal.grid(row=3,column=0)
textveg_meal=Entry(f1,font=('arial',16,'bold'),textvariable=Veg_Meal,bd=10,insertwidth=4,bg="powder blue",justify='right')
textveg_meal.grid(row=3,column=1)

lblnonveg_meal=Label(f1,font=('arial',16,'bold'),text="Non-Veg Meal",bd=16,anchor='w')
lblnonveg_meal.grid(row=4,column=0)
textnonveg_meal=Entry(f1,font=('arial',16,'bold'),textvariable=NonVeg_Meal,bd=10,insertwidth=4,bg="powder blue",justify='right')
textnonveg_meal.grid(row=4,column=1)

lblkababs=Label(f1,font=('arial',16,'bold'),text="Kababs",bd=16,anchor='w')
lblkababs.grid(row=5,column=0)
textkababs=Entry(f1,font=('arial',16,'bold'),textvariable=Kababs,bd=10,insertwidth=4,bg="powder blue",justify='right')
textkababs.grid(row=5,column=1)
                    #=================================Column===================

lb1Drinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lb1Drinks.grid(row=0,column=2)
textDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
textDrinks.grid(row=0,column=3)

lblcost=Label(f1,font=('arial',16,'bold'),text="Cost Of Meal",bd=16,anchor='w')
lblcost.grid(row=1,column=2)
textcost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
textcost.grid(row=1,column=3)

lblServiceCharge=Label(f1,font=('arial',16,'bold'),text="Service Charges",bd=16,anchor='w')
lblServiceCharge.grid(row=2,column=2)
textServiceCharges=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceCharges,bd=10,insertwidth=4,bg="powder blue",justify='right')
textServiceCharges.grid(row=2,column=3)

lblTax=Label(f1,font=('arial',16,'bold'),text="Total Tax",bd=16,anchor='w')
lblTax.grid(row=3,column=2)
textTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
textTax.grid(row=3,column=3)

lblsubTotal=Label(f1,font=('arial',16,'bold'),text="SubTotal",bd=16,anchor='w')
lblsubTotal.grid(row=4,column=2)
textsubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
textsubTotal.grid(row=4,column=3)

lblTotal=Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
textTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
textTotal.grid(row=5,column=3)

                    #=============================Buttons===================

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=4,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=4,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=4,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

