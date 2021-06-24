#Ejercicio 1
import re
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
contador=0
with open(ruta,"r") as Verso1:
    if not(re.search("^T",Verso1)):
        contador+=1

#Ejercicio 2
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
def imprimir_n_primeras_lineas(n):
    with open(ruta,"r") as Verso1:
        lineas=Verso1.readlines()
        for linea in lineas:
            if lineas.index(linea)<=(n-1):
                print (linea)

#Ejercicio 3
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
def imprimir_n_ultimas_lineas(n):
    with open(ruta,"r") as Verso1:
        lineas=Verso1.readlines()
        cantidad_lineas=len(lineas)
        ultimas_n_lineas=cantidad_lineas-n-1
        for linea in lineas3:
            if lineas.index(linea)>=ultimas_n_lineas:
                print (linea)

#Ejercicio 4
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
with open (ruta,"r") as Verso1:
    lineas=Verso1.readlines()
    palabras=[]
    for linea in lineas:
        palabras_en_linea=linea.split()
        for palabra in palabras_en_linea:
            palabras.append(palabra)
    len(palabras)

#Ejercicio 5
import re
import shutil
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
ruta_auxiliar="F:\\Fundamentos_de_Informática\\Verso1_modificado.txt"
with open (ruta,"r") as Verso1:
    verso1=Verso1.read()
with open (ruta_auxiliar,"w") as vm1:
    shutil.copyfile(ruta,ruta_auxiliar)
with open (ruta_auxiliar,"r+") as vm1:
    vm1.write(re.sub("h","h\n",vm1.read()))

#Ejercicio 6 
import re
import shutil
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
ruta_auxiliar2="F:\\Fundamentos_de_Informática\\Verso1_modificado2.txt"
with open (ruta,"r") as Verso1:
    verso1=Verso1.read()
with open (ruta_auxiliar2,"w") as Verso1_modificado2:
    shutil.copyfile(ruta,ruta_auxiliar2)
with open (ruta_auxiliar2,"r+") as vm2:
    vm2.write(re.sub("\n"," ",vm2.read()))

#Ejercicio 7
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
palabras=[]
letras=[]
with open (ruta,"r") as Verso1:
    lineas=Verso1.readlines()
for linea in lineas:
    linea_partida=linea.split()
    for palabra in linea_partida:
        palabras.append(palabra)
for palabra in palabras:
    cantidad_letras=len(palabra)
    letras.append(cantidad_letras)
max_letras=max(letras)
index=letras.index(max_letras)
palabra_mas_larga=palabras[index]
largo=len(palabra_mas_larga)
print ("La palabra más larga es "+palabra_mas_larga+" y tiene "+str(largo)+" letras")

#Ejercicio 8
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
ruta2="F:\\Fundamentos_de_Informática\\Verso2.txt"
ruta_combinado="F:\\Fundamentos_de_Informática\\VersoCombinado.txt"
with open(ruta,"r") as Verso1:
    verso1_a_combinar=Verso1.read()
with open(ruta2,"r") as Verso2:
    verso2_a_combinar=Verso2.read()
verso1_a_combinar+="\n"
verso1_a_combinar+=verso2_a_combinar
with open(ruta_combinado,"w") as VersoCombinado:
    VersoCombinado.write(verso1_a_combinar)

#Ejercicio 9
ruta="F:\\Fundamentos_de_Informática\\Verso1.txt"
palabras=[]
repeticiones_palabras={}
with open (ruta,"r") as Verso1:
    lineas=Verso1.readlines()
for linea in lineas:
    linea_partida=linea.split()
    for palabra in linea_partida:
        palabras.append(palabra)
for palabra in palabras:
    if palabra in repeticiones_palabras.keys():
        repeticiones_palabras[palabra]+=1
    else:
        repeticiones_palabras[palabra]=1
repeticiones_palabras

#Ejercicio 10
carpeta="F:\\Fundamentos_de_Informática\\Textos"
texto_destino="F:\\Fundamentos_de_Informática\\Textos\\Texto_Destino"
texto_a_combinar=""
with open(carpeta,"r") as carpeta:
    for texto in carpeta:
        texto_leido=texto.read()
        texto_a_combinar+=texto_leido
        texto_a_combinar+="\n"
    print(texto_a_combinar)
with open(texto_destino,"w") as texto_destino:
    texto_destino.write(texto_a_combinar)