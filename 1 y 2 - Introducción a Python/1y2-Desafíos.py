#Desafío I: ¿Qué pasos nos faltaron? ¿Podes pensar otras posibles situaciones que no estemos contemplando (como por ejemplo que no haya yerba en el yerbero)? 
#Agregá a la guía para preparar mate(script) los pasos, problemas posibles y las soluciones que se te ocurran en sentencias u ordenes sencillas 
#(ejemplo; verificar si hay yerba en el yerbero. Si no hay agregar, si hay llenar el mate)

#Paso 1) Seleccionar el mate.
#Paso 2) Buscar el yerbero.
        #Paso 3) Verificar si el yerbero está sobre la mesada:
                #Paso 4) Si el yerbero está sobre la mesada, verificar si hay yerba en el yerbero.
                                #Paso 5) Si hay yerba en el yerbero, verificar si el mate está vacío.
                                        #Paso 6) Si el mate está vacío, llenarlo con la yerba del yerbero.
                                        #Paso 7) Si el mate está lleno:
                                                #Paso 8) Vaciarlo en una maceta
                                                #Paso 9) Llenarlo con la yerba del yerbero. 
                                #Paso 10) Si no hay yerba en el yerbero:
                                        #Paso 11) Ir al supermercado a comprar yerba.
                                        #Paso 12) Llenar el yerbero.
                                        #Paso 13) Verificar si el mate está vacío.
                                                #Paso 14) Si el mate está vacío, llenarlo con la yerba del yerbero.
                                                #Paso 15) Si el mate está lleno:
                                                        #Paso 16) Vaciarlo en una maceta
                                                        #Paso 17) Llenarlo con la yerba del yerbero.
        #Paso 18) Si el yerbero no está sobre la mesada, entonces está en la alacena.
                #Paso 19) Si el yerbero está sobre la mesada, verificar si hay yerba en el yerbero.
                                #Paso 20) Si hay yerba en el yerbero, verificar si el mate está vacío.
                                        #Paso 21) Si el mate está vacío, llenarlo con la yerba del yerbero.
                                        #Paso 22) Si el mate está lleno:
                                                #Paso 23) Vaciarlo en una maceta
                                                #Paso 24) Llenarlo con la yerba del yerbero. 
                                #Paso 25) Si no hay yerba en el yerbero:
                                        #Paso 26) Ir al supermercado a comprar yerba.
                                        #Paso 27) Llenar el yerbero.
                                        #Paso 28) Verificar si el mate está vacío.
                                                #Paso 29) Si el mate está vacío, llenarlo con la yerba del yerbero.
                                                #Paso 30) Si el mate está lleno:
                                                        #Paso 31) Vaciarlo en una maceta
                                                        #Paso 32) Llenarlo con la yerba del yerbero.

#Desafío II: Abrí la terminal de Python que tengas instalada en tu computadora y luego abrí Visual Code y luego presioná las teclas Ctrl + J. 
#Se abrirá una terminal en el editor de código. ¿Cómo es el prompt en cada caso? ¿Qué lenguaje "entiende" la terminal de Visual Code?

#El prompt de la terminal de Python es >>>.
#El prompt de la termina de Visual Code (que es Bash) es $.
#Sin embargo, la terminal de Bash puede entender lenguaje Python si ingresamos la palabra "python", pero al revés no funciona.
#Cuando ingresamos "python" en la consola de Bash el prompt cambia a >>>.

#Para pensar:
# * significa multiplicación.
# / significa división.

edad_lola = 13
edad_ana = 32
edad_lola == edad_ana
#El resultado es False, que es un booleano.

afirmacion = "si"
gran_afirmacion = "SI"
gran_afirmacion == afirmacion
#El resultado es False, porque Python distingue entre mayúsculas y minúsculas.

#La C en Marie Curie tendrá la posición 6, porque se empieza a contar desde el cero y el espacio cuenta como una posición.

