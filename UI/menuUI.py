
from cProfile import label
from sre_parse import expand_template
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import *



root=Tk()


root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+500+200')
root.resizable(0,0)
root.config(bg="white")


f=None

main_wd = Frame(root)
main_wd.pack(expand=1, fill='both')
                       
main_wd.config(bg="white")
main_wd.config(relief ="groove", bd=2)

wd_menu = Frame(main_wd)
wd_menu.pack(expand=1, anchor="n")  


wd_menu_title = Frame(wd_menu)
wd_menu_title.config(bg="white")
wd_menu_title.grid(row=0, column=0, pady=50, padx=0)


wd_menu_items = Frame(wd_menu)
wd_menu_items.config(bg="white")
wd_menu_items.grid(row=1, column=0, pady=0, padx=0)

#-----------------Subwindows--------------------
wd_menu_deptitle = Frame(wd_menu)
wd_menu_deptitle.config(bg="white")

wd_menu_coptitle = Frame(wd_menu)
wd_menu_coptitle.config(bg="white")

wd_menu_adtitle = Frame(wd_menu)
wd_menu_adtitle.config(bg="white")

#-----------------------------------

# Creating a function for removing widgets from grid
def removegrid(widgets): 
  for x in widgets:
	  x.grid_remove()
	
def forgetgrid(widgets): 
  for x in widgets:
	  x.grid_forget()
	
def packforget(widgets):
	for x in widgets:
	  x.pack_forget()

def destroylist(widgets):
	for x in widgets:
	    x.destroy()






	
def adm(t):
	global f
	f=1
	forgetgrid([wd_menu_items, t, wd_menu_title])
	
	wd_menu_adtitle.grid(row=0, column=0, pady=50, padx=0)
	

	dp_t = Label(wd_menu_adtitle, 
		 text="ADMINISTRACION",
		 fg = "#cc0000",
		 #bg = "ligth blue",
		 font =("Segoe UI Black",20))
	dp_t.grid(row=0, column=2, pady=10, padx=60)
	
    
	
	
def compras(t):
	global f
	f=2
	forgetgrid([wd_menu_items, t, wd_menu_title])
	wd_menu_coptitle.grid(row=0, column=0, pady=50, padx=0)

	dp_t = Label(wd_menu_coptitle, 
		 text="COMPRAS",
		 fg = "#cc0000",
		 #bg = "ligth blue",
		 font =("Segoe UI Black",20))
	dp_t.grid(row=0, column=2, pady=10, padx=60)
	

def deposito(t):
	global f
	f=3
	forgetgrid([wd_menu_items, t, wd_menu_title])
	wd_menu_deptitle.grid(row=0, column=0, pady=50, padx=0)
	
 
	



t = Label(wd_menu_title, 
		 text="Tienda Virtual",
		 fg = "#cc0000",
		 #bg = "ligth blue",
		 font =("Arial Black",35))
t.grid(row=0, column=2, pady=30, padx=60)





imag3 = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\administracion.png").subsample(7, 7) 
a = Button(wd_menu_items, text = "Administracion", image = imag3, compound = BOTTOM, height = 150, width =150, relief ="flat", highlightbackground="red", command=lambda:  adm(t))

a.grid(row=1, column=1, pady=2, padx=5)


imag = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\carritocompras.png").subsample(7, 7) 
c = Button(wd_menu_items, text = "Compras", image = imag, compound = BOTTOM, height = 150,  width =150, relief ="flat", command=lambda: compras(t))
c.grid(row=1, column=2, pady=2, padx=5)


imag2 = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\deposito.png").subsample(7, 7) 
d = Button(wd_menu_items, text = "Deposito", image = imag2, compound = BOTTOM, height = 150,  width =150, relief ="flat", command=lambda: deposito(t))
d.grid(row=1, column=3, pady=2, padx=5)                    


def back():
	if f==1: forgetgrid([wd_menu_adtitle])
	elif f==2: forgetgrid([wd_menu_coptitle])
	elif f==3: forgetgrid([wd_menu_deptitle])
	wd_menu_title.grid(row=0, column=0, pady=50, padx=0)
	t.grid(row=0, column=2, pady=30, padx=60)
	wd_menu_items.grid(row=1, column=0, pady=0, padx=0)
		
  
	

fimag = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\f_comeback.png").subsample(20, 20) 
fl = Button(main_wd, image = fimag, compound = BOTTOM, relief ="flat", highlightbackground="red", command=lambda: back() )
fl.place(x=2,y=4)




root.mainloop()#Bucle infinito






