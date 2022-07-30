#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *

def getvals(event):
    value = event.widget.cget('text')
    if value=='Vider':
        sc_variable.set('')
        screen.update()
        status_var.set('Pas de calcule en cours.')
        screen.update()
    elif value=='=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
            status_var.set('Calcule en cours..')
            screen.update()
        except Exception as e:
            screen.update()
            status_var.set('erreur!!')
            screen.update()
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')

root=Tk()
canvas_width=455
canvas_height=600
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('Calculatrice')

my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
root.config(menu=my_menu)
my_menu.add_command(label='Fermer',command=quit)

sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='black',bg='white',borderwidth=5)
screen.pack(pady=30)

# Ligne 1 de la calculatrice 7..*
f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b2=Button(f,text='8',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b3=Button(f,text='9',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b4=Button(f,text='*',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4]
count=0
for i in range(4):
        buttons[count].grid(row=1,column=i)
        count += 1

# Ligne 2 de la calculatrice 4..-
f=Frame(root)
f.pack()
b1=Button(f,text='4',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b2=Button(f,text='5',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b3=Button(f,text='6',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b4=Button(f,text='-',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4]
count=0
for i in range(4):
    buttons[count].grid(row=2,column=i)
    count += 1

# Ligne 3 de la calculatrice 1..+
f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b2=Button(f,text='2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b3=Button(f,text='3',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b4=Button(f,text='+',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4]
count=0
for i in range(4):
    buttons[count].grid(row=3,column=i)
    count += 1
f=Frame(root)
f.pack()

# Ligne 4 de la calculatrice ,..Vider
b1=Button(f,text='.',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b2=Button(f,text='0',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b3=Button(f,text='/',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)
b4=Button(f,text='Vider',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)

buttons=[b1,b2,b3,b4]
count=0
for i in range(4):
    buttons[count].grid(row=4,column=i)
    count += 1
f=Frame(root)
f.pack()

# la derniere ligne avec le button = 
b1=Button(f,text='=',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='blue',bg='white',width=24)

b1.bind('<Button-1>',getvals)

buttons=[b1]
count=0
for i in range(1):
    buttons[count].grid(row=4,column=i)
    count += 1
f=Frame(root)
f.pack()
status_var=StringVar()
status_var.set('Calcule en cours...')
Label(root,textvariable=status_var,relief=SUNKEN,anchor='w',borderwidth=3,bg='yellow',fg='black').pack(side=BOTTOM,fill=X)

root.mainloop()


# In[ ]:




