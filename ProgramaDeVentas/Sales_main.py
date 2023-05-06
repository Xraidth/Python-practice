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

class LineaCompra():
    def __init__(self, numero, cantidad, subtotal, codProducto, codCompra):
         self.numero = numero
         self.cantidad = cantidad
         self.subtotal = subtotal
         self.codProducto = codProducto
         self.codCompra = codCompra
    def getNumero(self):
        return self.numero
    def getCantidad(self):
       return self.cantidad
    def getSubtotal(self):
        return self.subtotal
    def getCodProducto(self):
        return self.codProducto
    def getCodCompra(self):
        return self.codCompra

class Compra():
    def __init__(self, codigo, fechahora, estado, totalprecio):
         self.codigo = codigo
         self.fechahora = fechahora
         self.estado = estado
         self.totalprecio = totalprecio
    def getCodigo(self):
        return self.codigo   
    def getFecha(self):
        return self.fechahora
    def getEstado(self):
       return self.estado
    def getTotalPrecio(self):
        return self.totalprecio
    def setEstado(self,n):
        if n==1:self.estado = "Paga"
        elif n==0: self.estado = "No paga"


#-------------------------------------------------
#Crea archivos
#def inicioArchivos():
path = 'repository/productos.dat'
isExist = os.path.exists(path)

if isExist == False: 
    archivo_productos = open("repository/productos.dat","wb") #Apertura
    archivo_productos.close()


path = 'repository/compras.dat'
isExist = os.path.exists(path)

if isExist == False: 
    archivo_compras = open("repository/compras.dat","wb") #Apertura
    archivo_compras.close()


path = 'repository/lineacompras.dat'
isExist = os.path.exists(path)

if isExist == False: 
    archivo_lineacompras = open("repository/lineacompras.dat","wb") #Apertura
    archivo_lineacompras.close()
#-----------------------------------------------------------------------
#Lectura inicial
#def lecturaArchivos():

archivo_compras = open("repository/compras.dat","rb+")
archivo_lineacompras = open("repository/lineacompras.dat","rb+") 
archivo_productos = open("repository/productos.dat","rb+")

if not(os.stat('repository/compras.dat').st_size == 0):
    lista_Compras = pickle.load(archivo_compras)
    
    
else: 
    print("ERROR: Archivo  C  vacio")
    lista_Compras = [] 

if not(os.stat('repository/lineacompras.dat').st_size == 0):
    lista_LineaCompra = pickle.load(archivo_lineacompras)
    
else: 
    print("ERROR: Archivo LC vacio")
    lista_LineaCompra = []

if not(os.stat('repository/productos.dat').st_size == 0):
    lista_productos = pickle.load(archivo_productos)
    
else: 
    print("ERROR: Archivo P vacio")
    lista_productos = []

   

   

  
#---------------------------------------------------------
#Escritura final

def escrituraArchivo():
    archivo_compras = open("repository/compras.dat","wb+")
    archivo_lineacompras = open("repository/lineacompras.dat","wb+") 
    archivo_productos = open("repository/productos.dat","wb+")
    
    pickle.dump(lista_Compras, archivo_compras)
    pickle.dump(lista_LineaCompra, archivo_lineacompras)
    pickle.dump(lista_productos, archivo_productos)
    

    archivo_compras.close
    archivo_lineacompras.close
    archivo_productos.close
    
   


