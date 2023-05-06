
from tkinter import *
from REPO import ingresarProductos
from tkinter import ttk








def wd_2_in_producto():
    wd_2_in_producto = Toplevel()
    wd_2_in_producto.title("Ingreso de productos")
    wd_2_in_producto.iconbitmap("iconoroot.ico")
    wd_2_in_producto.geometry('290x290+1070+350')
    wd_2_in_producto.resizable(0,0)

    wd_2_in_producto_div = Frame(wd_2_in_producto)
    wd_2_in_producto_div.pack(side="top", anchor="nw")

    wd_2_in_producto_div_2 = Frame(wd_2_in_producto)
    wd_2_in_producto_div_2.pack(side="bottom", pady=2)
    
    wd_2_in_producto_l_nom = Label(wd_2_in_producto_div, text="Nombre", font =("Arial",12), justify="left").grid(row="0",column="0",pady=0,padx=5)
    wd_2_in_producto_l_stk = Label(wd_2_in_producto_div, text="Stock", font =("Arial",12), justify="left").grid(row="1",column="0",pady=10,padx=5)
    wd_2_in_producto_l_pre = Label(wd_2_in_producto_div, text="Precio", font =("Arial",12), justify="left").grid(row="2",column="0",pady=10,padx=5)

    nom = Entry(wd_2_in_producto_div, font =("Arial",12), justify="center").grid(row="0",column="1",pady=10)
    stk = Entry(wd_2_in_producto_div, font =("Arial",12), justify="center").grid(row="1",column="1",pady=10)
    pre = Entry(wd_2_in_producto_div, font =("Arial",12), justify="center").grid(row="2",column="1",pady=10)

    nom2 = nom.get()
    stk2 = stk.get()
    pre2 = pre.get()
    wd_2_in_producto_b_add = Button(wd_2_in_producto_div_2, text="Agregar",width=8, command= lambda: ingresarProductos(nom,stk,pre))
    wd_2_in_producto_b_add.grid(row="0",column="0",padx=8,pady=0) 

    wd_2_in_producto_b_apl = Button(wd_2_in_producto_div_2, text="Aplicar",width=8)
    wd_2_in_producto_b_apl.grid(row="0",column="1",padx=10,pady=0)  
    wd_2_in_producto_b_ccc = Button(wd_2_in_producto_div_2, text="Cancelar", command=wd_2_in_producto.destroy,width=8)
    wd_2_in_producto_b_ccc.grid(row="0",column="2",padx=10,pady=0) 


def wd_2_mod_producto():
    # Crear una ventana secundaria.
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Modificacion de productos")
    ventana_secundaria.iconbitmap("iconoroot.ico")
#    ventana_secundaria.config(width=300, height=200)
    ventana_secundaria.geometry('350x380+650+250')
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)

def wd_2_del_producto():
    # Crear una ventana secundaria.
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Eliminacion de productos")
    ventana_secundaria.iconbitmap("iconoroot.ico")
#    ventana_secundaria.config(width=300, height=200)
    ventana_secundaria.geometry('350x380+650+250')
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)    
