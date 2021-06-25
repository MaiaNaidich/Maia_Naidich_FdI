#La teoría de esta clase (que la dio un profesor invitado) está en:
#https://replit.com/@FrancoBulgarell/ObjetosUCEMA
#Tocar Fork y acceder con mi cuenta de Google para poder ver los archivos.

#¿Qué es un paradigma de programación?
#Un paradigma es un enfoque o marco conceptual acerca de qué es programar y cómo programar. Sirve para resolver un problema.
#Los paradigmas no compiten entre sí, se complementan. Cada uno tiene sus propias ventajas y desventajas.
#Lo que siempre estuvimos usando, hasta ahora, es programación imperativa (Paradigma Imperativo Procedural). Asumimos que un programa es una lista ordenada de instrucciones que se ejecutan de arriba a abajo. 
#Nuevo paradigma --> Paradigma Orientada a Objetos.

from aves import pepita #Pepita es un objeto (todo o casi todo es un objeto en este paradigma)
pepita.volar_en_circulos() #le estamos enviando un mensaje a Pepita. No nos devuelve nada pero tampoco arroja un error.
pepita.cantar_boleros() #salta un error porque "Pepita no sabe cantar boleros". 
pepita.comer_alpiste(10) #poner entre paréntesis la cantidad de gramos que tiene que comer.

from aves import anastasia 
#Anastasia y Pepita son dos objetos distintos --> tienen códigos diferentes.
#Anastasia y Pepita son parecidas (ambas son golondrinas) por lo que pueden hacer lo mismo, osea recibir los mismos mensajes.
pepita == anastasia #devuelve False.

#Ningún objeto es idéntico al otro, aunque sí se puede analizar si son parecidos o completamente distintos.
#Ambiente: conjunto de objetos que están disponibles y puedo utilizar.
#Cada consola es otro ambiente.
#El código de cada objeto cambia cada vez que se corre el código.

pepita.energia #devuelve un número que en cada ambiente es distinto porque hay cosas que afectan a la energía.
anatasia.energia #devuelve un número distinto al de Pepita.
#Cada objeto arranca con la misma cantidad de energía en todos los ambientes y dependiendo de los mensajes que se les envíe, la energía va a ir subiendo o bajando.
    #Cuando vuelan pierden 10 puntos de energía.
    #Cuando comen gana cuatro veces la cantidad de gramos que comió.

#Los objetos pueden tener estado --> en este caso el estado está dado por la energía.
#No necesariamente todos los objetos parecidos arrancan en el mismo estado.
#Este estado puede ser modificado a partir de los mensajes que le enviamos.
#Comportamiento: la acción que hace cuando se le envía un mensaje. Este comportamiento se ve reflejado en el estado.
#Los objetos que son parecidos siempre se comportan de la misma manera --> su energía cambia igual con cada mensaje.

#Interfaz: conjunto de mensajes que los objetos entienden. Aquellas cosas que puedo decirle que haga.

from aves import roberta 
#Roberta entiende los mismos mensajes que Pepita y Anastasia (algunos) pero no tiene el mismo comportamiento.
#Pepita y Anastasia son golondrinas, mientras que Roberta es un dragón.
roberta.volar_en_circulos()
roberta.volar(5)
roberta.comer_peces(3) #Roberta no come alpiste, como Anastasia y Pepita, sino que come peces.
roberta.escupir_fuego()
#Pepita y Anastasia tienen una interfaz y Roberta tiene otra, aunque comparten algunos mensajes.

#Cuando tenemos dos o más objetos que comparten una interfaz, pero la implementan de forma diferente, permitiendo que un tercero los use de forma intercambiable, decimos que los objetos en cuestión son polimórficos.

#Para no repetir código entre dos clases usaos las herencias.
#Herencias: distintas clases comparten clases comunes de las cuales descienden o heredan.
#La "clase madre" está más arriba en la jerarquía.