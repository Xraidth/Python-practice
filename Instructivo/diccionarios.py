#Clave:valor
#Nunca hay dos claves iguales
diccionario = {"Argentina":"Buenos Aires", "Brazil":"Rio"}  
diccionario["Italia"] = "Roma"   #Para modificar se usa el mismo
print(diccionario["Argentina"])
print(diccionario)
del diccionario["Brazil"] 
print(diccionario) #Se pueden poner listas o tuplas dentro de los diccionarios