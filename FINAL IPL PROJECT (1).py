from tkinter import*
from tkinter import messagebox,ttk
import random
import tkinter as tk


root=Tk()
root.title('CONTIX ticket seller')
root.geometry('1280x720')
root.resizable(width=False, height=False)
bg_color='#9d0000'

CONCERT = ['BlackPink','Twice','Justin Sesbreño','JA Torio', 'JP entertainment','Kim boksoju','Bebe Em','Aly Santiago']
BOX=['VIP','Backstage','Lower Box','Upper Box','Economy']

dict={	'BlackPink':2000,
        'Twice':2000,
        'Justin Sesbreño':5000,
        'JA Torio':5000,
        'JP entertainment':5000,
        'Kim boksoju':5000,
        'Bebe Em':5000,
		'Aly Santiago':5000,
}
dict2={
        'VIP':5,
        'Backstage': 8,
        'Lower Box': 4,
        'Upper Box': 3,
        'Economy': 2,
        
}
#variables--------------------------------------------------------------------------------------
person=IntVar()
c_name=StringVar()
c_phone=StringVar()
ticket_no=StringVar()
#Frames----------------------------------------------------------------------------------------

def verify():
    global dis, diss
    a = combo_s.get()
    b = combo_d.get()
    p = person.get()
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
            messagebox.showerror('Error','Phone number should be an integer')
            return
    else:
        messagebox.showerror("Error", "User's Info detail are needed")
        return
    if a in dict:
        dis=dict[a]
    if b in dict2:
        diss=dict2[b]
    else:
        messagebox.showwarning('Warning ', 'Please choose a concert!')
        return
    messagebox.showinfo('Verified','Successfully Verified')

def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END,f"\n {55*'*'}")
        textarea.insert(END, f"\n\n Concert Name :\t\t      {combo_s.get()}")
        textarea.insert(END, f"\n SECTION(BOX)  :\t\t      {combo_d.get()}")
        textarea.insert(END, f"\n Ticket Price:\t\t{dis}")
        textarea.insert(END, f"\n Quantity : {p}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n Total Amount :\t\t{p*dis*diss}")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n\n {55*'*'}")
        save_ticket()
    except Exception:
        messagebox.showwarning('Warning','Pleaes verify the details first')
        clear()

def clear():
    c_name.set('')
    c_phone.set('')
    person.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()

def save_ticket():
    op=messagebox.askyesno("Save ticket","Do you want to download ticket ?")
    if op>0:
        ticket_details=textarea.get('1.0',END)
        f1=open("RECIEPTS/"+str(ticket_no.get())+".txt","w")
        f1.write(ticket_details)
        f1.close()
        messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
    else:
        return
    

    
def welcome():
    x = random.randint(1000, 9999)
    
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.tag_configure("tag_name", justify='center')
    textarea.insert("1.0",  " CONTIX Ticket Seller")
    textarea.tag_add("tag_name", "1.0", "end")
    textarea.insert(END, "\n Production by ")
    textarea.insert(END, "\n TOLEDO, TROPA, TORIO, TASSIAT, SESBREÑO ")
    textarea.insert(END, f"\n {35*'='}")
    textarea.insert(END,f"\n Ticket Number:\t\t {    ticket_no.get()}")
    textarea.insert(END,f"\n Name:\t\t  {    c_name.get()}")
    textarea.insert(END,f"\n Phone Number:\t\t    {    c_phone.get()}")
    textarea.insert(END, f"\n {35*'='}")
    textarea.configure(font='fantasy 15 ')
    
    
    

pic= tk.PhotoImage(file="../images/Contix.png")
title=Label(root,pady=2,image=pic, bg="black", bd=12,fg='gold',font=('fantasy', 25 ,''),relief=FLAT,justify=CENTER)
title.pack(fill=X)


#Product Frames---------------------------------------------------------------------------------------------------------------------------------
F1=LabelFrame(root,bd=10,bg='red',relief=FLAT,font=('fantasy',15,''),fg='gold')
F1.place(x=0,y=105, relwidth=1)



cname_lbl=Label(F1,text='Name',font=('serif',18,''),bg='red',fg='black').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='fantasy 15 ',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('serif',18,''), bg='red',fg='black').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='fantasy 15 ',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, font=('fantasy', 18, ''), fg='gold',)
F2.place(x=20, y=180,width=630,height=500)

source= Label(F2, text='Choose Your Concert', font=('fantasy',18, ''),  fg='black').grid(
row=0, column=0, padx=30, pady=20)
combo_s=ttk.Combobox(F2,font=('fantasy',18),state='readonly',value=CONCERT)
combo_s.grid(row=0,column=1,pady=10)

des= Label(F2, text='Choose your BOX', font=('fantasy',18, ''),  fg='black').grid(
row=1, column=0, padx=30, pady=20)
combo_d=ttk.Combobox(F2,font=('fantasy',18),state='readonly',value=BOX)
combo_d.grid(row=1,column=1,pady=10)



n= Label(F2, text='Number of ticket', font=('fantasy',18, ''),  fg='black').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=person, font='fantasy 15 ', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)

#Ticket area------------------------------------------------------------------------------------------------------------------------------------------
F3=Frame(root,relief=FLAT,bd=10)
F3.place(x=700,y=180,width=550,height=500)

bill_title=Label(F3,text='Ticket',font='fantasy 15 ',bd=7,relief=FLAT).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#Buttons----------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(F2,text='Submit',font='fantasy 15 ',command=verify,padx=5,pady=10,bg='red',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Result',font='fantasy 15 ',command=gticket,padx=5,pady=10,bg='red',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='fantasy 15 ',padx=5,pady=10,command=clear,bg='red',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='fantasy 15 ',padx=5,pady=10,command=exit,bg='red',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

root.mainloop()