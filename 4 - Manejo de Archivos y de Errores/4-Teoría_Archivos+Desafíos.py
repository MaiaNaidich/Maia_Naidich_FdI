#Path: ruta que referencia a la posición/localización exacta del archivo.
#Es un string que se compone por todos los nombres de las carpetas a las que tengo que acceder para llegar al archivo separadas por una barra invertida (\).
#Ruta relativa: hace más genérica la ruta, y por ende aumenta la usabilidad de mi script.
    #Desde el arhcivo donde estoy --> .\
    #Desde la carpet anterior a donde estoy --> ..\

#Desafío I
ruta="F:\\Fundamentos de Informática\\bio.txt"
open(ruta,"w")

#Desafío III
ruta="F:\\Fundamentos de Informática\\bio.txt"
with open(ruta,"w") as Bio:
    Bio.write("Hola, mi nombre es Maia.\n Estudio Analítica de Negocios en UCEMA.")

#Desafío IV
import re
path="F:\Fundamentos de Informática\4.2 Manipulacion_Archivos.txt"
abrir_archivo=open(path,"r")
texto=(abrir_archivo.read())
print(texto)
patron="-(.*)-"
print(re.search(patron,texto))

#Para pensar:
#El patrón significa encontrá todo lo que está entre guiones.