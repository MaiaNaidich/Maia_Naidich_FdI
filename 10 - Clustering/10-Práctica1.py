import pandas as pd

datos=pd.read_csv("F:\\Fundamentos_de_Informática\\Datos.csv")
datos

datos.info()

datos_dropna=datos.dropna()
datos_dropna.info()
datos_dropna.describe()

datos_filtro_altura=datos_dropna[datos_dropna["Altura"]<2.3]
datos_filtro_altura.describe()

datos_filtro_altura.plot.scatter("Nombres","Sueldo")
datos_ok=datos_filtro_altura[datos_filtro_altura["Sueldo"]<200000]
datos_ok.describe()

datos_ok["Sueldo"].mode()
datos_ok["Altura"].mode()

datos_ok["Sueldo"].plot.density()
datos["Altura"].plot.density()