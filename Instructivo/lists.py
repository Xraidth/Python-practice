#Listas varios valores (diferentes valores/expancion dinamica como registro)
#Comiezan en 0
#Lista[0:3] Porcion de elementos
#Lista[:3] Los 3 primeros
#Lista[1:3] Arranca en el uno y termina en el 3
#Lista[2] Dos ultimos elementos



"""
lista = []
lista.append("Objeto añadido")                  #Añade un elemento
lista.insert(1,"Objeto añadido con insert")     #Inserta un elemento en un lugar especifico
lista.extend(["Pepe","Maria", "Marco"])         #Concatena una lista con la lista que self
print(lista.index("Pepe"))                      #Devuelve el numero de la lista en donde se encuentra
print( "Pepe" in lista)                         #Muestra T/F si contiene un elemento en una lista
lista.remove("Pepe")                            #Elimina a pepe se puede poner 2
lista.pop()                                     #Elimina el ultimo elemento de una lista
lista2 = lista+ ["Maria"]                       #Suma listas
lista = lista2 * 3 
print(lista)
list=["1","2","3"]
print(len(list))
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




def listar(l, t):
    print("\n------Lista de "+ t.className() +"------\n")
    if l == False: 
        print("\nLista de" + t.className()+" vacia\n")
    else:
        t.classCampos()
        for p in l:
            p.show_me(l.index(p))
            
def buscaCod(l,c): #Busqueda secuencial
     r = False
     
     for x in l:
        if x.getCodigo()==c: 
            r = True
            p = x
            break
     if r: return p
     else: return False
                 



p = Producto(22, "Leche", 10, 20.5)
p2 = Producto(23, "Carne", 23, 200.5)
p3 = Producto(24, "Huevo", 5, 27.5)

list = [] #[p, p2, p3]
#print(buscaCod(list, 50))
#listar(list, Producto)

if list == True: print("")
"""
