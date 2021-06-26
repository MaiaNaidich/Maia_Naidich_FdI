#Ejercicio 1
dict_muestra={1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df_muestra=pd.DataFrame(dict_muestra)
df_muestra

#Ejercicio 2
df_muestra[1].to_list()

#Ejercicio 3
df_vacio=pd.DataFrame()
def agregar_columna(header,datos):
  df_vacio[header]=datos
def agregar_fila(index,datos):
  df_vacio.loc[index]=datos

agregar_columna("Nombre",["Máximo","Maia","Mateo","Valentina","Sofía"])
agregar_columna("Apellido",["Cabezas Fernández","Naidich","Sceia","Kelly","Gramuglia"])
agregar_fila(5,["Juana","Llaneza Manzo"])

df_vacio

#Ejercicio 4
dict4={"Producto":["Mochila","Mochilita","Bolso","Bolsito","Cartera","Carterita","Billetera","Monedero"],
       "Color":["Azul","Celeste","Negro","Gris","Marrón","Beige","Verde Oscuro","Verde Claro"],
       "Precio":[500,250,1000,750,1500,1250,1100,400]}
df_original=pd.DataFrame(dict4)

df_original

def eliminar_filas(n):
  df_sin_filas=df_original.tail(len(df_original)-n)
  print(df_sin_filas)

eliminar_filas(3)

df_original #se imprime lo mismo que en la fila 20.

#Ejercicio 5
def chequear_columna(columna,df):
  try:
    print(df[columna])
  except:
    print("No hay una columna con ese nombre en el Data Frame ingresado")

chequear_columna("Producto",df_original)
chequear_columna("Material",df_original)

#Ejercicio 6
alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6b_dict={"Nombre":["Luis","Martina","Camila"],"Nota Matemática":[9,7,5.5],"Nota Lengua":[10,8,7],"Nota Baile":[9,8,7]}

alumnos6a_df=pd.DataFrame(alumnos6a_dict)
alumnos6b_df=pd.DataFrame(alumnos6b_dict)

alumnos_sexto_eje=pd.concat([alumnos6a_df,alumnos6b_df],ignore_index=True,axis=0)

alumnos_sexto_eje

#Ejercicio 7
alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6a_df=pd.DataFrame(alumnos6a_dict)

alumnos6a_df

nota_ingles6a=[7,6,8]
alumnos6a_df["Nota Inglés"]=nota_ingles6a

alumnos6a_df

#Ejercicio 8
alumnos6a_dict={"Nombre":["Juana","Pedro","Carlos"],"Nota Matemática":[10,8.5,6],"Nota Lengua":[9,7,8],"Nota Ed. Física":[7,7,8]}
alumnos6b_dict={"Nombre":["Luis","Martina","Camila"],"Nota Matemática":[9,7,5.5],"Nota Lengua":[10,8,7],"Nota Baile":[9,8,7]}

alumnos6a_df=pd.DataFrame(alumnos6a_dict)
alumnos6b_df=pd.DataFrame(alumnos6b_dict)

alumnos_sexto_eje=pd.concat([alumnos6a_df,alumnos6b_df],ignore_index=True,axis=0,join="inner")

alumnos_sexto_eje