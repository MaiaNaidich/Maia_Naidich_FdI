# Ejercicio 1
string=input("Inserte una palabra ")
len(string)

# Ejercicio 2
string_grande=input("Inserte una palabra que tenga 6 letras o más ")
if len(string_grande)>5:
    print(string_grande[4].upper() + " " + string_grande[5].upper())
else:
    print("La palabra ingresada no tiene la cantidad de letras suficientes")

# Ejercicio 3
nombre_y_apellido=input("¿Cuál es tu nombre y tu apellido? ")
print("Hola "+ nombre_y_apellido)

# Ejercicio 4
nombre_y_apellidos=input("¿Cuál es tu nombre y tus dos apellidos? ")
datos_en_lista=nombre_y_apellidos.split()
print(datos_en_lista[0][0].upper()+" "+datos_en_lista[1][0].upper()+" "+datos_en_lista[2][0].upper())

# Ejercicio 5
numero1=(input("Inserte un número "))
numero2=(input("Inserte otro número "))
numero3=(input("Inserte un último número "))
print("El promedio de estos tres números es "+str((int(numero1)+int(numero2)+int(numero3))/3))

# Ejercicio 6
minutos=input("Inserte cierta cantidad de minutos ")
print(minutos+" minutos es igual a "+str(int(int(minutos)/60))+" hora/s y "+str(int(minutos)%60)+" minuto/s.")

# Ejercicio 7
sueldo_base=input("¿Cuál es tu sueldo base? ")
ventas=input("¿Cuántas ventas lograste este mes? ")
print ("Al final del mes recibirás $"+str(int(sueldo_base)+(0.1*int(sueldo_base)*int(ventas)))+" de sueldo total.")

# Ejercicio 8
respuestas_correctas=input("¿Cuántas preguntas respondiste correctamente? ")
respuestas_incorrectas=input("¿Cuántas preguntas respondiste incorrectamente? ")
respuestas_en_blanco=input("¿Cuántas preguntas no respondiste? ")
nota=int(respuestas_correctas)*4+int(respuestas_incorrectas)*(-1)+int(respuestas_en_blanco)*0
if nota>0:
    print("La nota final es "+str(nota))
else:
    print("La nota final es 0")

# Ejercicio en grupo
costo_total=input("¿Cuánto vale la casa que te gustaría comprar? ")
sueldo_anual=input("¿Cuál es tu sueldo anual? ")
porcentaje_ahorrado=input("¿Qué porcentaje de tu sueldo ahorras por mes? (En formato decimal) ")
sueldo_mensual=float(sueldo_anual)/12
porcentaje_deposito=0.25
ganancia_anual=0.04
cantidad_ahorrada=0
ahorro_mensual=float(porcentaje_ahorrado)*sueldo_mensual
ganancia_mensual=ahorro_mensual*(ganancia_anual/12)
total_mensual=ahorro_mensual+ganancia_mensual
deposito=float(costo_total)*porcentaje_deposito
meses_para_deposito=round((deposito/total_mensual)+0.5)
print("Te tomará "+str(meses_para_deposito)+" meses ahorrar el dinero necesario para pagar el depósito.")