#-------------------------------------------------
def ingresarProductos():
    os.system("cls")
    opcion = 0
    print("\n------Ingreso de productos------\n")
    while opcion != 2:
        
        codProducto = len(lista_productos)
        nombreProducto = str(input("Ingrese el nombre del producto: "))
        stockProducto = int(input("Ingrese el stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        nuevoProducto = Producto(codProducto, nombreProducto, stockProducto, precio)
        lista_productos.append(nuevoProducto) 
        opcion = int(input("\nDesea ingresar otro producto 1)Si 2) No: "))
        if opcion == 1: print("-----------------------\n")

def listaProductos():
    
    print("\n------Lista de productos------\n")
    if(bool(lista_productos)== False): 
        print("\nNo hay productos para listar\n")
        
    else:
        print("Numero"+"\t"+"Nombre"+"\t"+"Stock"+"\t"+"Precio\n")
        for p in lista_productos:
            print(str(lista_productos.index(p))+ "\t" + p.getNombre()[:10] + "\t" + str(p.getStock())+"\t" + str(p.getPrecio()))
    
    
    
    
def nuevaLineaCompra(codCompra, nl):
     
     listaProductos()
     print("\n--------------------\n")
     n = int(input("\nIngrese numero de producto: "))
             
     while 0>n or n>=len(lista_productos):
                 print("\n----Numero de producto invalido----\n")
                 n = int(input("Ingrese numero de producto: "))
                  

     cantidad = int(input("Ingrese cantidad de producto: "))  
     productoCompra = lista_productos[n]
             
             
     while (0>=cantidad or cantidad > productoCompra.getStock()):
           print("\n------La cantidad de producto ingresada no es valida------\n")
           cantidad = int(input("Ingrese cantidad de producto: "))  
                  
     productoCompra.calStock(cantidad)   
     codProducto = productoCompra.getCodigo()
     precioproducto = productoCompra.getPrecio()
     subtotal = precioproducto * cantidad
     nuevaLineaCompra = LineaCompra(nl, cantidad, subtotal, codProducto, codCompra)
     lista_LineaCompra.append(nuevaLineaCompra)
     return subtotal
     
    
def nuevaCompra(codCompra, totalprecio):
    fechahora = datetime.now()
    estado = "Pendiente"
    nuevaCompra = Compra(codCompra, fechahora, estado, totalprecio)
    print("--------------------\nTotal: $"+ str(totalprecio))
    opcionC = 3 
    opcionC = int(input("\n¿Cliente abono la compra? 1)Si 2)No: ")) 
    if(opcionC == 1):
       nuevaCompra.setEstado(1)
       print("\n-----Compra realizada-----\n")
    else: 
        print("compra no realizada") #CA:¿Que pasa si la compra no es realizada hay que re ingresar el stock?
        nuevaCompra.setEstado(0) 
    lista_Compras.append(nuevaCompra)   
    

def ok_Stock(): #Verfica el stock
    c=0
    for p in lista_productos:
        if p.getStock()!=0: c=c+1
    if c>0: return False
    else: return True    
    



def Compras(): #Cuando la cantidad es cero de un producto no se podria comprar
     os.system("cls")
     print("\n------Compras------\n")
     
     opcionC = 0
     
     while opcionC != 2:
         if(bool(lista_productos)== False) or ok_Stock() :
                 print("\n----No hay productos para vender----\n")
                 
                 os.system("Pause")
                 break
         
         codCompra = len(lista_Compras)
         totalprecio = 0
         subtotal = 0
         opcionLC = 0
         nl=0
         while opcionLC != 2:
             nl=nl+1
             subtotal = nuevaLineaCompra(codCompra, nl)
             totalprecio = totalprecio + subtotal 
             opcionLC = int(input("\nDesea ingresar otro producto a la compra 1)Si 2) No: "))
             if ok_Stock(): 
                print("\n---No hay mas productos en stock---\n") 
                break
             
         nuevaCompra(codCompra, totalprecio)
         
         opcionC = 3 
         opcionC = int(input("\nDesea ingresar otra compra 1)Si 2) No: "))
         




def listaCompras():
    os.system("cls")
    print("\n------Listado De Compras------\n")
    if(bool(lista_Compras)== False): 
        print("\nNo hay compras realizadas\n")
    else:
         print("Numero"+"\t"+"Fecha"+"\t\t"+"Hora"+"\t"+"Estado"+"\t"+"Total")
         totalganado = 0
         for c in lista_Compras:
             numeroLC = str(lista_Compras.index(c))                        
             codigoLC = str(c.getCodigo())
             estadoLC = str(c.getEstado())
             totalLC  = str(c.getTotalPrecio())
            
             f = c.getFecha()
             fecha = str(f.day) + "/" + str(f.month) + "/" + str(f.year)
             hora = str(f.hour)+":"+str(f.minute)

             totalganado =  c.getTotalPrecio() + totalganado
             print(numeroLC + "\t" + fecha + "\t" + hora + "\t" + estadoLC[:5] + "\t" + totalLC )
         print("\nTotal de compras: $"+str(totalganado)+"\n")
    
    
   
    
    
def detalleCompra():
    os.system("cls")
    print("\n------Detalle de Compras------\n")
    if(bool(lista_LineaCompra)== False):
         print("\nNo hay compras realizadas\n")
    else:
        print("Numero"+"\t"+"Cantidad"+"\t"+"SubTotal"+"\t"+"CodPro"+"\t"+"codCom\n")
        for c in lista_LineaCompra:
            nro = str(lista_LineaCompra.index(c))                        
            numeroid = str(c.getNumero())
            cant = str(c.getCantidad())
            subtotal = str(c.getSubtotal())
            codPr  = str(c.getCodProducto()) #Hay que cambiar esto por el nombre del producto
            codCo =str(c.getCodCompra())
           

            
            print(nro+"\t"+ cant+"\t\t"+subtotal+"\t\t"+codPr+"\t"+codCo) 

def updateProdcutos():
    os.system("cls")
    print("\n------Modificar Prdocutos------\n")
    upop = 0
    while upop!=2:
        if(bool(lista_productos)== False):
           print("\n----No hay productos para modificar----\n")      
           os.system("Pause")
           break
        
        listaProductos()
        print("\n--------------------\n")
        upn = int(input("\nIngrese numero de producto: "))
        while upop!=5:
            print("\nMenu de modificacion:")
            print("1)Codigo\n2)Nombre\n3)Stock\n4)Precio\n5)Salir\n")
            upop = int(input("\nIngrese opcion: "))
            if upop == 1 : 
                lista_productos[upn].setCodigo(int(input("\nIngrese nuevo codigo de producto: ")))
                print("\n-----Codigo de Producto modificado-----\n")
            if upop == 2 : 
                lista_productos[upn].setNombre(input("\nIngrese nuevo nombre de producto: "))
                print("\n-----Nombre de Producto modificado-----\n")
            if upop == 3 : 
                lista_productos[upn].setStock(int(input("\nIngrese nuevo stock de producto: ")))
                print("\n-----Stock de Producto modificado-----\n")
            if upop == 4 : 
                lista_productos[upn].setPrecio(float(input("\nIngrese nuevo precio de producto: ")))
                print("\n-----Precio de Producto modificado-----\n")
            elif upop == 5 : break
            os.system("Pause")
        upop = int(input("\n¿Desea modificar otro producto? 1)Si 2) No: "))


 #Falta la validacion si el codigo ingresado es erronio



def deletealldetalle():
    for x in lista_LineaCompra:
        lista_LineaCompra.remove(x)
    detalleCompra()
        

def deleteallCompra():
    for x in lista_Compras:
        lista_Compras.remove(x)
    listaCompras()


def deleteallproducto():
    for x in lista_productos:
        lista_productos.remove(x)
    listaProductos()

def deleteallall():
    deletealldetalle()
    deleteallCompra()
    deleteallproducto()

def deletedetallecompra(n):
        detalleCompra()
        for x in lista_LineaCompra:
            if x.getCodCompra()==n: lista_LineaCompra.remove(x)
        



def deleteCompra():
    listaCompras()
    opl=0
    while not((bool(lista_Compras)== False)):
            print("\n--------------------\n")
            n = int(input("\nIngrese numero de compra: "))

            while 0>n or n>=len(lista_Compras):
                 print("\n----Numero de compra invalido----\n")
                 n = int(input("Ingrese numero de compra: "))
            print("\nLa compra selecionada es: "+ "\n" +"Codigo:"+ str(lista_Compras[n].getCodigo())+"\n")
            opl =int(input("¿Desea borrar la compra? 1)Si 2)no: "))
            if opl==1: 
                c = lista_Compras[n].getCodigo()
                deletedetallecompra(c)
                lista_Compras.remove(lista_Compras[n])
                
                        
                        
            opl = int(input("Desea borrar otro compra 1)Si 2)No: "))
            if opl==2: break
    if ((bool(lista_Compras)== False)): os.system("Pause")





#----------------------------Esto es un poco más complejo falta devolver el stock y falta descontarlo del total de la compra-----------
def deletedetalleproductocompra(c,p):
    for x in lista_LineaCompra:
        if (x.getCodCompra()==c)and(x.getCodProducto()==p): lista_LineaCompra.remove(x)




def deletedetalle():
        detalleCompra()
        opl=0
        while not((bool(lista_LineaCompra)== False)):
            print("\n--------------------\n")
            n = int(input("\nIngrese numero de compra: "))

            while 0>n or n>=len(lista_Compras):
                 print("\n----Numero de compra invalido----\n")
                 n = int(input("Ingrese numero de compra: "))

                 
            print("\nLa compra selecionada es: "+ "\n" +"Codigo:"+ str(lista_Compras[n].getCodigo())+"\n")
            

            os.system('cls')
            listaProductos()
            np = int(input("\nIngrese numero de Producto: "))

            while 0>np or np>=len(lista_productos):
                 print("\n----Numero de producto invalido----\n")
                 np = int(input("Ingrese numero de producto: "))

            print("\nEl producto selecionado es: "+ "\n" +"Numero:"+ lista_productos[n].getNombre()+"\n")

            opl =int(input("¿Desea borrar el detalle de \nla compra? 1)Si 2)no: "))
            if opl==1: 
                c = lista_Compras[n].getCodigo()
                p = lista_productos[np].getCodigo()
                deletedetalleproductocompra(c,p)
                
                
                        
                        
            opl = int(input("Desea borrar otro producto de la compra 1)Si 2)No: "))
            if opl==2: break
        if ((bool(lista_Compras)== False)): os.system("Pause")

#-------------------------------------------------------------------------------------------






def deleteproducto():

     listaProductos()
     opl=0
     while not((bool(lista_productos)== False)):
            print("\n--------------------\n")
            n = int(input("\nIngrese numero de producto: "))

            while 0>n or n>=len(lista_productos):
                 print("\n----Numero de producto invalido----\n")
                 n = int(input("Ingrese numero de producto: "))
            print("\nEl producto selecionado es: "+ "\n" +"Nombre:"+ lista_productos[n].getNombre()+"\n")
            opl =int(input("¿Desea borrarlo? 1)Si 2)no: "))
            if opl==1: lista_productos.remove(lista_productos[n])
            opl = int(input("Desea borrar otro producto 1)Si 2)No: "))
            if opl==2: break
     if ((bool(lista_productos)== False)): os.system("Pause")
            
            

def deleteall():
    opciondMenu=0
    while opciondMenu!=5:
        os.system('cls')
        dmenu = "Menu para borrar todo\n¿Que desea borrar?:\n1)Compra\n2)Detalle de Compra\n3)producto\n4)Borrar todo\n5)Salir"
        print(dmenu)
        opciondMenu = int(input("\nIngresa opcion: "))
        if opciondMenu ==1: deleteallCompra()
        if opciondMenu ==2: deletealldetalle()
        if opciondMenu ==3: deleteallproducto()
        if opciondMenu ==4: deleteallall()
        os.system("Pause")
    

def Delete():
    opciondMenu=0
    while opciondMenu!=5:
        os.system('cls')
        dmenu = "¿Que desea borrar?:\n1)Compra\n2)Detalle de Compra\n3)producto\n4)Borrar todo\n5)Salir"
        print(dmenu)
        opciondMenu = int(input("\nIngresa opcion: "))
        if opciondMenu ==1: deleteCompra()
        if opciondMenu ==2: deletedetalle()
        if opciondMenu ==3: deleteproducto()
        if opciondMenu ==4: deleteall()
        
    
        
        
    



print("\nInicio de programa\n")
#inicioArchivos()
#lecturaArchivos()
opcionMenu = 0
while opcionMenu!=8:
    os.system('cls')
    menu = "Menu de opciones:\n1)Compras\n2)Listado de Compras\n3)Detalle de Compras\n4)Ingreso de productos\n5)Listado de productos\n6)Modificar Productos\n7)Eliminaciones\n8)Guardar y Salir"
    print(menu)
    opcionMenu = int(input("\nIngresa opcion: "))
    if opcionMenu == 1: Compras() 
    elif opcionMenu == 2: 
        listaCompras()
        os.system("Pause")
    elif opcionMenu == 3: 
        detalleCompra()
        os.system("Pause")
    elif opcionMenu == 4: ingresarProductos()
    elif opcionMenu == 5: 
        os.system("cls")
        listaProductos()  
        os.system("Pause")
    elif opcionMenu == 6: updateProdcutos()
    elif opcionMenu == 7: 
        Delete()
    else: break
     




escrituraArchivo()


print("Fin de programa")