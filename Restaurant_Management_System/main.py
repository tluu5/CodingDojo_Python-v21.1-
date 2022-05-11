from tkinter import *
from tkinter import font

root = Tk()
root.geometry('1270x690+0+0')
root.title('Restaurant Management System')
root.config(bg='firebrick4')
topFrame=Frame(root,bd=10,relief=RIDGE, bg='firebrick4')
topFrame.pack(side=TOP)
labelTitle=Label(topFrame, text='Restaurant Management System', font=('arial', 30, 'bold'), fg='yellow', bd=9, bg='red4', width=51)
labelTitle.grid(row=0, column=0)

menuFrame=Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame, bd=4, relief=RIDGE, bg='firebrick4', pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root, bd=15, relief=RIDGE, bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame, bd=1, relief=RIDGE, bg='red4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame, bd=4, relief=RIDGE, bg='red4')
receiptFrame.pack()

buttonFrame=Frame(rightFrame, bd=3, relief=RIDGE, bg='red4')
buttonFrame.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()

e_China_Pearl_Egg_Roll=StringVar()
e_Vegetable_Egg_Roll=StringVar()
e_Egg_Rolls=StringVar()
e_Crab_Rangoon=StringVar()
e_Fried_Shrimp=StringVar()
e_BBQ_Rib=StringVar()
e_BBQ_Porks=StringVar()
e_Chicken_Teriyaki=StringVar()
e_Beef_Teriyaki=StringVar()

e_China_Pearl_Egg_Roll.set('0')
e_Vegetable_Egg_Roll.set('0')
e_Egg_Rolls.set('0')
e_Crab_Rangoon.set('0')
e_Fried_Shrimp.set('0')
e_BBQ_Rib.set('0')
e_BBQ_Porks.set('0')
e_Chicken_Teriyaki.set('0')
e_Beef_Teriyaki.set('0')

e_Mango_Smoothies=StringVar()
e_Pineapple_Smoothies=StringVar()
e_Watermelon_Smoothies=StringVar()
e_Strawberry_Smoothies=StringVar()
e_Banana_Smoothies=StringVar()
e_Coke=StringVar()
e_Diet_Coke=StringVar()
e_Pepsi=StringVar()
e_Diet_Pepsi=StringVar()

e_Mango_Smoothies.set('0')
e_Pineapple_Smoothies.set('0')
e_Watermelon_Smoothies.set('0')
e_Strawberry_Smoothies.set('0')
e_Banana_Smoothies.set('0')
e_Coke.set('0')
e_Diet_Coke.set('0')
e_Pepsi.set('0')
e_Diet_Pepsi.set('0')

e_Oreo_Cake=StringVar()
e_Kitkat_Cake=StringVar()
e_Vanilla_Cake=StringVar()
e_Apple_Cake=StringVar()
e_Blackforest_Cake=StringVar()
e_Banana_Cake=StringVar()
e_Brownie_Cake=StringVar()
e_Carrot_Cake=StringVar()
e_Chocolate_Cake=StringVar()

e_Oreo_Cake.set('0')
e_Kitkat_Cake.set('0')
e_Vanilla_Cake.set('0')
e_Apple_Cake.set('0')
e_Blackforest_Cake.set('0')
e_Banana_Cake.set('0')
e_Brownie_Cake.set('0')
e_Carrot_Cake.set('0')
e_Chocolate_Cake.set('0')

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

China_Pearl_Egg_Roll=Checkbutton(foodFrame, text='China Pearl\'s Egg Roll', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1)
China_Pearl_Egg_Roll.grid(row=0,column=0, sticky=W)

Vegetable_Egg_Roll=Checkbutton(foodFrame, text='Vegetable Egg Roll', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2)
Vegetable_Egg_Roll.grid(row=1,column=0, sticky=W)

Egg_Rolls=Checkbutton(foodFrame, text='Egg Rolls', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3)
Egg_Rolls.grid(row=2,column=0, sticky=W)

