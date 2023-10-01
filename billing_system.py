from tkinter import *

root = Tk()
root.geometry("1000x500")  
root.title("Billing Management System")
root.resizable(False, False)

def Reset():
    entry_samosa.delete(0, END)
    entry_Cookies.delete(0, END)
    entry_Tea.delete(0, END)
    entry_Coffee.delete(0, END)
    entry_Juice.delete(0, END)
    entry_Pancake.delete(0, END)
    entry_Eggs.delete(0, END)

def Total():
    try:a1=int(samosa.get())    
    except: a1=0
    
    try:a2=int(cookies.get())    
    except: a2=0
    
    try:a3=int(Tea.get())    
    except: a3=0
    
    try:a4=int(coffee.get())    
    except: a4=0
   
    try:a5=int(juice.get())    
    except: a5=0
    
    try:a6=int(pancake.get())    
    except: a6=0
   
    try:a7=int(eggs.get())    
    except: a7=0

    # define the cost of each item per quantity
    c1=25*a1
    c2=60*a2
    c3=50*a3
    c4=60*a4
    c5=110*a5
    c6=120*a6
    c7=25*a7

    lbl_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=50)

    entry_total=Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.", str('%.2f' %totalcost)
    Total_bill.set(string_bill)


Label (text="Billing Management System", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

## Menu section
f=Frame(root, bg="Mint Cream", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=("Georgia", 40, "bold"), fg="black", bg="Mint Cream").place(x=80, y=0)
Label(f, font=("Georgia", 15, 'bold'), text="samosa ........Rs.25/piece", fg="black", bg="Mint Cream").place(x=10, y=80)
Label(f, font=("Georgia", 15, 'bold'), text="Cookies ........Rs.60/plate", fg="black", bg="Mint Cream").place(x=10, y=110)
Label(f, font=("Georgia", 15, 'bold'), text="Tea ........Rs.50/cup", fg="black", bg="Mint Cream").place(x=10, y=140)
Label(f, font=("Georgia", 15, 'bold'), text="Coffee ........Rs.60/cup", fg="black", bg="Mint Cream").place(x=10, y=170)
Label(f, font=("Georgia", 15, 'bold'), text="Juice ........Rs.110/glass", fg="black", bg="Mint Cream").place(x=10, y=200)
Label(f, font=("Georgia", 15, 'bold'), text="Pancakes ........Rs.120/piece", fg="black", bg="Mint Cream").place(x=10, y=230)
Label(f, font=("Georgia", 15, 'bold'), text="Eggs ........Rs.25/piece", fg="black", bg="Mint Cream").place(x=10, y=260)


# Bill
f2=Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
Bill.place(x=120, y=10)

## For Entry

f1=Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

samosa=StringVar()
cookies=StringVar()
Tea=StringVar()
coffee=StringVar()
juice=StringVar()
pancake=StringVar()
eggs=StringVar()
Total_bill=StringVar()

## Label
lbl_samosa=Label(f1, font=("aria", 20, 'bold'), text="Samosa", width=12, fg="blue4")
lbl_Cookies=Label(f1, font=("aria", 20, 'bold'), text="Cookies", width=12, fg="blue4")
lbl_Tea=Label(f1, font=("aria", 20, 'bold'), text="Tea", width=12, fg="blue4")
lbl_Coffee=Label(f1, font=("aria", 20, 'bold'), text="Coffee", width=12, fg="blue4")
lbl_Juice=Label(f1, font=("aria", 20, 'bold'), text="Juice", width=12, fg="blue4")
lbl_Pancake=Label(f1, font=("aria", 20, 'bold'), text="Pancake", width=12, fg="blue4")
lbl_Eggs=Label(f1, font=("aria", 20, 'bold'), text="Eggs", width=12, fg="blue4")
lbl_samosa.grid(row=1, column=0)
lbl_Cookies.grid(row=2, column=0)
lbl_Tea.grid(row=3, column=0)
lbl_Coffee.grid(row=4, column=0)
lbl_Juice.grid(row=5, column=0)
lbl_Pancake.grid(row=6, column=0)
lbl_Eggs.grid(row=7, column=0)

# Entry
entry_samosa=Entry(f1, font=("aria", 20, 'bold'), textvariable=samosa, bd=6, width=8, bg="lightpink")
entry_Cookies=Entry(f1, font=("aria", 20, 'bold'), textvariable=cookies, bd=6, width=8, bg="lightpink")
entry_Tea=Entry(f1, font=("aria", 20, 'bold'), textvariable=Tea, bd=6, width=8, bg="lightpink")
entry_Coffee=Entry(f1, font=("aria", 20, 'bold'), textvariable=coffee, bd=6, width=8, bg="lightpink")
entry_Juice=Entry(f1, font=("aria", 20, 'bold'), textvariable=juice, bd=6, width=8, bg="lightpink")
entry_Pancake=Entry(f1, font=("aria", 20, 'bold'), textvariable=pancake, bd=6, width=8, bg="lightpink")
entry_Eggs=Entry(f1, font=("aria", 20, 'bold'), textvariable=eggs, bd=6, width=8, bg="lightpink")

entry_samosa.grid(row=1, column=1)
entry_Cookies.grid(row=2, column=1)
entry_Tea.grid(row=3, column=1)
entry_Coffee.grid(row=4, column=1)
entry_Juice.grid(row=5, column=1)
entry_Pancake.grid(row=6, column=1)
entry_Eggs.grid(row=7, column=1)

# buttons

btn_reset=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset",command=Reset)
btn_reset.grid(row=8, column=0)


btn_total=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Total",command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()
