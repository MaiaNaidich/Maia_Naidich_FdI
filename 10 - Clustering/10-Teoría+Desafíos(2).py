#Escalado de los datos: nos sirve para no infra- o sobre- valorar ninguna variable.
#Hay variables que, por su naturaleza, toman valores mucho más grandes que otros.

#Normalizado de los datos: cómo se comporta con respecto a la distribución de los puntos.
#Conocer no solo el valor en sí mismo, sino también cuáto se aleja de la media.

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
iris_escaleado=scaler.fit_transform(iris)
#A partir de ahora siempre trabajo con este data frame.

#El método K-means va a buscar la mejor forma de separar los datos en grupos.
#Utiliza la varianza interna para asegurar que los puntos que componen un grupo tengan la menos distancia entre sí.
#1. Conjutno de datos inicial.
#2. Intuitivamente, le decimos a K-means cuántos grupos creemos que hay --> K = número de grupos.
#3. Al azar selecciona K puntos (centroides) y los agrupa a los puntos que tengan la menor distancia.
#4. Calcula la media de los datos que hay en cada grupo.
#5. Se reasignan los centroides según la media calculada en el paso anterior.
#6. Se vuelven a separar los grupos según ese nuevo centroide.
#7. Se repiten los pasos 4, 5 y 6 hasta que hace la mejor separación de grupos posible.
#Cuando calcula la media del grupo y coincide con el valor del centroide, quiere decir que están agrupados de la mejor forma posible.
#También podemos ponerle un límite de iteraciones.

from sklearn.cluster import KMeans
k = K  #definimos la cantidad de clusters.
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones.
kmeans.fit(iris_escaleado)  #aplicamos el método a nuestros datos.

print(kmeans.labels_) #Muestra a qué valor le adjudicó cada etiqueta.

print(kmeans.cluster_centers_ ) #Muestra en qué punto colocó los centroides.

colores = ["red", "green", "blue"]
g_grupos = sns.scatterplot(x = iris_escaleado[:,2], y = iris_escaleado[:, 3], hue = kmeans.labels_, palette = colores, alpha = 0.5)
#Nos muestra el gráfico de dispersión con los puntos pintados de distintos colores según el grupo al que pertenecen.

g_centroides = sns.scatterplot(x = kmeans.cluster_centers_[:,2], y = kmeans.cluster_centers_[:,3], zorder = 10, palette = colores, hue = [0, 1, 2], legend = False, marker=6, s=200)
#Nos muestra dónde están los centroides.
#Si se ejecutan estas últimas dos líneas juntas, muestra los grupos y sus respectivos centroides en el mismo gráfico.

#Inercia: dispersión de los datos alrededor del centroide.
kmeans.inertia_

#Desafio VI
inertias_dict={}
inertias_dict["K"]=[]
inertias_dict["Inertia"]=[]
for i in range(15):
  k = i + 1
  kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeans.fit(iris_escaleado)
  inertias_dict["K"].append(k)
  inertias_dict["Inertia"].append(kmeans.inertia_)
print(inertias_dict)

inertias_df=pd.DataFrame(inertias_dict)
inertias_df

#Desafío VII
sns.pointplot(data=inertias_df,x="K",y="Inertia")

#Índices de cohesión:
  #Inertia --> devuelve un único valor.
  #Sillhoutte --> devuelve un valor para cada punto.

from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette.
#Calculamos el promedio del silhouette de todos.
silhouette_avg = silhouette_score(iris_escaleado, kmeans.labels_)
#Calculamos el silhouette de cada punto.
sample_silhouette_values = silhouette_samples(iris_escaleado, kmeans.labels_)

import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
import numpy as np
def graficarSilhouette (k, labels, sample_silhouette_values, silhouette_avg):
  fig, ax1 = plt.subplots(1, 1)
  y_lower = 10
  for i in range(k):
      ith_cluster_silhouette_values = \
          sample_silhouette_values[labels == i]

      ith_cluster_silhouette_values.sort()

      size_cluster_i = ith_cluster_silhouette_values.shape[0]
      y_upper = y_lower + size_cluster_i

      color = cm.nipy_spectral(float(i) / k)
      ax1.fill_betweenx(np.arange(y_lower, y_upper),
                        0, ith_cluster_silhouette_values,
                        facecolor=color, edgecolor=color, alpha=0.7)
      ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
      y_lower = y_upper + 10

  ax1.set_title("Plot del silhouette de cada cluster")
  ax1.set_xlabel("Coeficiente de silhouette")
  ax1.set_ylabel("Etiqueta del cluster")
  ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
  ax1.set_yticks([]) 

graficarSilhouette (k, kmeans.labels_, sample_silhouette_values, silhouette_avg)

#El mejor valor al que puedo llegar es 1 y el peor es -1.
#Permite ver cuán cohesivos son los grupos.

#Desafío IX
silhouette_avg=[]
for k in range(2,11):
  kmeanss=KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeanss.fit(iris_escaleado)
  silhouette_avg.append(silhouette_score(iris_escaleado,kmeanss.labels_))

#Desafío X
df_s=pd.DataFrame({"K":list(range(2,11)),"SilhouettePromedio":silhouette_avg})
g_s=sns.pointplot(data=df_s,x="K",y="SilhouettePromedio")

#Una distribución normal puede ser descrita únicamente por su media y su desvío estándar.

#El p-value es la probabilidad de que un valor estadístico calculado sea posible dada una hipótesis nula que es cierta.
#Si es mayor a 0,05 está ok.