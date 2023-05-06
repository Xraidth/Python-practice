

#Creacion de clases
from math import prod


class Producto():
        #Variables de clase
    def __init__(self, codigo, nombre, stock, precio):
        #Variables de instancia
         self.codigo = codigo
         self.nombre = nombre
         self.stock = stock
         self.precio = precio
    def get_nombre(self):
        return self.nombre
    def get_stock(self):
        return self.stock

producto = Producto(1,"Aceitunas", 5, 200)
productolista= [str(producto.codigo), producto.nombre, str(producto.stock), str(producto.precio)]




print("El nombre del producto es: " + str(producto.get_nombre()))
