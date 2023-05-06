
"""
tkinter
Wxpython
PyQT
PyGTK


Raiz->frames->widgets




from tkinter import *
raiz=Tk()

raiz.title("Tienda Virtual")#Titulo de la ventana
#raiz.resizable(1,0) impedir el redimencionamiento
raiz.iconbitmap("iconoraiz.ico")
raiz.geometry("650x652")
raiz.config(bg="black")

miframe = Frame()#se puede especificar dentro de frame la raiz y el tamaño directamente acà  
miframe.pack() 

para el pak
side="left" anchor="n"  Colocar en tal lado
fill = "y" expand="true" redimencionar fill both es para que se expanda en x e y



miframe.config(width="650", height="652", bg="white")





-----bordes------
relief="groove" entre comillas el tipo de borde
bd=20 grosor de 20

#cursor
cursor="hand2"




#label
variable=label(contenedor PADRE,opciones)
label.place(x=100,y=100)

label().place() #tamb se puede esto

"bold" para negrita


#imagenes

miimagen=PhotoImage(file="nombredearchivodeimagen.gif")
label(contenedor, image=miimagen).place(x=0,y=0)


#entrys
cuadroTxt=Entry(raiz)
cuadroTxt.pack()
place tambien sirve


trabajar con pack o con grid

.grid() #tablas 
row=0 colum=0
sticky ="e"  puntos cardinales
#padding
padx = 
pady = 

config show="*" muestra el asterisco





raiz.mainloop()#Bucle infinito




tk.Button(miframe,
                                 text = "Comprar",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35).grid(row=1, column=2, pady=4, padx=10)
                                 
tk.Button(miframe,
                                 text = "Listar compras",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35).grid(row=2, column=2, pady=6, padx=10)
#------------
tk.Button(miframe,
                                 text = "Detalle de compra",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35).grid(row=3, column=2, pady=6, padx=10)
tk.Button(miframe,
                                 text = "Ingreso de productos",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35).grid(row=4, column=2, pady=6, padx=10)
tk.Button(miframe,
                                 text = "Listado de productos",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35).grid(row=5, column=2, pady=6, padx=10)                                                  

tk.Button(miframe,
                                 text = "Salir",
                                 bg = "#ffffd9",
                                 fg = "black",
                                 font=("Georgia",12),
                                 height = 1, 
                                 width =35,                             
                                 command=raiz.destroy).grid(row=6, column=2, pady=40, padx=10)

command se usa la funcion sin parentesis pero si queres pasarle paraletros se usa lambda
comand = lambda: saludo("HOLA MUNDO")




caja=entry
x=caja.get() devuelve el valor ingresado


label etiqueta
etiqueta["Texto"]=x


borrar con forget 
grid_forget
pack_forget



import tkinter as tk
    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.label=tk.Label(self.root,
                           text = "Label")
       self.buttonForget = tk.Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.pack_forget())
       self.buttonRecover = tk.Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.pack())       
       
       self.buttonForget.pack()
       self.buttonRecover.pack()
       self.label.pack(side="bottom")
       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
root = Test()

# Python program to remove widgets
# from grid in tkinter
  
# Import the library tkinter
from tkinter import *
  
# Create a GUI root
root = Tk()
  
# Creating a function for removing widgets from grid
def remove(widget1, widget2):
    widget1.grid_remove()
    widget2.grid_remove()
  
# Creating a function for making widget visible again
def display(widget1, widget2):
    widget1.grid(column=0, row=3, padx=10, pady=10)
    widget2.grid(column=0, row=4, padx=10, pady=10)
  
# Button widgets
b1 = Button(root, text="Vinayak")
b1.grid(column=0, row=3, padx=10, pady=10)
  
# Label Widgets
l1 = Button(root, text="Rai")
l1.grid(column=0, row=4, padx=10, pady=10)
  
# Create and show button with remove() function
remove_btn = Button(root, text="Remove widgets", 
                    command=lambda: remove(b1, l1))
remove_btn.grid(column=0, row=0, padx=10, pady=10)
  
# Create and show button with display() function
display_btn = Button(root, text="Display widgets",
                     command=lambda: display(b1, l1))
display_btn.grid(column=0, row=1, padx=10, pady=10)
  
# Make infinite loop for displaying root on screen
root.mainloop()









def forgetgrid(widgets): #Olvida widgets con grid
  for x in widgets:
	  x.grid_forget()
	
def packforget(widgets): #Olvida widgets con pack
	for x in widgets:
	  x.pack_forget()

def destroylist(widgets): #Destruye widgets
	for x in widgets:
	    x.destroy()










  

from tkinter import *
  

#---------------------------------------------------------------
root = Tk()
root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+500+200')
root.resizable(0,0)
root.config(bg="white")
#---------------------------------------------------------------

# Creating a function for removing widgets from grid
def remove(l):
    for w in l:
     w.grid_remove()

# Creating a function for making widget visible again
def display(widget1, widget2):
    widget1.grid(column=0, row=3, padx=10, pady=10)
    widget2.grid(column=0, row=4, padx=10, pady=10)

#------------------------------------------------------------------
fr = Frame(root)
fr.pack(expand=1, fill='both')
                       
fr.config(bg="white")
fr.config(relief ="groove", bd=2)

fr2 = Frame(fr)#se puede especificar dentro de frame la root y el tamaño directamente acà  
fr2.pack(expand=1, anchor="n")  

#-------------------------------------------------------------------------------
frd1 = Frame(fr2)#se puede especificar dentro de frame la root y el tamaño directamente acà    
frd1.config(bg="white")
frd1.grid(row=0, column=0, pady=50, padx=0)


frd2 = Frame(fr2)#se puede especificar dentro de frame la root y el tamaño directamente acà    
frd2.config(bg="white")
frd2.grid(row=1, column=0, pady=0, padx=0)
#---------------------------------------------------------------------------------
    



titulo = Label(frd1, 
		 text="Tienda Virtual",
		 fg = "#cc0000",
		 #bg = "ligth blue",
		 font =("Arial Black",35)).grid(row=0, column=2, pady=30, padx=60)


#imag = PhotoImage(file = r"C:\Users\usuario\Desktop\Drive\ERP\carritocompras.png").subsample(7, 7) 
#a = Button(frd2, text = "Administracion", image = imag, compound = BOTTOM, height = 150, width =150).grid(row=0, column=1, pady=2, padx=5)


b1 = Button(frd2, text="Vinayak")
b1.grid(column=0, row=3, padx=10, pady=10)
  
# Label Widgets
l1 = Button(frd2, text="Rai")
l1.grid(column=0, row=4, padx=10, pady=10)
  
# Create and show button with remove() function
remove_btn = Button(frd2, text="Remove widgets", 
                    command=lambda: remove([l1, b1]))
remove_btn.grid(column=0, row=0, padx=10, pady=10)
  
# Create and show button with display() function
display_btn = Button(frd2, text="Display widgets",
                     command=lambda: display(b1, l1))
display_btn.grid(column=0, row=1, padx=10, pady=10)


root.mainloop()

import tkinter as tk

def on_enter(e):
    myButton['background'] = 'red'

def on_leave(e):
    myButton['background'] = 'SystemButtonFace'

root = tk.Tk()
myButton = tk.Button(root,text="Click Me")
myButton.grid()


myButton.bind("<Enter>", on_enter) #Funciones de eventos
myButton.bind("<Leave>", on_leave)

root.mainloop()

def pulsar(event):
    if event.char =="q" : hace algo

ventana.bind("<key>", pulsar)






















from cProfile import label
from sre_parse import expand_template
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import *
root=Tk()


lista_productos = ["Tomate", "huevo", "cevolla"]


root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+500+200')
root.resizable(0,0)
root.config(bg="white")



main_wd = Frame(root)
main_wd.pack(expand=1, fill='both')
                       
main_wd.config(bg="white")
#main_wd.config(relief ="groove", bd=2)

wd_deposito = Frame(main_wd)
wd_deposito.pack(expand=1, fill='both')   #anchor="n"


wd_deposito_header = Frame(wd_deposito, height = 40, width = 650)
wd_deposito_header.grid(row=0, column=0, columnspan=3, pady=0, padx=0)
wd_deposito_header.config(bg="green")

wd_deposito_left_bar = Frame(wd_deposito, height =375, width = 216)
wd_deposito_left_bar.grid(row=1, column=0, pady=0, padx=0)
wd_deposito_left_bar.config(bg="yellow")

wd_deposito_body = Frame(wd_deposito, height = 375, width = 216)
wd_deposito_body.grid(row=1, column=1, pady=0, padx=0)
wd_deposito_body.config(bg="orange")

wd_deposito_right_bar = Frame(wd_deposito, height = 375, width = 218)
wd_deposito_right_bar.grid(row=1, column=2, pady=0, padx=0)
wd_deposito_right_bar.config(bg="red")

wd_deposito_footer = Frame(wd_deposito, height = 40, width = 650)
wd_deposito_footer.grid(row=2, column=0, columnspan=3, pady=0, padx=0)
wd_deposito_footer.config(bg="blue")

root.mainloop()#Bucle infinito






































from cProfile import label
from sre_parse import expand_template
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import *
root=Tk()


lista_productos = ["Tomate", "huevo", "cevolla"]


root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+500+200')
root.resizable(0,0)
root.config(bg="white")



main_wd = Frame(root)
main_wd.pack(expand=1, fill='both')
                       
main_wd.config(bg="white")

wd_deposito = Frame(main_wd)
wd_deposito.pack(expand=1, fill='both')   


wd_deposito_header = Frame(wd_deposito, height = 40, width = 650)
wd_deposito_header.grid(row=0, column=0, columnspan=2, pady=0, padx=0)
wd_deposito_header.config(bg="green")

wd_deposito_body = Frame(wd_deposito, height = 375, width = 520)
wd_deposito_body.grid(row=1, column=0, pady=0, padx=0)
wd_deposito_body.config(bg="orange")

wd_deposito_right_bar = Frame(wd_deposito, height = 375, width = 130)
wd_deposito_right_bar.grid(row=1, column=1, pady=0, padx=0)
wd_deposito_right_bar.config(bg="red")

wd_deposito_footer = Frame(wd_deposito, height = 40, width = 650)
wd_deposito_footer.grid(row=2, column=0, columnspan=2, pady=0, padx=0)
wd_deposito_footer.config(bg="blue")

root.mainloop()#Bucle infinito


import tkinter as tk
import random
def actualizar_etiqueta():
    numero_aleatorio = random.randint(1, 100)
    etiqueta1.config(text=f"Número aleatorio: {numero_aleatorio}")
    ventana.after(2000, actualizar_etiqueta) #Recursividad dentro de aqui
ventana = tk.Tk()
ventana.title("Ejemplo after() en Tk")
ventana.config(width=400, height=300)
etiqueta1 = tk.Label(text="¡Hola mundo!")
etiqueta1.place(x=100, y=70)
ventana.after(2000, actualizar_etiqueta)
ventana.mainloop()

"""