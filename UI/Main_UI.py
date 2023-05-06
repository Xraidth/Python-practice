from cProfile import label
from sre_parse import expand_template
from textwrap import fill
import tkinter as tk
from tkinter import *
from classUI import *
from filesUI import *
from widgetsFuntionsUI import *
from WDdepositoUI import *



root=Tk()


root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+420+200')
root.resizable(0,0)
root.config(bg="white")

imag_dep_box = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\deposito.png")


f=None

main_wd = Frame(root)
main_wd.pack(expand=1, fill='both')
                       
main_wd.config(bg="white")
main_wd.config(relief ="groove", bd=2)

wd_menu = Frame(main_wd)
wd_menu.pack()  


wd_menu_title = Frame(wd_menu)
wd_menu_title.config(bg="white")
wd_menu_title.grid(row=0, column=0, pady=50, padx=0)


wd_menu_items = Frame(wd_menu)
wd_menu_items.config(bg="white")
wd_menu_items.grid(row=1, column=0, pady=0, padx=0)

	#-----------------Subwindows--------------------
wd_menu_dep = Frame(wd_menu)
wd_menu_dep.config(bg="white")

wd_menu_coptitle = Frame(wd_menu)
wd_menu_coptitle.config(bg="white")

wd_menu_adtitle = Frame(wd_menu)
wd_menu_adtitle.config(bg="white")

	#-----------------------------------

	# Creating a function for removing widgets from grid







		
def adm(t):
	global f
	f=1
	forgetgrid([wd_menu_items, wd_menu_title])
		
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
		forgetgrid([wd_menu_items, wd_menu_title])
		wd_menu_coptitle.grid(row=0, column=0, pady=50, padx=0)

		dp_t = Label(wd_menu_coptitle, 
			text="COMPRAS",
			fg = "#cc0000",
			#bg = "ligth blue",
			font =("Segoe UI Black",20))
		dp_t.grid(row=0, column=2, pady=10, padx=60)
		

imag_dep_box_1=imag_dep_box.subsample(20,20)

def deposito(t):
		global f
		f=3
		forgetgrid([wd_menu_items, wd_menu_title])
		wd_menu_dep.pack()
		
		createDeposito(wd_menu_dep, lista_productos, imag_dep_box_1)
		
	
		



t = Label(wd_menu_title, 
			text="Tienda Virtual",
			fg = "#cc0000",
			#bg = "ligth blue",
			font =("Arial Black",35,"bold"))
t.grid(row=0, column=2, pady=30, padx=60)





imag3 = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\administracion.png").subsample(7, 7) 
a = Button(wd_menu_items, text = "Administracion", image = imag3, compound = BOTTOM, height = 150, width =150, relief ="flat", highlightbackground="red", command=lambda:  adm(t))

a.grid(row=1, column=1, pady=2, padx=5)

imag = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\carritocompras.png").subsample(7, 7) 
c = Button(wd_menu_items, text = "Compras", image = imag, compound = BOTTOM, height = 150,  width =150, relief ="flat", command=lambda: compras(t))
c.grid(row=1, column=2, pady=2, padx=5)


imag_dep_box_2=imag_dep_box.subsample(7,7)
d = Button(wd_menu_items, text = "Deposito", image = imag_dep_box_2, compound = BOTTOM, height = 150,  width =150, relief ="flat", command=lambda: deposito(t))
d.grid(row=1, column=3, pady=2, padx=5)                    



def back():
		if f==1: forgetgrid([wd_menu_adtitle])
		elif f==2: forgetgrid([wd_menu_coptitle])
		elif f==3: packforget([wd_menu_dep])
		
		wd_menu_title.grid(row=0, column=0, pady=50, padx=0)
		t.grid(row=0, column=2, pady=30, padx=60)
		wd_menu_items.grid(row=1, column=0, pady=0, padx=0)
			
	
		

fimag = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\f_comeback.png").subsample(20, 20) 
fl = Button(main_wd, image = fimag, compound = BOTTOM, relief ="flat", highlightbackground="red", command=lambda: back() )
fl.place(x=2,y=4)





root.mainloop()#Bucle infinito