import pandas as pd

personas=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\personas.csv",sep=";")
personas

ref_tipo_condicion_docente=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_tipo_condicion_docente.csv",sep=";")
ref_clase_cargo=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_clase_cargo.csv",sep=";")
ref_tipo_dedicacion_horaria_semanal=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_tipo_dedicacion_horaria_semanal.csv",sep=";")
ref_categoria_conicet=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_categoria_conicet.csv",sep=";")
ref_tipo_personal=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_tipo_personal.csv",sep=";")
ref_disciplina=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_disciplina.csv",sep=";")
ref_grado_academico=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_grado_academico.csv",sep=";")
ref_sexo=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\ref_sexo.csv",sep=";")

personas_mas_ref=personas.join(ref_tipo_condicion_docente,lsuffix="_personas",rsuffix="_ref").join(ref_clase_cargo,lsuffix="_personas",rsuffix="_ref").join(ref_tipo_dedicacion_horaria_semanal,lsuffix="_personas",rsuffix="_ref").join(ref_categoria_conicet,lsuffix="_personas",rsuffix="_ref").join(ref_tipo_personal,lsuffix="_personas",rsuffix="_ref").join(ref_disciplina,lsuffix="_personas",rsuffix="_ref").join(ref_grado_academico,lsuffix="_personas",rsuffix="_ref").join(ref_sexo,lsuffix="_personas",rsuffix="_ref")
personas_mas_ref

import seaborn as sns
sns.heatmap(personas.isnull(), cmap="viridis")

#Desafío I
for columna in personas.columns.values:
  print(personas[columna].isnull().value_counts()/len(personas[columna]))

#Desafío II
import pandas as pd
personas=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\personas.csv",sep=";")
nulos=dict(personas.isna().sum())
columnas=list(personas.columns.values)
for columna in columnas:
  print("La columna de nombre "+str(columna)+" tiene un "+str(nulos[columna]/(len(personas.index)*100))+"% de datos nulos")

#Desafío III
import pandas as pd
personas=pd.read_csv("F:\\Fundamentos_de_Informática\\Personas\\personas.csv",sep=";")

personas.info()
columnas=list(personas.columns.values)
columnas_numericas=columnas.remove("seniority_level")

personas_mean=pd.DataFrame()
for columna in columnas_numericas:
  personas_mean[columna]=personas[columna].fillna(personas[columna].mean())
personas_mean.info()

personas_mode=pd.DataFrame()
for columna in columnas:
  personas_mode[columna]=personas[columna].fillna(str(personas["anio"].mode())[0])
personas_mode.info()

#Para pensar:
personas.describe()