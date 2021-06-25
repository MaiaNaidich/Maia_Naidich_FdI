#Se le agrega el (Ave) para indicar que Golondrina hereda de Ave.
class Golondrina(Ave): #la clase indica cuáles son los mensajes que va a entender y cuáles van a ser sus comportamientos.
  def __init__(self, energia):
    self.energia = energia
#La energía es un atributo de la golondrina (se lo asigno cuando la creo), por eso cuando lo pregunto en la terminal no le pongo paréntesis.

#La estructura es la misma con la que definimos una función, pero no es una función.
#Es un método.
#Diferencias entre método y función:
  #Las funciones se invocan como función(argumentos), mientras que los métodos evalúan a través del envío de mensajes --> objeto.mensaje(argumentos)
  #Los métodos tienen siempre como primer parámetro "self". Las funciones no. --> ¿Qué es self?
    #Cuando escribimos el mensaje para que lo haga, no lo escribimos.
    #Self representa el objeto al cual se le está enviando el mensaje.
  #Los métodos siempre van dentro de una clase, pero las funciones van por fuera. 

  def comer_alpiste(self, gramos): #qué es lo que sabe hacer.
    self.energia += 4 * gramos #cómo lo hace.

  def volar_en_circulos(self): #volar en círculos es equivalente a volar 0 km.
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

#No todos los métodos tienen que modificar el estado del objeto.
#esta_debil evalúa el estado del objeto sin modificarlo.  
  def esta_debil(self):
    return self.energia<10

class Dragon(Ave):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

pepita = Golondrina(100) #esto se lee como: "Pepita va a ser un objeto que se construya como una golondrina (va a ser de esa clase) y su energía inicial va a ser 100"
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

#Cada objeto es una instancia de su clase. Es un ejemplo o caso concreto.
#Pepita es un objeto.
#Pepita es una instancia de Golondrina.

#Las clases siempre son denominadas en singular.

#EJERCICIO: hace a hipo, entrenador de dragones: 
#sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos los dias, 
#haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces).

class EntrenadorDeDragones:
  def __init__(self, vacantes):
    self.vacantes=vacantes
    self.alumnos=[]
  
  def aceptar_dragon(self,dragon):
    if len(self.alumnos)<self.vacantes:
      list.append(self.alumnos,dragon)
      self.vacantes-=1

  def entrenar_dragones(self):
    for dragon in self.alumnos:
      for _ in range(20):
        dragon.volar_en_circulos()
      dragon.comer_peces(3)

hipo=EntrenadorDeDragones(5)

#Definir "clase madre". 
#Tanto los dragones como las golondrinas van a compartir esta interfaz y van a responder de la misma manera a estos mensajes.
#Las aves son un concepto general y abstracto, por eso no vamos a crear aves directamente.
class Ave:
  def esta_feliz(self):
    return self.energia>500