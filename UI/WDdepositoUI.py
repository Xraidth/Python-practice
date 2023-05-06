
from cProfile import label
from sre_parse import expand_template
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import *
from EDproductos import *



try:
    import tkinter as tk
except ImportError:
    import tkinter as tk
from itertools import cycle


        
import datetime
from datetime import datetime
from tkinter import Menu



def nscount(lista_productos):
    c=0
    for x in lista_productos:
        if (x.getStock()==0): c=c+1 
    return str(c)    
   

def concat_list_productos(lista_productos):
    l2=[]
    for x in lista_productos:
        l1=[str(x.getCodigo()), x.getNombre(), str(x.getStock()),"$"+str(x.getPrecio())]
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





#---------------------------------------------------


def createDeposito(root, lista_productos, imag2_1):

        main_wd = Frame(root)
        main_wd.pack(expand=1, fill='both')
                            
        main_wd.config(bg="white")

        wd_deposito = Frame(main_wd)
        wd_deposito.pack(expand=1, fill='both') 
        wd_deposito.config(bg="black")  


        wd_deposito_div_1 = Frame(wd_deposito)
        wd_deposito_div_1.grid(row=0, column=0, pady=0, padx=0)


        wd_deposito_div_2 = Frame(wd_deposito)
        wd_deposito_div_2.grid(row=1, column=0, pady=0, padx=0)


        wd_deposito_div_3 = Frame(wd_deposito)
        wd_deposito_div_3.grid(row=2, column=0, pady=0, padx=0)

        wd_deposito_div_2_1 = Frame(wd_deposito_div_2)
        wd_deposito_div_2_1.grid(row=0, column=0, pady=0, padx=0)

        wd_deposito_div_2_2 = Frame(wd_deposito_div_2)
        wd_deposito_div_2_2.grid(row=0, column=1, pady=0, padx=0)



        wd_deposito_header = Frame(wd_deposito_div_1, height = 40, width = 652)
        wd_deposito_header.pack()
        wd_deposito_header.config(relief="groove", bd=3)
        #wd_deposito_header.config(bg="green")

        wd_deposito_body = Frame(wd_deposito_div_2_1)
        wd_deposito_body.pack(fill=tk.BOTH,expand=1)
        #wd_deposito_body.config(bg="orange")

        wd_deposito_right_bar = Frame(wd_deposito_div_2_2, height = 375, width = 130)
        wd_deposito_right_bar.pack()
        #wd_deposito_right_bar.config(bg="red")

        wd_deposito_footer = Frame(wd_deposito_div_3, height = 40, width = 650)
        wd_deposito_footer.pack()
        #wd_deposito_footer.config(bg="blue")


        #-----header--------
        wd_deposito_header_div = Frame(wd_deposito_header, height = 40, width = 300)
        wd_deposito_header_div.place(x=30,y=2)
        #wd_deposito_header_div.config(bg="#000000")

        wd_deposito_header_div_1 = Frame(wd_deposito_header_div)
        wd_deposito_header_div_1.grid(row=0, column=0, pady=0, padx=0)
        wd_deposito_header_div_1.config(bg="black")

        wd_deposito_header_div_2 = Frame(wd_deposito_header_div)
        wd_deposito_header_div_2.grid(row=0, column=1, pady=0, padx=10)


        t = Label(wd_deposito_header_div_2, 
                text="Deposito",
                fg = "#000000",
                #bg = "ligth blue",
                font =("Arial Black",12))
        t.pack()

        
        
        t2 = Label(wd_deposito_header_div_1, image=imag2_1)	 
        t2.pack()
        #---------body----------


        wd_deposito_body_div= Frame(wd_deposito_body, height = 0.5, width = 520)
        wd_deposito_body_div.pack(side="top")


        wd_deposito_body_div= Frame(wd_deposito_body, height = 375, width = 0.5)
        wd_deposito_body_div.pack(side="right")
        wd_deposito_body_div.config(bg="#8f9a9c")

        b = MultiListbox(wd_deposito_body,['Numero', 'Nombre', 'Stock', 'Precio'], width=4)
        b.add_data(concat_list_productos(lista_productos))
        b.pack(fill=tk.BOTH, expand=True)  

        #----------------------------------

        #-------------------right_bar-----------


        wd_deposito_right_bar_div_1 = Frame(wd_deposito_right_bar, bg="#eeeeea")
        wd_deposito_right_bar_div_1.place(x=8,y=20)


        wd_deposito_right_bar_div_1_1 = Frame(wd_deposito_right_bar_div_1) 
        wd_deposito_right_bar_div_1_2 = Frame(wd_deposito_right_bar_div_1)
        wd_deposito_right_bar_div_1_3 = Frame(wd_deposito_right_bar_div_1) 

        wd_deposito_right_bar_div_1_1.grid(row=1, column=0, pady=10, padx=20)
        wd_deposito_right_bar_div_1_2.grid(row=2, column=0, pady=10, padx=20)
        wd_deposito_right_bar_div_1_3.grid(row=3, column=0, pady=10, padx=20)


        add= Button(wd_deposito_right_bar_div_1_1, text="Añadir", height = 1,  width =10, bg="#eedfff", command=lambda: wd_2_in_producto() )
        mod= Button(wd_deposito_right_bar_div_1_2, text="Modificar", height = 1,  width =10, bg="#eedfff", command=lambda: wd_2_mod_producto() )
        ddd= Button(wd_deposito_right_bar_div_1_3, text="Borrar", height = 1,  width =10, bg="#eedfff", command=lambda:wd_2_del_producto())

        add.pack()
        mod.pack()
        ddd.pack()
        #-------------------footer-----------




        wd_deposito_footer_div = Frame(wd_deposito_footer, height = 0.5, width =650, bg="#8f9a9c")
        wd_deposito_footer_div.pack(side="top", anchor="n", pady=1)



        t = Label(wd_deposito_footer,text="Total: "+(str(len(lista_productos))+"   Sin stock: "+ nscount(lista_productos)), fg = "#000000", font =("Arial",10)) #bg = "ligth blue",
        t.pack(pady=5)#.place(x=20,y=4)
        #----------------------------------------

       




