from tkinter import *;
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tkinter import messagebox;

win = Tk()
win.title("Bike_Prediction")
icon = PhotoImage(file='C:\ic4.png')
win.iconphoto(False,icon)

win.geometry('1100x750')
win.minsize(1000,750)
win.maxsize(1000,750)
win.configure(bg="#FAFAD2")

dta = pd.read_csv("C:/Users/Admin/bikes.csv");
dta.drop("ID", axis=1, inplace=True)
dta.dropna(inplace=True)
pd.get_dummies(dta['Gender'])
gen = pd.get_dummies(dta['Gender'], drop_first=True)
married = pd.get_dummies(dta["Marital Status"], drop_first=True)
homeOwner = pd.get_dummies(dta["Home Owner"], drop_first=True)
dta = pd.concat([dta, married, gen, homeOwner], axis=1)
dta.drop("Marital Status", axis=1, inplace=True)
dta.drop("Home Owner", axis=1, inplace=True)
dta.drop("Gender", axis=1, inplace=True)
regon = pd.get_dummies(dta['Region'], drop_first=True)
dta.drop("Region",axis=1,inplace=True)
dta = pd.concat([dta, regon], axis=1)
dta["Purchased Bike"] = dta["Purchased Bike"].map({'Yes': 1, 'No': 0})
dta.drop('Commute Distance', axis=1, inplace=True)
occupc = pd.get_dummies(dta['Occupation'], drop_first=True)
dta = pd.concat([occupc, dta], axis=1)
dta.drop('Occupation', axis=1, inplace=True)
dta.drop('Education', axis=1, inplace=True)
dta['Income'] = dta['Income'].astype(int)
dta['Children'] = dta['Children'].astype(int)
dta['Age'] = dta['Age'].astype(int)
dta['Cars'] = dta['Cars'].astype(int)
dta['North America']=dta['North America'].astype(int)
dta['Pacific']=dta['Pacific'].astype(int)
x = dta.drop("Purchased Bike", axis=1)
y = dta['Purchased Bike']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
model = LogisticRegression()
model.fit(x_train, y_train)

lb = Label(win,text="Prediction for whether customer will purchase bike or not ",font=("Britannic", 26, "bold"),fg = 'red',bg='#FFA07A')
lb.pack(fill='x')

