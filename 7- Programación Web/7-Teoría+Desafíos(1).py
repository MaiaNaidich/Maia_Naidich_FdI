#Biblioteca "request"

import requests

#Python no es un lenguaje muy usado para la programación web, 
#por eso nosotros vamos a verlo desde el lado del cosnsumo y no desde el lado de construir una web.

#Internet: redes de computadoras unidas por cables de red que une todas las computadoras del mundo.
#Web: los datos a los cuales puedo acceder a través de Internet.
#No son datos abstractos sino que son archivos que existen en alguna computadora --> archivos de hipertexto o HTML.
#Servidor: una computadora que ofrece recursos y de la cual los clientes pueden consumirlos.
#En principio, cualquier máquina puede ser cliente y puede ser servidor.
#Toda la tecnología web se escribe con tres lenguajes de programación básicos: Java Script (behavioral - le da dinamismo), CSS (presentational) y HTML (structural).
#Cloud Computing: consumir recursos de hardware --> correr un script en otra máquina --> ej.: Colab.
#Ventaja: no necesitas invertir en hardware.
#Desventaja: la empresa que te presta su hardware tiene acceso a toda tu información.
#¿Cómo se comunican el cliente y el servidor? --> protocolos de comunicación (convenciones).
#Protocolo HTTP:
    #Pedido --> URL: nos dan la información de un recurso y la manera de conseguirlo.
    # Un URL es cualquier string con formato URI que nos permita localizar un recurso.
    #protocolo://dominio:puerto/ruta#fragmento?parametro1=valor1&parametro2=valor2

#Desafío 1 - análogo a entrar en la página web y hacerlo clickeando sobre los botones que nos muestra la interfaz gráfica.
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
r.json()

#Desafío 2
import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/400")
r.json()
#Salta un error porque no existe la prenda 400.

r.headers #nos da información o datos anexos a lo que pedimos.
r.status_code #estados del pedido que hice.
    #404: error.
    #200: está todp bien.
    #500: error en el servidor --> algo se programó mal en el seridor.
    #Hay muchos más --> se supone que hay un código por cada posible error.

#Desafío 3
import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
r.headers
r.status_code #devuelve 200.

#Desafío 4
import requests
r = requests.get("https://macowins-server.herokuapp.com/prindas/1")
r.status_code #devuelve 404.

#Listado completo de prendas:
r = requests.get('https://macowins-server.herokuapp.com/prendas')
r.json()

#Filtrar por tipo de prenda:
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=saco')
r.json()

#Para pensar:
    # ¿Es lo mismo consultar /prendas/ que /prendas/1? 
    # ¿En qué se diferencian? ¿Qué ocurre si hacemos r.content? ¿Por qué?
    # /prendas/ devuelve el contenido de todas las prendas, mientras que /prendas/1 devuelve el conteido de la prenda con id =1.
    
    # ¿Qué hará /ventas/2? ¿/ventas/?
    # Imagino que será parecido a lo que sucedió en la pregunta anterior:
    # Para /ventas/ devolverá el contenido de todas las ventas, mientras que para /ventas/2 devolverá el contenido de la segunda venta.

#Desafío 5
import requests
v = requests.get('https://macowins-server.herokuapp.com/ventas')
v2 = requests.get('https://macowins-server.herokuapp.com/ventas/2')
v.content
v2.content
#Sucedió lo imaginado.

#Desafío 6
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remeras')
r.json()

#Desafío 7
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remeras&talle=XS')
r.json()

#Desafío 8
#Se está indicando que se va a acceder a través del cerebro, a los recuerdos, localizados en el sector número 3403.
#Para esto, se accederá a los recientes, más esepcíficamente a los de hoy.
#Por último, se buscará los recuerdos cuyo tema sea http.

#Desafío 9