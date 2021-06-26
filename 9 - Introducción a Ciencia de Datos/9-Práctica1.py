#Ejercicio 1
lista1=[3, 7, 12, 15, 21]
lista2=[1, 4, 10, 14, 19]
serie1=pd.Series(lista1)
serie2=pd.Series(lista2)

suma=(serie1+serie2)
print(suma)

resta=(serie1-serie2)
print(resta)

producto=(serie1*serie2)
print(producto)

division=(serie1/serie2)
print(division)

#Ejercicio 2
lista3=[3, 7, 9, 14, 25]
lista4=[1, 7, 10, 16, 19]
serie3=pd.Series(lista3)
serie4=pd.Series(lista4)

es_mayor=serie3>serie4
print(es_mayor)

es_igual=(serie3==serie4)
print(es_igual)

es_menor=serie3<serie4
print(es_menor)

#Ejercicio 3
dict3 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
serie=pd.Series(dict1)
print(serie)

#Ejercicio 4 (falta hacerle algunas correcciones para que se puedan repetir elementos en una misma lista)
dict1 = {"a": [1,3,5,2], "b": [4,2,3,5]}
dict2 = {}
for clave in dict1.keys():
  dict2[clave]=[]
  for numero in dict1[clave]:
    if dict1[clave].index(numero)%2==0:
      dict2[clave].append(numero**dict1[clave][(dict1[clave].index(numero))+1])
print(dict2)
df3=pd.DataFrame(dict2)
df3

#Ejercicio 5
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df1=pd.DataFrame(datos_ejemplo)
df2=pd.DataFrame(labels)
df1

#Ejercicio 6
df1.info()

#Ejercicio 7
import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df1_7=pd.DataFrame(data=datos_ejemplo,index=labels)
df1_7.head(3)

#Ejercicio 8
df1_8=pd.DataFrame(data=[df1_7["nombre"],df1_7["puntaje"]]).transpose()
df1_8

#Ejercicio 9
dict1_9={"NOMBRE":[],"longitud":[]}
for nombre in list(df1_7["nombre"]):
  dict1_9["NOMBRE"].append(nombre.upper())
for NOMBRE in dict1_9["NOMBRE"]:
  dict1_9["longitud"].append(len(NOMBRE))
df1_9=pd.DataFrame(dict1_9)