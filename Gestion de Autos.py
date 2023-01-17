
import pandas as pd

import matplotlib.pyplot as plt
 

autos=pd.read_csv("autos.csv",index_col="index")


#1 Mayor modelo de carro con mas ingreso
Masingreso=autos.groupby("model").agg({"price":sum})
mayor=Masingreso["price"].max()
print(Masingreso[Masingreso["price"]==mayor])
#-------------------Sin Modelo--------------
mayor=autos["price"].max()
precio=autos[["model","price"]]
print("\n")
print(precio[precio["price"]==mayor])

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
        return "\n El manual tuvo mas ventas\n"
    else:
        return "\n El automatico tuvo mas ventas\n"
   
     
  
   
numero=Caja(a)
print(numero)


#3 Mayor dia

dias=autos[["dateCrawled","price"]]
e=""

def di(a):
  e=a.split(" ")
  
  return e[0]
     
     
     
dias["DAY"]=dias["dateCrawled"].apply(di)

fecha=dias.groupby("DAY").agg({"price":'sum'})
maxprice=fecha["price"].max()
print(fecha[fecha["price"]>=maxprice])
print("\n \n")


#4 Mayor hora en ventas
e=""
def ho(a):
   e=a.split(" ")
   
   return e[1]

def prom(a):
    """Promedio de Ventas precio de cada hora dividido entre las 24 horas"""
    pro=a/24
    
    return pro
    pass
    
    
dias["HOUR"]=dias["dateCrawled"].apply(ho)
hora=dias.groupby("HOUR").agg({"price":'sum'})

hora["Promedio"]=hora["price"].apply(prom)
maxpro=hora["Promedio"].max()
print(hora[hora["Promedio"]==maxpro])

#-----------------------------------------------

primero=autos["dateCrawled"].max()
ultimo=autos["dateCrawled"].min()

print("\nDia que empezaron las ventas "+str(ultimo))

print("\nDia que finalizaron las ventas "+str(primero))






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

