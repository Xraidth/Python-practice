"""
import os
print("Hello world")
os.system('cls')
print("Termino el programa")

import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('\n'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break



def funcion(n, nombre):
    print("La edad es: "+str(n)+"el nombre es: "+str(nombre))
    r = n + 1 
    nombre = "Vacio"
    return r, nombre


l = funcion(23, "nacho")

print(type(l))
"""
