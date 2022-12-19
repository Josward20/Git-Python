
#Diccionario dentro de otro Diccionario
diccionario={1:{"Nombre":"Josward","edad":20,"Titulos":2},2:{"Nombre":"Maria","edad":22,"Titulos":3}}

print("Mostrar "+str(diccionario))

#Diccionario por Indice
print("\n Mostrar por indice"+str(diccionario[2]))

#Diccionario interno
print("\n Mostrar Diccionario interno ("+str(diccionario[1]["Nombre"])+")")

#Si no existe el indice
print("\n"+str(diccionario.get(3,"Persona no encontrada")))

#Pregunta True o False
print("\n"+str(3 in diccionario))

#Mostrar claves
print("\n"+str(diccionario.keys()))

#Mostrar valor
print("\n"+str(diccionario.values()))
print("\n"+str(diccionario[1].values()))

print ("\n"+str(diccionario.items()))

#ZIP