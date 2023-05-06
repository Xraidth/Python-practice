"""
from tkinter import *




root=Tk()


root.title("Tienda Virtual")#Titulo de la ventana
#root.resizable(1,0) impedir el redimencionamiento
root.iconbitmap("iconoroot.ico")
root.geometry('650x452+420+200')
root.resizable(0,0)
root.config(bg="white")

i=0

def incre():
    global i
    i=i+1   
    print(i)

root.after(2000,lambda:incre())
rec = Frame(root, height=10,width=10, bg="red")
rec.place(relx=0.5,rely=0.5)
rec.move()
root.mainloop()
"""

# imports every file form tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *
 
class GFG:
    def __init__(self, master = None):
        self.master = master
         
        # to take care movement in x direction
        self.x = 1
        # to take care movement in y direction
        self.y = 0
 
        # canvas object to create shape
        self.canvas = Canvas(master)
        # creating rectangle
        self.rectangle = self.canvas.create_rectangle(
                         10, 10, 50, 50, fill = "black")
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()
     
    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle, self.x, self.y)
 
        self.canvas.after(10, self.movement)
     
    # for motion in negative x direction
    def left(self, event):
        
        self.x = -5
        self.y = 0
     
    # for motion in positive x direction
    def right(self, event):
        
        self.x = 5
        self.y = 0
     
    # for motion in positive y direction
    def up(self, event):
        
        self.x = 0
        self.y = -5
     
    # for motion in negative y direction
    def down(self, event):
        
        self.x = 0
        self.y = 5
 
if __name__ == "__main__":
 
    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()
    gfg = GFG(master)
 
    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
     
    # Infinite loop breaks only by interrupt
    mainloop()