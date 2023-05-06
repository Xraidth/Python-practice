
try:
    import tkinter as tk
except ImportError:
    import tkinter as tk
from itertools import cycle


        
import datetime
from datetime import datetime
from tkinter import Menu
import os
import pickle 


class Producto():
        #Variables de clase
    def __init__(self, codigo, nombre, stock, precio):
        #Variables de instancia
         self.codigo = codigo
         self.nombre = nombre
         self.stock = stock
         self.precio = precio
    def getCodigo(self):
        return self.codigo
    def getNombre(self):
       return self.nombre
    def getStock(self):
        return self.stock
    def getPrecio(self):
        return self.precio
    def calStock(self, cantidad):
        self.stock = self.stock-cantidad 
    def setCodigo(self,c):
        self.codigo = c
    def setNombre(self,n):
        self.nombre = n
    def setStock(self, s):
        self.stock = s
    def setPrecio(self, p):
        self.precio = p
    def show_me(self,n):
        print(str(n)+ "\t" + str(self.getCodigo()) + "\t" + self.getNombre()[:5] + "\t" + str(self.getStock())+"\t" + str(self.getPrecio()))
    @classmethod
    def classCampos(cls):
        print("Numero"+"\t"+"Codigo"+"\t"+"Nombre"+"\t"+"Stock"+"\t"+"Precio\n")
    @classmethod
    def className(cls):
        return "Productos"


#-------------------------------------------------
#Crea archivos
#def inicioArchivos():
path = 'repository/productos.dat'
isExist = os.path.exists(path)

if isExist == False: 
    archivo_productos = open("repository/productos.dat","wb") #Apertura
    archivo_productos.close()




#-----------------------------------------------------------------------
#Lectura inicial
#def lecturaArchivos():


archivo_productos = open("repository/productos.dat","rb+")

    

if not(os.stat('repository/productos.dat').st_size == 0):
    lista_productos = pickle.load(archivo_productos)
    
else: 
    print("ERROR: Archivo P vacio")
    lista_productos = []

   

   

  
#---------------------------------------------------------
#Escritura final

def escrituraArchivo():
   
    archivo_productos = open("repository/productos.dat","wb+")
    
    
    pickle.dump(lista_productos, archivo_productos)
    

    archivo_productos.close
    
   

def concat_list_productos():
    l2=[]
    for x in lista_productos:
        l1=[str(x.getCodigo()), x.getNombre(), str(x.getStock()),str(x.getPrecio())]
        l2=l2+l1
    return l2
        



  



















def multiple(*func_list):
    '''run multiple functions as one'''
    # I can't decide if this is ugly or pretty
    return lambda *args, **kw: [func(*args, **kw) for func in func_list]; None

def scroll_to_view(scroll_set, *view_funcs):
    ''' Allows one widget to control the scroll bar and other widgets
    scroll set: the scrollbar set function
    view_funcs: other widget's view functions
    '''
    def closure(start, end):
        scroll_set(start, end)
        for func in view_funcs:
            func('moveto', start)
    return closure

class MultiListbox(tk.Frame):
    def __init__(self, master=None, columns=2, data=[], row_select=True, **kwargs):
        '''makes a multicolumn listbox by combining a bunch of single listboxes
        with a single scrollbar
        :columns:
          (int) the number of columns
          OR (1D list or strings) the column headers
        :data:
          (1D iterable) auto add some data
        :row_select:
          (boolean) When True, clicking a cell selects the entire row
        All other kwargs are passed to the Listboxes'''
        tk.Frame.__init__(self, master, borderwidth=1, highlightthickness=1, relief=tk.SUNKEN)
        self.rowconfigure(1, weight=1)
        self.columns = columns
        if isinstance(self.columns, (list, tuple)):
            for col, text in enumerate(self.columns):
                tk.Label(self, text=text).grid(row=0, column=col)
            self.columns = len(self.columns)

        self.boxes = []
        for col in range(self.columns):
            box = tk.Listbox(self, exportselection=not row_select, **kwargs)
            if row_select:
                box.bind('<<ListboxSelect>>', self.selected)
            box.grid(row=1, column=col, sticky='nsew')
            self.columnconfigure(col, weight=1)
            self.boxes.append(box)
        vsb = tk.Scrollbar(self, orient=tk.VERTICAL,
            command=multiple(*[box.yview for box in self.boxes]))
        vsb.grid(row=1, column=col+1, sticky='ns')
        for box in self.boxes:
            box.config(yscrollcommand=scroll_to_view(vsb.set,
                *[b.yview for b in self.boxes if b is not box]))
        self.add_data(data)

    def selected(self, event=None):
        row = event.widget.curselection()[0]
        for lbox in self.boxes:
            lbox.select_clear(0, tk.END)
            lbox.select_set(row)

    def add_data(self, data=[]):
        '''takes a 1D list of data and adds it row-wise
        If there is not enough data to fill the row, then the row is
        filled with empty strings
        these will not be back filled; every new call starts at column 0'''
        # it is essential that the listboxes all have the same length.
        # because the scroll works on "percent" ...
        # and 100% must mean the same in all cases
        boxes = cycle(self.boxes)
        idx = -1
        for idx, (item, box) in enumerate(zip(data, boxes)):
            box.insert(tk.END, item)
        for _ in range(self.columns - idx%self.columns - 1):
            next(boxes).insert(tk.END, '')
          
    def __getitem__(self, index):
        '''get a row'''
        return [box.get(index) for box in self.boxes]

    def __delitem__(self, index):
        '''delete a row'''
        [box.delete(index) for box in self.boxes]

    def curselection(self):
        '''get the currently selected row'''
        selection = self.boxes[0].curselection()
        return selection[0] if selection else None
        
"""
class GUI(tk.Frame):
    '''an example gui'''
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        b = MultiListbox(self, ['Numero', 'Nombre', 'Stock', 'Precio'], width=4)
        b.add_data(concat_list_productos())
        b.pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    win = GUI(root)
    win.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
"""
  

root=tk.Tk()
root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+500+200')
root.resizable(0,0)
root.config(bg="white")

l= tk.Frame(root, height=500,width=500)
l.pack(expand=1, fill=tk.BOTH, anchor="center")
l.config(bg="black")

b = MultiListbox(l,['Numero', 'Nombre', 'Stock', 'Precio'], width=4)
b.add_data(concat_list_productos())
b.pack(fill=tk.BOTH, expand=True)  


root.mainloop()