saludo = "Hola mundo"
saludo[0:3]
#Nos devuelve los primeros tres caracteres del stirng saludo.
#Si removemos el 3 (hacemos [0:]) nos devuelve el string completo, porque nos muestra todos los caracteres a partir del número 0.

#Desafío III: Probá las lineas anteriores y anotate para qué sirve cada uno de los métodos y funciones.
#len - cuenta la cantidad de caracteres de un string dado.
#upper - transforma un string dado al mismo string pero todo en letras mayúsculas.
#lower - transforma un string dado al mismo string pero todo en letras minúsculas. 
#count - cuenta cuántas veces aparece un caracter o conjunto de caracteres en un string dado.
#replace - en un stirng dado, reemplaza un caracter por otro.

#Para pensar:
#Hacer saludo.upper().lower() es lo mismo que hacer saludo.lower(), ya que convierte todas las letras del saludo a mayúsculas y luego a minúsculas.

#Desafío IV: Vimos que el método replace nos permite reemplazar un caracter por otro de un string dado, pero nos dejará reemplazar un segemento más largo? 
#Probá hacer saludo.replace("mundo", "terricolas")
saludo.replace("mundo", "terricolas")
#Sí, nos deja reemplazarlo.
saludo
#No cambió la variable. Si hubiéramos querido que cambie tendríamos que haberla redefinido como...
saludo=saludo.replace("mundo","terricolas")
#O en otra variable (para no "pisar" la que ya teníamos), como por ejemplo...
extraterrestre=saludo.replace("mundo","terricolas")

#Para pensar:
#Para conocer la longitud de la lista, se puede usar len, al igual que para conocer la longitud de un string.

#Index nos devuelve la posición de un elemento dentro de una lista.
#Por eso, si probamos lista.index("25") no dice ""25" is not in list".

#Para obtener los valores de un diccionario, podemos hacer diccionario.values().

#Desafío VI: Después de tanto programar necesitamos unos matecitos. 
#Hoy aprendiste a prepararlos. Lo que no estoy segura es de que el agua alcance para toda la ronda. 
#Suponiendo que cada cebada de mate consume del 30 ml de agua. 
#Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos consumiremos para un ronda dada (es decir una cantidad de personas dada).}
def cuantos_termos(cantidad_personas):
  return int((30*cantidad_personas)/1000)+1

#Desafío VII: Siempre con los mates, vienen bien unas facturitas.
#¿Si hacemos una vaquita ? Vaquita se le dice en Argentina a hacer una colecta de plata para un fin común. 
#Creá función que nos permita dividir los costos de una docena de facturas entre cierta cantidad de comensales.
def vaquita(cantidad_personas,precio_docena):
  return precio_docena/cantidad_personas

#Desafío VIII: En una ronda pequña de mate no hace falta llenar tooooodo el termo, con un poco de agua quizás alcanza. 
#Definí una función calcular_cantidad_de_agua que espere una cantidad de personas como argumento y devuelva la cantidad de mililitros con los que tenemos que cargar el termo.
def calcular_cantidad_de_agua(cantidad_personas):
  if cantidad_personas*30>=1000:
    print("Vas a necesitar más de un termo")
  else:
    return cantidad_personas*30

#Para pensar:
#Empanadas por gusto nos imprime los gustos de empanadas que los comensales pidieron.
#i representa a cada valor perteneciente a lista_comensales.

#Desafío IX: Modificá la función empanadas_por_gusto() para que devuelva la cantidad de empenadas de cada gusto que deben pedirse a la casa de comidas.
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas", "Fede":"no veggie"}
lista_comensales = pedido.keys()
lista_gustos = pedido.values()
lista_para_pedir={}
def empanadas_por_gusto():
  for gusto in lista_gustos:
    lista_para_pedir[gusto]=0
  for comensal in lista_comensales:
    lista_para_pedir[pedido[comensal]]+=1
  print(lista_para_pedir)
empanadas_por_gusto()