Crab_Rangoon=Checkbutton(foodFrame, text='Crab Rangoon(8)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4)
Crab_Rangoon.grid(row=3,column=0, sticky=W)

Fried_Shrimp=Checkbutton(foodFrame, text='Fried Shrimp(8)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5)
Fried_Shrimp.grid(row=4,column=0, sticky=W)

BBQ_Ribs=Checkbutton(foodFrame, text='B.B.Q Ribs(6)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6)
BBQ_Ribs.grid(row=5,column=0, sticky=W)

BBQ_Porks=Checkbutton(foodFrame, text='B.B.Q Porks(6)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7)
BBQ_Porks.grid(row=6,column=0, sticky=W)

Chicken_Teriyaki=Checkbutton(foodFrame, text='Chicken Teriyaki(6)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8)
Chicken_Teriyaki.grid(row=7,column=0, sticky=W)

Beef_Teriyaki=Checkbutton(foodFrame, text='Beef Teriyaki(6)', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9)
Beef_Teriyaki.grid(row=8,column=0, sticky=W)

textChina_Pearl_Egg_Roll=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_China_Pearl_Egg_Roll)
textChina_Pearl_Egg_Roll.grid(row=0,column=1)

textVegetable_Egg_Roll=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Vegetable_Egg_Roll)
textVegetable_Egg_Roll.grid(row=1,column=1)

textEgg_Rolls=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Egg_Rolls)
textEgg_Rolls.grid(row=2,column=1)

textCrab_Rangoon=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Crab_Rangoon)
textCrab_Rangoon.grid(row=3,column=1)

textFried_Shrimp=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Fried_Shrimp)
textFried_Shrimp.grid(row=4,column=1)

textBBQ_Rib=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_BBQ_Rib)
textBBQ_Rib.grid(row=5,column=1)

textBBQ_Porks=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_BBQ_Porks)
textBBQ_Porks.grid(row=6,column=1)

textChicken_Teriyaki=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Chicken_Teriyaki)
textChicken_Teriyaki.grid(row=7,column=1)

textBeef_Teriyaki=Entry(foodFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Beef_Teriyaki)
textBeef_Teriyaki.grid(row=8,column=1)

Mango_Smoothies=Checkbutton(drinksFrame, text='Mango Smoothies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var17)
Mango_Smoothies.grid(row=0,column=0, sticky=W)

Pineapple_Smoothies=Checkbutton(drinksFrame, text='Pineapple Smoothies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var18)
Pineapple_Smoothies.grid(row=1,column=0, sticky=W)

Watermelon_Smoothies=Checkbutton(drinksFrame, text='Watermelon Smoothies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19)
Watermelon_Smoothies.grid(row=2,column=0, sticky=W)

Strawberry_Smoothies=Checkbutton(drinksFrame, text='Strawberry Smoothies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20)
Strawberry_Smoothies.grid(row=3,column=0, sticky=W)

Banana_Smoothies=Checkbutton(drinksFrame, text='Banana Smoothies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21)
Banana_Smoothies.grid(row=4,column=0, sticky=W)

Coke=Checkbutton(drinksFrame, text='Coke', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22)
Coke.grid(row=5,column=0, sticky=W)

Diet_Coke=Checkbutton(drinksFrame, text='Diet Coke', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23)
Diet_Coke.grid(row=6,column=0, sticky=W)

Pepsi=Checkbutton(drinksFrame, text='Pepsi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24)
Pepsi.grid(row=7,column=0, sticky=W)

Diet_Pepsi=Checkbutton(drinksFrame, text='Diet Pepsi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var25)
Diet_Pepsi.grid(row=8,column=0, sticky=W)

textMango_Smoothies=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Mango_Smoothies)
textMango_Smoothies.grid(row=0,column=1)

textPineapple_Smoothies=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Pineapple_Smoothies)
textPineapple_Smoothies.grid(row=1,column=1)

textWatermelon_Smoothies=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Watermelon_Smoothies)
textWatermelon_Smoothies.grid(row=2,column=1)

textStrawberry_Smoothies=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Strawberry_Smoothies)
textStrawberry_Smoothies.grid(row=3,column=1)

textBanana_Smoothies=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Banana_Smoothies)
textBanana_Smoothies.grid(row=4,column=1)

textCoke=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Coke)
textCoke.grid(row=5,column=1)

textDiet_Coke=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Diet_Coke)
textDiet_Coke.grid(row=6,column=1)

