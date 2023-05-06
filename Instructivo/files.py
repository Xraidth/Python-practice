from cgitb import text
from fileinput import close #Seguimiento de excrips
from genericpath import exists #Existencia de archivos
from io import open; #Manejo de E/S
import os    #Manejo de sistema operativo
import errno #Manejo de errores
import pickle 
"""
----------------------------------------- 
# (r lectura) (w escritura) (a apertura) (r+ lectura y escritura)
archivo_txt = open("repository/archivo.txt","w", encoding="utf-8") #Apertura 
frase = "Hola mundo"
archivo_txt.write(frase) #Escritura
archivo_txt.close #Cierre

#Importante: si abres un archivo con (w escritura) y luego lo cierras se borra el contenido dentro pero si lo abres con (a apertura) no 

-----------------------------------------
#Lectura
archivo_txt = open("archivo.txt","r")
texto = archivo_txt.read()
archivo_txt.close
print(texto)

---------------------------------------
#Lectura en lista
archivo_txt = open("archivo.txt","r")
lineas_texto = archivo_txt.readlines()
archivo_txt.close
print(lineas_texto)

#Lectura de un elemento de una lista (sirve para buscar)
archivo_txt = open("archivo.txt","r")
lineas_texto = archivo_txt.readlines()
archivo_txt.close
print(lineas_texto[numero a buscar])


#Lectura
archivo_txt = open("archivo.txt","a")
texto = archivo_txt.write("\n Es un buen momento" )
archivo_txt.close
--------------------------------------
.seek() #Moverse en el archivo 
len longitud de algo


------------------------------------------------
#Funcion para saber si una ruta especifica dentro del directorio de la pc
import os
path = 'C:/Users/usuario/Desktop/Phython/ERP/productos.txt'
   
# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)
---------------------------------------------------------------
#Crear una carpeta 
os.mkdir('C:\')

---------------------------------------------------------------
#Forma màs completa de crear una carpeta preguntando si existe

import os
import errno
try:
    os.mkdir('dir1')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# funcion para saber si el contenido del archivo esta vacio o no

if os.stat('repository.archivo').st_size == 0:
   print('El archivo esta vacío.')


-------------------------------------
#Archivos binarios

#Crear archivo binario
archivo_productos = open("repository/productos.dat","wb") #Apertura
archivo_productos.close()

lista = []    
archivo_nuevo = open("archivos","wb") #Apertura
pickle.dump(lista, archivo_nuevo)     #volcado
archivo_nuevo.close()                 #Cerrado

archivo_viejo = open("archivos","rb") #Apertura
lista = pickle.load(archivo_viejo)    #Cargado
archivo_viejo.close                    #Cerrado
"""

"""
#------------------------
#----Funciona bien-------
#------------------------
archivo_productos = open("repository/productos.dat","ab+")
listaNP = ["Objeto"]
pickle.dump(listaNP, archivo_productos)
archivo_productos.close

if os.stat('repository/productos.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    archivo_productos = open("repository/productos.dat","rb") #apertura
    listaP = pickle.load(archivo_productos)
    print(listaP)
    archivo_productos.close
"""


"""
#Grabar
archivo_productos = open("repository/productos.dat","rb+")
listaNP = ["Objeto"]
pickle.dump(listaNP, archivo_productos)

#Leer
#Cuidado antes de leer preguntar si esta vacio sino te tira un error
if os.stat('repository/productos.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    #archivo_productos = open("repository/productos.dat","rb") #apertura
    listaP = pickle.load(archivo_productos)
    print(listaP)
    archivo_productos.close
"""




"""

#Lectura inicial

archivo_compras = open("repository/productos.dat","rb+")
archivo_lineacompras = open("repository/productos.dat","rb+")
archivo_productos = open("repository/productos.dat","rb+")



if os.stat('repository/compras.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    listaP = pickle.load(archivo_compras)
    print(listaP)
    archivo_compras.close


if os.stat('repository/lineacompras.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    listaP = pickle.load(archivo_lineacompras)
    print(listaP)
    archivo_lineacompras.close

if os.stat('repository/productos.dat').st_size == 0:
   print('El archivo esta vacío.')
else:
    listaP = pickle.load(archivo_productos)
    print(listaP)
    archivo_productos.close
  
"""





"""

  
#Lectura inicial

archivo_compras = open("repository/productos.dat","rb+")
archivo_lineacompras = open("repository/productos.dat","rb+")
archivo_productos = open("repository/productos.dat","rb+")

if not(os.stat('repository/compras.dat').st_size == 0):
    listaP = pickle.load(archivo_compras)
    print(listaP)
    archivo_compras.close

if not(os.stat('repository/lineacompras.dat').st_size == 0):
    listaP = pickle.load(archivo_lineacompras)
    print(listaP)
    archivo_lineacompras.close

if not(os.stat('repository/productos.dat').st_size == 0):
    listaP = pickle.load(archivo_productos)
    print(listaP)
    archivo_productos.close
    
"""





