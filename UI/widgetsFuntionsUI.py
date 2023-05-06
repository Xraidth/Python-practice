def removegrid(widgets): 
	for x in widgets:
		x.grid_remove()
		
def forgetgrid(widgets): 
	for x in widgets:
		x.grid_forget()
		
def packforget(widgets):
		for x in widgets:
			x.pack_forget()

def destroylist(widgets):
		for x in widgets:
			x.destroy()


