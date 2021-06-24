#Ejercicio 1
palabra=input("Inserte una palabra ")
inicial=palabra[0]
if "a"<=inicial<="z":
    print("La inicial de la palabra ingresada es minúscula")
else:
    print("La inicial de la palabra ingresada es mayúscula")

#Ejercicio 2
numero=input("Ingrese un número ")
if int(numero)>0:
    print("El número ingresado es positivo")
else:
    if int(numero)<0:
        print("El número ingresado es negativo")
    else:
        print("El número ingresado es cero")

#Ejercicio 3
cara=input("Ingrese un número del 1 al 6 ")
if int(cara)==1:
    print("6")
elif int(cara)==2:
    print("5")
elif int(cara)==3:
    print ("4")
elif int(cara)==4:
    print("3")
elif int(cara)==5:
    print("2")
elif int(cara)==6:
    print("1")
else:
    print("El número ingresado es incorrecto ")

#Ejercicio 4
peso=input("¿Cuánto pesa tu paquete (en kg)? ")
zona=input("¿En qué zona querés transportar tu paquete? ")
if float(peso)>5:
    print("No transportaremos tu paquete porque es muy pesado")
elif zona=="América del Sur":
    print("Tu envío te costará "+str(float(peso)*10)+" dólares")
elif zona=="América Central":
    print("Tu envío te costará "+str(float(peso)*15)+" dólares")
elif zona=="América del Norte":
    print("Tu envío te costará "+str(float(peso)*18)+" dólares")
elif zona=="Europa":
    print("Tu envío te costará "+str(float(peso)*24)+" dólares")
elif zona=="Asia":
    print("Tu envío te costará "+str(float(peso)*30)+" dólares")
else:
    print("No realizamos envíos en esa zona")

#Ejercicio 5
dia=input("¿Qué número de día de la semana es hoy? ")
if dia=="1":
    print("Hoy es domingo")
elif dia=="2":
    print("Hoy es lunes")
elif dia=="3":
    print("Hoy es martes")
elif dia=="4":
    print("Hoy es miércoles")
elif dia=="5":
    print("Hoy es jueves")
elif dia=="6":
    print("Hoy es viernes")
elif dia=="7":
    print("Hoy es sábado")
else:
    print("El número ingresado es incorrecto")

#Ejercicio 6
elemento1=input("Ingresá el primer elemento de la lista ")
elemento2=input("Ingresá el segundo elemento de la lista ")
elemento3=input("Ingresá el tercer elemento de la lista ")
elemento4=input("Ingresá el cuarto elemento de la lista ")
elemento5=input("Ingresá el quinto elemento de la lista ")
lista1=[]
list.append(lista1,elemento1)
list.append(lista1,elemento2)
list.append(lista1,elemento3)
list.append(lista1,elemento4)
list.append(lista1,elemento5)
lista2=list(lista1)
lista2.reverse()
lista2

#Ejercicio 7
listado=[]
numero_ingresado=input("Ingrese un número ")
while int(numero_ingresado)>=0:
    numero_ingresado=input("Ingrese un número ")
    list.append(listado,numero_ingresado)
ultimo_numero=(len(listado)-1)
list.remove(listado,listado[int(ultimo_numero)])
listado

#Ejercico 8
e1_l1=input("Ingresá el primer número de la primer lista ")
e2_l1=input("Ingresá el segundo número de la primer lista ")
e3_l1=input("Ingresá el tercer número de la primer lista ")
e4_l1=input("Ingresá el cuarto número de la primer lista ")
e5_l1=input("Ingresá el quinto número de la primer lista ")
e1_l2=input("Ingresá el primer número de la segunda lista ")
e2_l2=input("Ingresá el segundo número de la segunda lista ")
e3_l2=input("Ingresá el tercer número de la segunda lista ")
e4_l2=input("Ingresá el cuarto número de la segunda lista ")
e5_l2=input("Ingresá el quinto número de la segunda lista ")
lista1=[]
lista2=[]
lista3=[]
list.append(lista1,int(e1_l1))
list.append(lista1,int(e2_l1))
list.append(lista1,int(e3_l1))
list.append(lista1,int(e4_l1))
list.append(lista1,int(e5_l1))
list.append(lista2,int(e1_l2))
list.append(lista2,int(e2_l2))
list.append(lista2,int(e3_l2))
list.append(lista2,int(e4_l2))
list.append(lista2,int(e5_l2))
e1_l3=lista1[0]+lista2[0]
e2_l3=lista1[1]+lista2[1]
e3_l3=lista1[2]+lista2[2]
e4_l3=lista1[3]+lista2[3]
e5_l3=lista1[4]+lista2[4]
list.append(lista3,int(e1_l3))
list.append(lista3,int(e2_l3))
list.append(lista3,int(e3_l3))
list.append(lista3,int(e4_l3))
list.append(lista3,int(e5_l3))
lista3

