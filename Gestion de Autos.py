
import pandas as pd

import matplotlib.pyplot as plt
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
   
   
autos=pd.read_csv("autos.csv",index_col="index")


#1 Mayor modelo de carro con mas ingreso
#Masingreso=autos.groupby("model").agg({"price":sum})
#mayor=Masingreso["price"].max()
#print(Masingreso[Masingreso["price"]==mayor])

#2 Ventas por tipos de autos (Automatico o Manual)
a=list(autos["gearbox"])

def Caja(a):
 """Toma una lista y verfica cual de los tipos de autos fue vas vendidos"""
 b=0
 c=0 
 for i in a:
 
  if i=="manuell":
    b=b+1
  else:
    c=c+1

    if b>c:
        return "El manual tuvo mas ventas"
    else:
        return "El automatico tuvo mas ventas"
   
     
  
   
numero=Caja(a)
print(numero)









#Totalautos=autos.groupby("name").mean()

#Totalautos=autos.groupby("name").agg({"price":sum})
    
#print(Totalautos)

#autos.plot(kind="scatter",x="powerPS", y="kilometer")
#plt.show()

#print(autos[(autos["price"]>40000) & (autos["index"]>300000)].head())

#print(autos.loc[[5,7],"price"])  

#print(autos.loc[[5,7]])  

#print(autos.iloc[1:4])

#print(autos.describe())   

#precios=autos["price"]>1000

#print(precios["price"].head())