income = Label(win,text="Income : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
income.place(x=80,y=75)
enincome = Entry(win,width=25,bd=1,font=('Lucida Bright',20,'bold'))
enincome.place(x=240,y=75,height=40)
enincome.focus()

child = Label(win,text="Children : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
child.place(x=80,y=135)
enchild = Entry(win,width=25,bd=1,font=('Lucida Bright',20,'bold'))
enchild.place(x=240,y=135,height=40)

cars = Label(win,text="Cars : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
cars.place(x=80,y=195)
encars = Entry(win,width=25,bd=1,font=('Lucida Bright',20,'bold'))
encars.place(x=240,y=195,height=40)

age = Label(win,text="Age : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
age.place(x=80,y=255)
enage = Entry(win,width=25,bd=1,font=('Lucida Bright',20,'bold'))
enage.place(x=240,y=255,height=40)

def chs_radio_gen():
    choi_gen = gender.get()
    if(choi_gen==1):
        return 1;
    else:
        return 0;

gen = Label(win,text="Gender : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
gen.place(x=80,y=315)
gender = IntVar()
gen1 = Radiobutton(win,text="male",bg ="#FAFAD2" ,variable = gender , value = 1 , font = ('Arial Rounded MT',18) )
gen1.place(x=300,y=320)
gen2 = Radiobutton(win,text="female",bg ="#FAFAD2" ,variable = gender , value = 0 , font = ('Arial Rounded MT',18) )
gen2.place(x=400,y=320)

def chs_radio_mari():
    choi_mari = marid.get()
    if(choi_mari==1):
        return 0;
    else:
        return 1;

married = Label(win,text="Married : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
married.place(x=80,y=380)
marid = IntVar()
yesmarid = Radiobutton(win,text="Yes",bg ="#FAFAD2" ,variable = marid , value = 1 , font = ('Arial Rounded MT',18) )
yesmarid.place(x=300,y=380)
nomarid = Radiobutton(win,text="No",bg ="#FAFAD2" ,variable = marid , value = 0 , font = ('Arial Rounded MT',18) )
nomarid.place(x=400,y=380)

def chs_radio_own():
    choi_own = own.get()
    if(choi_own==1):
        return 1;
    else:
        return 0;

owner = Label(win,text="Home Owner : ",font=('Arial Rounded MT',23,'bold'),bg="#FAFAD2",fg="#191970")
owner.place(x=80,y=440)
own = IntVar()
yesowner = Radiobutton(win,text="Yes",bg ="#FAFAD2" ,variable = own , value = 1 , font = ('Arial Rounded MT',18) )
yesowner.place(x=300,y=440)
noowner = Radiobutton(win,text="No",bg ="#FAFAD2" ,variable = own , value = 0 , font = ('Arial Rounded MT',18) )
noowner.place(x=400,y=440)


def Chse_reg_paci(com_get1):
    if com_get1 == 'Pacific Region':
        return 1
    else:
         return 0

def Chse_reg_nor(com_get11):
    if com_get11 == 'North America':
        return 1
    else:
        return 0




reglb = Label(win,bg="#FAFAD2",fg="#191970" , text="Region : ",font=('Arial Rounded MT',23,'bold'))
reglb.place(x=80,y=505)
reg = StringVar(win)
region = ttk.Combobox(win,width = 18, font=('Rockwell',15),textvariable = reg)
region['values'] = ('Europe','Pacific Region','North America')
region.place(x=274,y=510);
region.current(0)
win.option_add('*TCombobox*Listbox.font',('Rockwell',15))


def chse_occu_man(get_com2):
       if(get_com2 == 'Management'):
           return 1
       else:
           return 0

def chse_occu_pro(get_com2):
        if (get_com2 == 'Professional Occupation'):
            return 1
        else:
            return 0

def chse_occu_manua(get_com2):
        if (get_com2 == 'Manual'):
            return 1
        else:
            return 0
def chse_occu_skill(get_com2):
        if (get_com2 == 'Skilled Manual'):
            return 1
        else:
            return 0



occub = Label(win,bg="#FAFAD2",fg="#191970" , text="Occupation : ",font=('Arial Rounded MT',23,'bold'))
occub.place(x=80,y=570)
occ = StringVar()
occupson = ttk.Combobox(win,width=18 , font=('Rockwell',15),textvariable= occ)
occupson['values']=('Management','Manual','Professional Occupation','Skilled Manual','Clerical')
occupson.place(x=274,y=580)
occupson.current(0)
win.option_add('*TCombobox*Listbox.font',('Rockwell',15))

def calc():
    if str(enincome.get()) == "":
        messagebox.showwarning("Error","plz, Enter your Income")
        enincome.focus()
        return
    if str(enchild.get()) == "":
        messagebox.showwarning("Error","plz, Enter your No. of child")
        enchild.focus()
        return
    if str(encars.get()) == "":
        messagebox.showwarning("Error","plz, Enter your No. of cars")
        encars.focus()
        return
    if str(enage.get()) == "":
        messagebox.showwarning("Error","plz, Enter your Age")
        enage.focus()
        return

    x = model.predict([[chse_occu_man(occ.get()), chse_occu_manua(occ.get()), chse_occu_pro(occ.get()),
                        chse_occu_skill(occ.get()), enincome.get(), enchild.get(), encars.get(), enage.get(),
                        chs_radio_mari(), chs_radio_gen(), chs_radio_own(), Chse_reg_nor(reg.get()),
                        Chse_reg_paci(reg.get())]])
    if x[0] == 0:
        res_zero = Label(win,text=" NO , Customer will \n not purchase Bike",bg="#FAFAD2",fg="red",font=("Verdana",20,'bold'))
        res_zero.place(x=630,y=470)
    if x[0] == 1:
        res_one = Label(win,text=" YES , Customer will \n purchase Bike",bg="#FAFAD2",fg="red",font=("Verdana",20,'bold'))
        res_one.place(x=630,y=470)

prid = Button(win,text = "Predict",bg='#a3c1ad',fg="#d53515",font=('Cooper',20,'bold'),command = calc)
prid.place(x=150,y=642)

def clear_value():
    enincome.delete(0,END)
    enchild.delete(0, END)
    enage.delete(0, END)
    encars.delete(0, END)
    enincome.focus()

clr = Button(win,text = "Clear",bg='#a3c1ad',fg="#d53515",font=('Cooper',20,'bold'),command=clear_value)
clr.place(x=360,y=642)

h1_can = Canvas(win,width = 345 , height = 5 , background = '#FFA812')
h1_can.place(x=610,y=455)

h2_can = Canvas(win,width = 345, height = 5 , background = '#FFA812')
h2_can.place(x=610,y=570)

v1_can = Canvas(win,width = 5 , height = 120 , background = '#FFA812')
v1_can.place(x=610,y=455)

v2_can = Canvas(win,width = 5 , height = 120 , background = '#FFA812')
v2_can.place(x=950,y=455)


win.mainloop()

