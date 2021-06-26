#Bibliotecas
#Pandas: nos permite trabajar con datos estructurados, que se puedan presentar y separar de algún modo como tabla.
#Nos permite cargar datos de distitnas fuentes (csv = comma separated values - cada línea es una lista).
import pandas as pd
import seaborn as sns
import scipy.stats as ss

#Lote de datos que vamos a usar en las próximas clases:
https://datasets.datos.mincyt.gob.ar/dataset/personal-de-ciencia-y-tecnologia/archivo/11dca5bb-9a5f-4da5-b040-28957126be18

#Necesitamos que los datos sean abiertos.

#Declarar un data frame. 
#Si se ingresa la data manualmente. La data va en forma de diccionario.
df = pd.DataFrame(data ={})
#Cargar los datos desde un archivo.
path="F:\\Fundamentos_de_Informática\\Introducción_Ciencia_de_Datos_DataFrames\\personas_2011.csv"
df = pd.read_csv(path,sep=";")
#Por default, el separador es una coma (,).

df.head() #imprime un pedacito del data frame. Por defecto es 5, pero podemos pasarle el número de líneas que queremos que nos lea.
df.info() #para cada columna nos indica cuántos son los datos no nulos y que tipo de datos son.
df.describe() #nos da datos estadísticos (media, mediana, cuartiles, máximo, mínimo, etc.)

pd.concat([df1,df2]) 
#Por defecto une según el eje de las columnas (axis=0). Si quiero unirlo seún el eje de las filas poner axis=1.
#El método concat muestra, por defecto, la unión de los data frame. Si se quisiera mostrar la intersección hay que poner escribir parámetro join="inner".
#Otro método para agregar data frames es append:
df1.append(df2) == pd.concat([df1,df2])
#La diferencia es que el método append pertenece al data frame, mientras que concat no.
#El resultado de append hay que guardarlo en una nueva variable.
#El parámetro ignore_index, tanto en concat como en append, nos permite olvidar los índices que estaban en los data frames originales cuando ignore_index=True.

df.to_dict() #pasar un data frame a un diccionario.
s.to_list() #pasar una serie a una lista. Las series también se pueden transformar a diccionarios.
#Aunque los diccionarios no se pueden convertir en listas, sí sus columnas se pueden convertir en listas.