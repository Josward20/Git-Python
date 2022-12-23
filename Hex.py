



p="amor"
b=0
#El ciclo desplaza cada letra
for i in p:
    b=str(ord(i))+""+str(b) #Concatena los numeros decimales
    
print(b[::-1])
c=int(b[::-1]) #Revierte el orden de salida
h=hex(c) #Combierte a hexadecimal
print(h) #IMPRIME

