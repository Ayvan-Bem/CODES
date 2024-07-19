import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox 

# root window
root = tk.Tk()
root.geometry("350x500")
root.title('Eibrhm Toledo')
root.resizable(0, 0)

#window 2 as root 2
def press(event):
        root2 = tk.Tk()
        root2.geometry("350x500")
        root2.title('Eibrhm Toledo')
        root2.resizable(0, 0)
        root2.columnconfigure(0, weight=1)
        root2.columnconfigure(1, weight=3)

        lb1 = ttk.Label(root2, text="Name:")
        lb1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        lba = ttk.Label(root2, text=name_entry.get())
        lba.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        lbl2 = ttk.Label(root2, text="Stundent ID:")
        lbl2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        lbl2a = ttk.Label(root2, text=ID_entry.get())
        lbl2a.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        lbl3 = ttk.Label(root2, text="SEX:")
        lbl3a = ttk.Label(root2, text=selected.get())
        lbl3.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        lbl3a.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        lbl4a = ttk.Label (root2, text="DEPARTMENT:")
        lbl4a.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        lbl4 = ttk.Label (root2, text=Combo.get())
        lbl4.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        l = [selected1.get(), selected2.get()]
        v = ['Web/Mobile App Development', 'Game Development']
        b = ""
        for i,j in enumerate(l):
            if j == 1:
                b += v[i] + "\n"
       
        lb5 = ttk.Label(root2, text="TRACKS:")
        lbl5 = ttk.Label(root2, text=b)
        lb5.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        lbl5.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        a = ""
        for i in lb.curselection():
            a += lb.get(i)+ "\n"
        lb6 = ttk.Label(root2, text="COURSES:")
        lb6.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        lbl7 = ttk.Label(root2, text=a)
        lbl7.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5) 
        root2.mainloop()


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

name_label = ttk.Label(root, text="Name:")
name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

ID_label = ttk.Label(root, text="Stundent ID:")
ID_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

ID_entry = ttk.Entry(root)
ID_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

selected = tk.StringVar()
labels = ttk.Label(root, text="SEX:")
labels.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
r1 = ttk.Radiobutton(root, text='MALE', value='MALE', variable=selected) 
r2 = ttk.Radiobutton(root, text='FEMALE', value='FEMALE', variable=selected) 
r1.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
r2.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

#sample code for Combobox 
vlist = ["IT", "CS", "HRM",
          "TN"]
 
Combo = ttk.Combobox(root, values = vlist)
Combo.set("DEPARTMENTs")
Combo.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

#Checkbutton
selected1= tk.IntVar()
selected2 =tk.IntVar()
CB = ttk.Label(root, text="TRACK:")
CB.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
C= ttk.Checkbutton(root)
C1 = ttk.Checkbutton(root, text = "Web/Mobile App Development", variable = selected1) 
C2 = ttk.Checkbutton(root, text = "Game Development", variable = selected2) 
C1.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
C2.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
#listbox
LB = ttk.Label(root, text="COURSES:")
LB.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
lb= tk.Listbox(root) 
lb=tk.Listbox(root, height=5, selectmode='multiple') 
course = ("IPT", "Networking", "IAS", "Capstone") 
for sub in course:
    lb.insert(tk.END,sub)
lb.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5) 

# submit button
subbutton=ttk.Button(root, text="Submit")
subbutton.bind('<Button-1>', press)
subbutton.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)


root.mainloop()
