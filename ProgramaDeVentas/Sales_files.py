#-------------Libreries------------------
from cgitb import text
from genericpath import exists
from io import open
from json import load;
import os
import errno
import pickle 
#----------------------------------------



"""

#----------------Habilitar en algun momento------------

#Creacionde carpeta del repositorio 
try:
    os.mkdir('repository')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

"""

"""
class Producto():
        #Variables de clase
    def __init__(self, codigo, nombre, stock, precio):
        #Variables de instancia
         self.codigo = codigo
         self.nombre = nombre
         self.stock = stock
         self.precio = precio
    def getCodigoProducto(self):
        return self.codigo
    def getPrecioProducto(self):
        return self.precio
       


productos = open("repository/productos.bat","r+", encoding="utf-8") #Apertura 

producto = ["0000", "Leche", str(10), str(3)]
productos.writelines(producto) 
l = productos.readlines()
print(l)




productos.close #Cierre

#Crear archivo binario
archivo_productos = open("repository/productos.dat","wb") #Apertura
archivo_productos.close() 

#Creo una lista dentro del archivo
archivo_productos = open("repository/productos.dat","rb+") #Apertura
lista_productos =[]
pickle.dump(lista_productos, archivo_productos)
archivo_productos.close() 




archivo_productos = open("repository/productos.dat","rb+") #Apertura
lista_productos = pickle.load(archivo_productos)
objeto_producto = Producto(1, "peregil", 1, 20)
lista_productos.append(objeto_producto)
pickle.dump(lista_productos, archivo_productos)
archivo_productos.close()

archivo_productos = open("repository/productos.dat","wb+") #Apertura
objeto_producto = Producto(1, "leche", 3, 200.5)
lista_productos = [objeto_producto]
pickle.dump(lista_productos, archivo_productos)
archivo_productos.close()

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
    



#Cargador de Productos
archivo_productos = open("repository/productos.dat","rb+") #Apertura
lista_productos = pickle.load(archivo_productos)
print("Codigo\tNombre\tStock\tPrecio")

for x in lista_productos:
    print(str(x.getCodigo())+"\t"+ x.getNombre()+"\t"+ str(x.getStock())+"\t"+ str(x.getPrecio()))

objeto_producto = Producto(2, "peregil", 1, 20)
lista_productos.append(objeto_producto)

print("\n\n\n\n")

for x in lista_productos:
    print(str(x.getCodigo())+"\t"+ x.getNombre()+"\t"+ str(x.getStock())+"\t"+ str(x.getPrecio()))

pickle.dump(lista_productos, archivo_productos)
print("cargado exitoso")
archivo_productos.close()


#Mostrar Productos

if os.stat('repository/productos.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    archivo_productos = open("repository/productos.dat","rb+") #Apertura
    lista_productos_muenstra = pickle.load(archivo_productos)
    print(lista_productos_muenstra)
    print("Codigo\tNombre\tStock\tPrecio")
    for x in lista_productos_muenstra:
        print(str(x.getCodigo())+"\t"+ x.getNombre()+"\t"+ str(x.getStock())+"\t"+ str(x.getPrecio()))
    archivo_productos.close()



#Funciona
archivo_productos = open("repository/productos.dat","rb+") #Apertura
lista_productos = pickle.load(archivo_productos)
objeto_producto = Producto(3, "Auto", 1, 200)
lista_productos.append(objeto_producto)
pickle.dump(lista_productos, archivo_productos)
archivo_productos.close()
"""


