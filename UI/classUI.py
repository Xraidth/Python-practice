
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