textPepsi=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Pepsi)
textPepsi.grid(row=7,column=1)

textDiet_Pepsi=Entry(drinksFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Diet_Pepsi)
textDiet_Pepsi.grid(row=8,column=1)

Oreo_Cake=Checkbutton(cakesFrame, text='Oreo Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var30)
Oreo_Cake.grid(row=0,column=0, sticky=W)

Apple_Cake=Checkbutton(cakesFrame, text='Apple Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var31)
Apple_Cake.grid(row=1,column=0, sticky=W)

Kitkat_Cake=Checkbutton(cakesFrame, text='Kitkat Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var32)
Kitkat_Cake.grid(row=2,column=0, sticky=W)

Vanilla_Cake=Checkbutton(cakesFrame, text='Vanilla Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var33)
Vanilla_Cake.grid(row=3,column=0, sticky=W)

Banana_Cake=Checkbutton(cakesFrame, text='Banana Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var34)
Banana_Cake.grid(row=4,column=0, sticky=W)

Brownie_Cake=Checkbutton(cakesFrame, text='Brownie Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var35)
Brownie_Cake.grid(row=5,column=0, sticky=W)

Carrot_Cake=Checkbutton(cakesFrame, text='Carrot Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var36)
Carrot_Cake.grid(row=6,column=0, sticky=W)

Chocolate_Cake=Checkbutton(cakesFrame, text='Chocolate Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var37)
Chocolate_Cake.grid(row=7,column=0, sticky=W)

Blackforest_Cake=Checkbutton(cakesFrame, text='Blackforest Cake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var38)
Blackforest_Cake.grid(row=8,column=0, sticky=W)

textOreo_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Oreo_Cake)
textOreo_Cake.grid(row=0,column=1)

textKitkat_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Kitkat_Cake)
textKitkat_Cake.grid(row=1,column=1)

textVanilla_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Vanilla_Cake)
textVanilla_Cake.grid(row=2,column=1)

textApple_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Apple_Cake)
textApple_Cake.grid(row=3,column=1)

textBlackforest_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Blackforest_Cake)
textBlackforest_Cake.grid(row=4,column=1)

textBanana_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Banana_Cake)
textBanana_Cake.grid(row=5,column=1)

textBrownie_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Brownie_Cake)
textBrownie_Cake.grid(row=6,column=1)

textCarrot_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Carrot_Cake)
textCarrot_Cake.grid(row=7,column=1)

textChocolate_Cake=Entry(cakesFrame,font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Chocolate_Cake)
textChocolate_Cake.grid(row=8,column=1)

labelCostofFood=Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1, padx=41)

labelCostofDrink=Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofDrink.grid(row=1,column=0)

textCostofDrink=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=costofdrinksvar)
textCostofDrink.grid(row=1,column=1, padx=41)

labelCostofCake=Label(costFrame, text='Cost of Cakes', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofCake.grid(row=2,column=0)

textCostofCake=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=costofcakesvar)
textCostofCake.grid(row=2,column=1, padx=41)

labelSubtotal=Label(costFrame, text='Subtotal', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3, padx=41)

labelServiceTax=Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelServiceTax.grid(row=1,column=2)

textSerivceTax=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=servicetaxvar)
textSerivceTax.grid(row=1,column=3, padx=41)

labelTotalCost=Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3, padx=41)

buttonTotal=Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5)
buttonReset.grid(row=0,column=4)

textReceipt=Text(receiptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0,column=0)

calculatorField=Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=4)
calculatorField.grid(row=0,column=0, columnspan=4)

button7=Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=4)
button7.grid(row=1,column=0)

button8=Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=4)
button8.grid(row=1,column=1)

button9=Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=4)
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=4)
buttonPlus.grid(row=1,column=3)

root.mainloop()