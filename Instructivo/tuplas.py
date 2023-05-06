#No se pueden indexar 
#Se ejecutan mas rapido
#Parentesis opcional

tupla = (1, 2, 3, 3)
tupla2 =(1,) #tupla unitaria
tupla3 ="L" 
lista = list(tupla) #Convierte una tupla en una lista
tupla = tuple(lista) #Convierte la lista en una tupla
print(tupla[2])         #Seleccionar un elemento
print(1 in tupla)       #Esta dentro de la tula
print(tupla.count(3))   #Cuantas veces esta la tupla
print(len(tupla))       #Cantidad de elementos
