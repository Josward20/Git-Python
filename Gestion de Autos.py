
import csv 

cont=0;


def Fecha(a):
     #Normalizar a la zona horaria Venezolana
  b=a.split(" ")
  fecha=b[0].split("-")
  print(str(fecha[2]+"-"+fecha[1]+"-"+fecha[0]))
  hora(b[1])

def hora(a):
   
  h=a.split(":")

  if int(h[0])>12:
   b=int(h[0])-12
   print(str(b)+":"+str(int(h[1]))+":"+str(int(h[2])))
  elif int(h[0])==00:
     print("1"+":"+str(int(h[1]))+":"+str(int(h[2])))
  else:
   print(a)  
   
   
   
with open("autos.csv") as arch:
   
   leer = csv.reader(arch)
   for linea in leer:
       cont+=1
       print( linea[0])


   







 



    
   



