

#Complejo 1


Registro={"Maria":"Activado","Norma":"Activado","Luis":"Desactivado","Jose":"Activado","Quevedo":"Desactivado",}

for a,b in Registro.copy().items():
   #print(Registro)
  if b=="Desactivado":
    del(Registro[a])
      
      
print("Eliminar los desactivados "+str(Registro)+"\n")


#Complejo 2

Registro={"Maria":"Activado","Norma":"Activado","Luis":"Desactivado","Jose":"Activado","Quevedo":"Desactivado",}

c=[]
for i in Registro:
 c=c+[i]
   
 
print("Ordenado por nombre "+str(sorted(c)))