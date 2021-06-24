#Desafio II: Creá una función denominada mitades que tenga como argumento un número e imprima el resultado de la división de ese número por 2.
def mitades(numero):
  return numero/2
#Cuando el número es 9, devuelve 4.5.
#Cuando el número es 0, devuelve 0.

#Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? 
#Reescribí la función incorporando una declaración try-except.
def mitades_ok(numero):
  try:
    return numero/2
  except:
    print("El número ingresado no se puede dividir por 2")