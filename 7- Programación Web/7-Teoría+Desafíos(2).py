#Web: red interconectada de todos los archivos (páginas) que están en las computadoras.
#Página Web: se accede a través de un navegador, usando Internet --> archivo HTML: archivo de hipertexto --> separado por etiquetas que determinan el contenido.
    #Datos estáticos --> nadie puede generar cambios.
#Aplicación web: tiene una interfaz gráfica parecida a la de una web (también tiene un archivo HTML)
#pero está asociada a un servidor que va a procesar la información que cualquier personas puede cargar o modificar.
#La diferencia entre una página y una aplicación web es que la aplicación tiene una contraparte en el servidor.
#En ese servidor hay una base de datos y hay código que procesa esos datos.

#Hacer un pedido con requests es lo mismo que ir a la aplicación y hace click sobre un botón.

requests.get("url") #traeme esa información.
url.json() #formato parecido a un diccionario de Python --> contenido del pedido que uno hizo.
url.headers #información (metadata) asociada al pedido.
#Un pedido y una respuesta HTTP tiene dos partes: el contenido y los headers (metadata asociada a ese contenido).
url.status_code #cómo resulto el proceso que se le pidió al proceos que haga.

#Partes de una URL: protocolo://dominio/recursos
#Protocolo: HTTP o HTTPS (más seguro porque es encriptado).
#Dominio: es le nombre del directorio del servidor donde puedo ir a encontrar las cosas.

#Escribir una URL es acceder a un archivo particular en una carpeta particular en una computadora particular --> parecido a los paths.

#Las URL tienen que tener un sentido semántico --> construir las rutas tal que no sean confusas.

delete #borrar.
requests.post("url", data=data) #agregar un recurso --> guardar en la variable data la data que quiero que agregue.
put #modifica un dato existente de forma total.
patch #modifica un dato existente de forma parcial --> casi no se usa.

#Desafío 1
https://labiblioteca.com/libros
https://labiblioteca.com/revistas
https://labiblioteca.com/audiolibros