#Ejercicio 1
import re
patron1="[a-zA-Z0-9]"
texto1="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
def texto_verificado1():
    if re.search(patron1,texto1):
        print("Verificado")
    else: 
        print("No Verificado")

#Ejercicio 2
import re
patron2="\W"
texto2a="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
texto2b="Amet@amet"
def texto_verificado2(texto):
    if not(re.search(patron2,texto)):
        print("Verificado")
    else: 
        print("No Verificado")

#Ejercicio 3
import re
texto4="El helado va en el freezer, no en la heeeladera"
patron4a="he*"
patron4b="he+"
patron4c="he{2,3}"
re.search(patron4a,texto4)
re.search(patron4b,texto4)
re.search(patron4c,texto4)

#Ejercicio 4
import re
texto4="Amet_et_amet"
patron4="[a-zA-Z]_[a-zA-Z]"
re.search(patron4,texto4)

#Ejercicio 5
texto5a="4 defensores, 4 mediocampistas y 2 delanteros"
texto5b="5 defensores, 2 mediocampistas y 3 delanteros"
def empieza_con(numero,texto):
    if texto[0]==numero:
        print("El texto empieza con  "+numero)
    else:
        print("El texto no empieza con "+numero)

#Ejercicio 6
import re
lista_strings6a=["pájaro","volando"]
lista_strings6b=["vaca","comiendo"]
texto6="Mejor pájaro en mano que 100 volando"
for palabra in lista_strings6a:
    re.search(palabra,texto6)
for palabra in lista_strings6b:
    re.search(palabra,texto6)

#Ejercicio 7
import re
patron7="[^a-zA-Z0-9\s]"
texto7a="4 Defensores 4 Mediocampistas y 2 Delanteros"
texto7b="4 Defensores @ 4 Mediocampistas & 2 Delanteros"
def texto_verificado7(texto):
    if re.search(patron7,texto):
        print("No Verificado")
    else: 
        print("Verificado")

#Ejercicio 8
import re
texto8="2 mandarinas, 3 duraznos y 1 ciruela"
patron8="[0-9]"
re.findall(patron8,texto8)

#Ejercicio 9
import re
texto9="Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
patron9="-(.*?)-"
re.findall(patron9,texto9)

#Ejercicio 10
import re
texto10="Hoy estuvimos @trabajando@ con re @regular expression& en &python@ con &VSCode&"
patron10a="@(.*?)@"
patron10b="@(.*?)&"
patron10c="&(.*?)@"
patron10d="&(.*?)&"
def obtener_substrings():
    substrings=[]
    substringa=re.findall(patron10a,texto10)
    substringb=re.findall(patron10b,texto10)
    substringc=re.findall(patron10c,texto10)
    substringd=re.findall(patron10d,texto10)
    list.append(substrings,substringa)
    list.append(substrings,substringb)
    list.append(substrings,substringc)
    list.append(substrings,substringd)
    print (substrings)

#Ejercicio 11
import re
lista_strings11=["Práctica Python", "Práctica C++", "Práctica Fortran"]
def dos_P():
    for palabra in lista_strings11:
        resultado=re.match("(P\w*)\W(P\w*)",elemento)
        if resultado is not None:
            print(resultado.group())

#Ejercicio 12
import re
texto12="Mejor pájaro_en_mano que: 100_volando"
patron12a=" "
patron12b="_"
patron12c=":"
texto_12=re.sub(patron12a,"|",texto12)
texto__12=re.sub(patron12b,"|",texto_12)
texto___12=re.sub(patron12c,"|",texto__12)
print(texto___12)

#Ejercicio 13
import re
texto13="Maia tiene 19 años"
patron13="[0-9]"
texto_13=re.sub(patron13,"_",texto13)
print(texto_13)

#Ejercicio 14
import re
texto14="Maia tiene\t19 años"
patron14a=" "
patron14b="\t"
texto_14=re.sub(patron14a,";",texto14)
texto__14=re.sub(patron14b,";",texto_14)
print(texto__14)

#Ejercicio 15
import re
texto15a="manaidich@gmail.com"
texto15b="maia.naidich@hotmail.cm"
patron15="@(.*).com"
def verificar_mail(patron,texto):
    if re.search(patron,texto):
        print("Mail con formato correcto")
    else:
        print("El formato del mail es incorrecto")