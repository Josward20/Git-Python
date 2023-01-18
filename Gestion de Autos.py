
import pandas as pd
import datetime 
import matplotlib.pyplot as plt
 

autos=pd.read_csv("autos.csv",index_col="index")


#1 Mayor modelo de carro con mas ingreso
Masingreso=autos.groupby("model").agg({"price":sum})
mayor=Masingreso["price"].max()
print(Masingreso[Masingreso["price"]==mayor])

#-------------------En Desarrollo-------
#mayor=autos["price"].max()
#precio=autos[["model","price"]]
#print("\n")
#print(precio[precio["price"]==mayor])

#2 Ventas por tipos de autos (Automatico o Manual)
Tipo=list(autos["gearbox"])

def Caja(a):
 """Toma una lista y verfica cual de los tipos de autos fue vas vendidos"""
 b=0
 c=0 
 for i in a: # Examina la serie con un ciclo
 
  if i=="manuell":
    b=b+1   #Contador de Manual
  else:
    c=c+1   #Contador de Automaticos

    if b>c: #Pregunta simple
        return "\n El manual tuvo mas ventas\n"
    else:
        return "\n El automatico tuvo mas ventas\n"
   
     
  
   
numero=Caja(Tipo) #Se llama la funcion 
print(numero) #Ejecucion del return


#3 Mayores dias que producieron ventas

dias=autos[["dateCrawled","price"]] #Obtengo 2 Series 
e=""

def di(a): #Funcion 
  """Serapador de dia de la Horas"""
  e=a.split(" ")
  
  return e[0]  #Retorna el dia 
     
     
     
dias["DAY"]=dias["dateCrawled"].apply(di) 
#Lugo de desplazar la informacion 
fecha=dias.groupby("DAY").agg({"price":'sum'}) # Agrupo las fechas y sumo los precios
maxprice=fecha["price"].max() # Obtengo la el precio mas alto
print(fecha[fecha["price"]>=maxprice]) # Muestra el dataframe
print("\n \n")


#4 Promedio hora en ventas  // MODIFICAR 
e=""
def ho(a):
   """Serapador de hora de los dias"""
   e=a.split(" ")
   
   return e[1]

def prom(a):
    """Promedio de Ventas precio de cada hora dividido entre las 24 horas"""
    pro=a/24
    
    return pro
    pass
    
    
dias["HOUR"]=dias["dateCrawled"].apply(ho) # Se aplica la funcion ho
hora=dias.groupby("HOUR").agg({"price":'sum'}) 

hora["Promedio"]=hora["price"].apply(prom) #Aplico la funcion prom en el proce
maxpro=hora["Promedio"].max()
print(hora[hora["Promedio"]==maxpro])

#5 Cambio a Formato estandar Serie 
def cambio(a):
 """Cambia el formato de la fecha y hora"""
 Final=datetime.datetime.strptime(a,"%Y-%m-%d %H:%M:%S") #Combierto de texto a fecha
 Final2=datetime.datetime.strftime(Final,"%d-%m-%Y %I:%M:%S") #Luego normalizo
 return Final2
      


dias["Formato Estandar"]=dias["dateCrawled"].apply(cambio) # Aplico

print(dias["Formato Estandar"].head(10)) # Muestra
#-----------------------------------------------
#6 Inicio y final de las ventas

primero=dias["DAY"].max()
ultimo=dias["DAY"].min()
 
print("\nDia que empezaron las ventas "+str(ultimo))

print("\nDia que finalizaron las ventas "+str(primero))








def l():
  Masingreso=autos.groupby("model").agg({"price":sum})
  mayor=0
  for i in range(3):
    
   if i>=1:
    Masingreso.drop(Masingreso.index[Masingreso.price == mayor])
   else:
       print("------")
       
       mayor=Masingreso["price"].max()
       print(Masingreso[Masingreso["price"]==mayor])  




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

