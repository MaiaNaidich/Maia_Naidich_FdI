#Cuando usamos search no necesariamente tenemos que encontrar la posición de algo, sino también podemos utilizarlo para hacer algo, sabiendo si una cadena está o no en el texto.
if re.search(patron,texto) is not None:
    #bloque de código
else:
    #bloque de código

#Para concatenar rangos, simplemente se ponen uno al lado del otro dentro del mismo corchete.

#Cuando lo que queremos encontrar es una palabra... 
re.search(patron,texto).group() #...nos devuelve la coincidencia.

#Cuando lo que queremos encontrar es todo lo que se encuentra entre dos palabras o caracteres...
patron="palabra1(.*)palabra2" #Prioriza el matcheo más extenso (desde que aparece por primera vez palabra1 hasta que aparece por última vez palabra2)
re.search(patron,texto).group() #...nos devuelve el texto que está entre los delimitadores y los delimitadores.
re.search(patron,texto).group(1) #... nos devuelve el texto que está entre los delimitadores, sin los delimitadores.

patron="palabra1(.*?)palabra2" #Prioriza el matcheo interno (desde que aparece por primera vez palabra1 hasta que aparece por primera vez palabra2)

re.findall(patron,texto) #Devuelve todas las coincidencias, como si se usara group(1).

patron=r"\b palabra \b" #Para cuando querés buscar una palabra que se encuentra entre dos caracteres no alfanuméricos. 