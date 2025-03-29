#EJERCICIO 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


#EJERCICIO 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")


#EJERCICIO 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apelido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apelido}, tengo {edad} años y vivo en {residencia}.")

def ejercicio_cuatro():

#EJERCICIO 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
radio = float(input("Ingresar valor del rario: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es de: {area:.2f}, el perímetro del círculo es de: {perimetro:.2f}.") #redondear 2 decimales


#EJERCICIO 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int(input("Ingresar la cantidad de segundos: "))
total_horas = segundos / 3600
print(f"Los {segundos} segundos ingresados, equivalen a: {total_horas:.2f}h.")


#EJERCICIO 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int(input("Ingrese un número: "))
for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")


#EJERCICIO 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_uno = int(input("Ingresar el primer número: "))
numero_dos = int(input("Ingresar el segundo número: "))
if numero_uno and numero_dos != 0:
    print(f"La suma de {numero_uno} + {numero_dos} es igual a: {numero_uno + numero_dos}") 
else:
    print("Los números ingresados deben ser distintos a 0")


#EJERCICIO 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingreso su altura: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es de: {imc:.2f}")


#EJERCICIO 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia
temp_c = int(input("Ingrese la temperatura en Celsius: "))
temp_f = (9/5) * temp_c + 32
print (f"La temperatura en grados Fahrenheit es de: {temp_f:.2f}")


#EJERCICIO 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
num_uno = float(input("Ingresar el primer número: "))
num_dos = float(input("Ingresar el segundo número: "))
num_tres = float(input("Ingresar el tercer número: "))

promedio = (num_uno + num_dos + num_tres) / 3

print(f"El promedio de {num_uno} + {num_dos} + {num_tres} es de: {promedio}")
