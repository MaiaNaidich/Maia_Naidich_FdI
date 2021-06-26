#Ejercicio 1
diccionario1={}
for numero in range(1,16):
    diccionario1[numero]=numero*numero
print(diccionario1)

#Ejercicio 2
suma=0
for numero in diccionario1.values():
  suma+=numero
suma

#Ejercicio 3
strings=["pez","vaca","pollo"]
longitudes=[]
for lugar in range(len(strings)):
  longitudes.append(len(strings[lugar]))
longitudes

#Ejercicio 4
lista_mixta=[2,"Andy","Pepa",3,5]
cantidad_int=0
lista_strings=[]
for elemento in lista_mixta:
  if type(elemento)==int:
    cantidad_int+=1
  elif type(elemento)==str:
    e_nuevo=elemento.replace("a","u")
    e_final=e_nuevo.replace("A","U")
    lista_strings.append(e_final)