#Ejercicio 9
nombres=[]
notas=[]
nombre=input("Inserte el nombre de un alumno ")
nota=input("Inserte su nota ")
while nombre!="*":
    nombre=input("Inserte el nombre de un alumno ")
    nota=input("Inserte su nota ")
    list.append(nombres, nombre)
    list.append(notas,nota)
asterisco=(len(nombres)-1)
list.remove(nombres,nombres[int(asterisco)])
nota_maxima=max(notas)
index_nota_maxima=notas.index(nota_maxima)
mejor_alumno=nombres[index_nota_maxima]
print("La nota máxima fue "+str(nota_maxima)+" y la obtuvo "+mejor_alumno)


#Ejercicio 10 (hecho en clase)
caracteres={}
cadena=input("Escribí algo ")
for caracter in cadena:
    if caracter in caracteres:
        caracteres[caracter]+=1
    else:
        caracteres[caracter]=1
for clave,valor in caracteres.items():
    print(clave,valor)

#Ejercicio 11 (hecho en clase)
alfabeto="abcdefghijklmnñopqrstuvwxyz"
caracteres2={}
for letra in alfabeto+alfabeto.upper():
    caracteres2[letra]=0
cadena2=input("Escribí algo ")
for caracter in cadena2:
    if caracter.lower() in alfabeto:
        caracteres2[caracter]+=1
for clave,valor in caracteres2.items():
    print(clave,valor)

#Ejercicio 12
datos_alumnos={}
cantidad_alumnos=input("Ingrese el número de alumnos que va a introducir ")
preguntar_nombre=""
preguntar_nota=0
for alumno in range(int(cantidad_alumnos)):
    lista_notas=[]
    preguntar_nombre=input("Nombre: ")
    preguntar_nota=int(input("Nota: "))
    if preguntar_nombre not in datos_alumnos.keys():
        while preguntar_nota>0:
            lista_notas.append(preguntar_nota)
            datos_alumnos[preguntar_nombre]=lista_notas
            preguntar_nota=int(input("Nota: "))
            print(lista_notas)
    else:
        print("Alumno ya cargado")
for alumno in datos_alumnos.keys():
    promedio=sum(datos_alumnos[alumno])/len(datos_alumnos[alumno])
    print("El promedio de "+alumno+" es "+str(promedio))
        
#Ejercicio 13
def esMultiplo():
    numero1=input("Inserte un número entero ")
    numero2=input("Inserte otro número entero ")
    if int(numero1)%int(numero2)==0:
        print(numero1+" es múltiplo de "+numero2)
    else:
        if int(numero2)%int(numero1)==0:
            print(numero2+" es múltiplo de "+numero1)
        else:
            print("Los números ingresados no son múltiplos entre sí")

#Ejercicio 14
cantidad_dias=input("¿La información de cuántos días se va a cargar? ")
for dia in range(int(cantidad_dias)):
    fecha=input("Fecha: ")
    temp_minima=input("Temperatura mínima: ")
    temp_maxima=input("Temperatura máxima: ")
    temp_media=(int(temp_minima)+int(temp_maxima))/2
    print("La temperatura media del "+fecha+" es "+str(temp_media))

#Ejercicio 15
socios={"1":["Florencia Ocampo","14/06/2001","Cuota al día"],
"2":["David Estévez","14/09/2001","Cuota al día"],
"3":["Sofía Cáceres","14/09/2001","Cuota al día"],
"4":["Pedro Juarez","21/10/2017","Cuota atrasada"]}
cantidad_socios=len(socios.keys())
def cuotas_pagas():
    n_socio=input("¿Qué socio ha pagado todas sus cuotas? ")
    socios[n_socio][2]="Cuota al día"
def modificar_fecha_ingreso(fecha_mal,fecha_bien):
    for socio in socios:
        if socios[socio][1]==fecha_mal:
            socios[socio][1]=fecha_bien
def dar_de_baja():
    baja_socio=input("¿Qué socio querés dar de baja? ")
    for socio in socios:
        if socios[socio][0]==baja_socio:
           del socios[socio] 