pd.merge()
#how: indica la manera de unión de los data frames, por defecto es “inner” (intersección). La otra opción es outer.
#on: a qué columna le da más peso --> pone todos los datos de esa columna, sin importar si tiene NaN (es como hacer obligatoria esa columna).
#on: indica en base a qué columna se van a unir los data frames. Esta columna tiene que estar presente en ambos data frames.
#left_on: nombre de la columna de los datos de la izquierda el cual se va a usar para unir los data frames. 
     #Se utiliza cuando no coincide ninguna columna entre los dos dataframes.
#right_on: igual al anterior, pero con una columna de los datos de la derecha. Ambos tienen que explicitarse.

pf.df.set_index()
#Si no le indicamos cuál queremos que sea el índice, se ponen números desede el cero.
#También se pueden pasar índices múltiples.

pd.df.sort_values()
#Permite ordenar los valores.

pd.df.to_csv
#Sirve para guardar nuestro Data Frame como un archivo de formato csv.