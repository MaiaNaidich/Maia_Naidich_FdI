import re
# Métodos de re disponibles en: https://docs.python.org/3/library/re.html

# Metacaracteres: caracteres especiales que le dan formato al texto → cuando se imprime en pantalla se ve el texto con el formato.
# Ejemplo:
texto="Esta es la linea uno\npalabra en la linea dos\n"
print(texto)

#Para pensar:
#Podemos buscar cuántas veces se repite una palabra en un discurso largo, y si consideramos que son demasiadas repeticiones, cambiar alguna de ellas por sinónimos.

texto = 'Esta es la linea uno\npalabra en la linea dos\n'
^palabra #True.
\Apalabra #False.
palabra$ #False.
palabra\Z #False.

# La siguiente expresión devuelve todos los caracteres entre X e Y de todos los tipos y todas las veces que aparezcan
"X(.*)Y"

# Desafío 1
\d{4,}

# Desafío 2
[a-z]{3,6}

# Desafío 3
*ab

# Desafío 4
texto = "En la clase de Introducción a la programación hay 30 estudiantes"
\d

# Desafío 5
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
re.search(patron,texto)
texto[22:26]

.group() #nos devuelve el patrón en forma de stirng (si lo encuentra)
.search(patron,texto) #nos indica si se encontró o no el patrón en el texto y en qué posición aparece por primera vez.
.findall(patron,texto) #nos devuelve una lista con todas las aparciciones del patrón en el texto.
.sub(patron,"###",texto) #reemplaza en el texto las partes que cumplen con el patrón por "###".