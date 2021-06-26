import pandas as pd
import seaborn as sns
import sklearn

#Machine learning: a partir de un set de datos, entrenar a la máquina para que detecte patrones en esos datos.
#Clustering: tengo un set de datos y quiero ver si esos datos comparten características entre sí.
#No sé a qué grupo pertenece cada dato y quiero separarlos.
#Pensar un criterio para separar los datos, en base a las variables/características que tengo de esos datos.
#Forma exploratoria de analizar los datos.

iris=pd.read_csv("F:\\Fundamentos_de_Informática\\iris_data.txt",sep="\t")
iris

#Desafío I
import pandas as pd
iris=pd.read_csv("F:\\Fundamentos_de_Informática\\iris_data.txt",sep="\t")
iris.columns

#Desafíos II y III
import matplotlib.pyplot as plt
g_petal_length = sns.histplot(data = iris, x = "petal.length", binwidth=0.25, kde = True) #gráfico de barras con función de distribución.
plt.show()
g_petal_width = sns.histplot(data = iris, x = "petal.width", binwidth=0.25, kde = True)
plt.show()
g_sepal_length = sns.histplot(data = iris, x = "sepal.length", binwidth=0.25, kde = True)
plt.show()
g_sepal_width = sns.histplot(data = iris, x = "sepal.width", binwidth=0.25, kde = True)
plt.show()
#Con estos gráficos podemos tener una priemra intuición de cómo separar los datos en grupos, en base a su distirbución.

#Datos homogéneos: son todos iguales --> no los puedo separar en grupos.

#Desafío IV
g = sns.pairplot(iris) #nos muestra un montón de gráficos que van a ser útiles para hacer clustering --> gráficos de dispersión y de barras --> relación entre todas las variables que teníamos.

#Hay que establecer un criterio para determinar cuán similares son dos datos.
#La clasificación no es una verdad absoluta, es subjetiva --> depende del criterio.

#La distancia entre los puntos de un gráfico de dispersión, nos va a ayudar a saber si existe algún posible agrupamiento entre los datos, porque es un indicador de su similitud.
#¿Cómo calculamos la distancia? --> hay distintas formas de calcular las distancias, y por ende, distintas formas de calcular la similitud.

#Último paso previo al clustering --> normalizado y escalado de los datos --> análisis multivariado.