from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os

root=Tk()
root.title('Employee record')
root.geometry('1280x720')
bg_color='red'

#####################Variable#################
ref_var=IntVar()
name_var=StringVar()
gender_var=StringVar()
email_var=StringVar()
salary_var=StringVar()
phone_var=StringVar()
des_var=StringVar()

###################function######################
#if ref_var.get()==0 and name_var.get()=='' and gender_var.get()=='' and salary_var.get()=='' and email_var.get()=='' and phone_var.get()=='' and des_var.get()=='':
    #print('Error','All fields are required?')

def add():
    if ref_var.get()==0 or name_var.get()=='' or gender_var.get()=='' or salary_var.get()=='' or email_var.get()=='' or phone_var.get()=='' or des_var.get()=='':
        tkinter.messagebox.showerror("Error","All fields are required!")   
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n====================')
        textarea.insert(END,f'Employee ref\t\t\t\t{ref_var.get()}')
        textarea.insert(END, '\n====================')
        textarea.insert(END, f'\n\nFull Name\t\t\t\t{name_var.get()}')
        textarea.insert(END, f'\nEmail Address\t\t\t\t{email_var.get()}')
        textarea.insert(END, f'\nGender\t\t\t\t{gender_var.get()}')
        textarea.insert(END, f'\nDesignation\t\t\t\t{des_var.get()}')
        textarea.insert(END, f'\nContact No.\t\t\t\t{phone_var.get()}')
        textarea.insert(END, f'\n   Salary Amt\t\t\t\t{salary_var.get()}')
        textarea.insert(END, f'\nHome Address\t\t\t\t{txt_add.get(1.0, END)}')
        textarea.insert(END, '\n###################################')

        
#os was imported so as for this program to run.
def save():
    data=textarea.get(1.0,END)
    f1=open('recordss/'+str(ref_var.get())+'.txt','w')
    f1.write(data)
    f1.close()
    tkinter.messagebox.showinfo('Saved', f'Ref No:{ref_var.get()} Saved successfully')

#os was imported so as for this program to run.
def print():
    data=textarea.get(1.0,END)
    f='C:\\Users\\ADIGUN ASHABI FATHIA\\AppData\\Local\\Programs\\Python\\Python39\\recordss'+str(ref_var.get())+'.txt'
    os.startfile(f,'Print')

def reset():
    textarea.delete(1.0,END)
    txt_add.delete(1.0, END)
    ref_var.set(0)
    name_var.set('')
    gender_var.set('')
    des_var.set('')
    phone_var.set('')
    email_var.set('')
    salary_var.set('')

def Exit():
    if tkinter.messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()
        
        
##################Heading###########################
title=Label(root,text='Employee Records System',bg=bg_color,fg='blue',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)
# x=fill horizontal with the color choosen.


#================Left Frame Details=================
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=665,height=560)

lbl_ref=Label(F1,text='Employee ref', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_ref.grid(row=0,column=0,padx=30,pady=10)
txt_ref=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=ref_var)
txt_ref.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Full Name', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_email=Label(F1,text='Email Address', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_email.grid(row=2,column=0,padx=30,pady=10)
txt_email=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=email_var)
txt_email.grid(row=2,column=1,pady=10,sticky='w')

lbl_Gender=Label(F1,text='Gender', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_Gender.grid(row=3,column=0,padx=30,pady=10)

combo_gender=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=gender_var)
combo_gender['value']=('male','female','unic','others')
combo_gender.grid(row=3,column=1,pady=10)

lbl_des=Label(F1,text='Designation', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_des.grid(row=4,column=0,padx=30,pady=10)

combo_des=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=des_var)
combo_des['value']=('Hr','Accountant','IT','Sales','Finance','Engineer','Doctor')
combo_des.grid(row=4,column=1,pady=10)

lbl_no=Label(F1,text='Contact No.', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_no.grid(row=5,column=0,padx=30,pady=10)
txt_no=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=phone_var)
txt_no.grid(row=5,column=1,pady=10,sticky='w')

lbl_s=Label(F1,text='Salary Amt', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_s.grid(row=6,column=0,padx=30,pady=10)
txt_s=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=salary_var)
txt_s.grid(row=6,column=1,pady=10,sticky='w')

lbl_add=Label(F1,text='Home Address', font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_add.grid(row=7,column=0,padx=30,pady=10)
txt_add=Text(F1,width=40,height=3,font=('times new rommon',10),relief=RIDGE,bd=7)
txt_add.grid(row=7,column=1,pady=5,sticky='w')


#####################right frame details#####################
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=660,height=560)

lbl_t=Label(F2,text='Employee Details', font=('italic 15 bold'),fg='black',bd=7,relief=GROOVE)
lbl_t.pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='italic 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)


##################Button########################
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1295,height=100)

btn1=Button(F3,text='Add Record',font='arial 20 bold',bg='black',fg='red',width=10,command=add)
btn1.grid(row=0,column=0,padx=25,pady=7)

btn2=Button(F3,text='Save',font='arial 20 bold',bg='black',fg='red',width=10,command=save)
btn2.grid(row=0,column=1,padx=25,pady=7)

btn3=Button(F3,text='Print',font='arial 20 bold',bg='black',fg='red',width=10,command=print)
btn3.grid(row=0,column=2,padx=25,pady=7)

btn4=Button(F3,text='Reset',font='arial 20 bold',bg='black',fg='red',width=10,command=reset)
btn4.grid(row=0,column=3,padx=25,pady=7)

btn5=Button(F3,text='Exit',font='arial 20 bold',bg='black',fg='red',width=10,command=Exit)
btn5.grid(row=0,column=4,padx=25,pady=7)


root.mainloop()
