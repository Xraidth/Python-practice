import os
import pickle 

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
    
   
