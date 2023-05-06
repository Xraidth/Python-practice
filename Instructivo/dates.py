
""""
import datetime

date_object = datetime.date.today()
print(type(date_object))
--------------------------------------------------------------
#Crear una fecha

from datetime import date

a = date(2019, 4, 13)
print(type(a))
----------------------------------------------------------------
dividir la fecha actual

from datetime import datetime
f = datetime.now()

print(str(f.hour)+":"+str(f.minute)+":"+str(f.second))
----------------------------------------------------------------
"""
import datetime
from datetime import datetime
f = datetime.now()
print(f)

print("Dia:" + str(f.day) + "/" + str(f.month) + "/" + str(f.year) + " Hora:" + str(f.hour)+":"+str(f.minute)+":"+str(f.second))