import random

'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.'''

for iterador in range(1, 101):
    print(iterador)

'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. '''


numero = int(input("Ingrese un numero: "))
contador = 0 

while numero > 0:
    numero = numero // 10
    contador = contador + 1

print(contador)

'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. '''

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese Otro numero: "))
memoria = 0
if num_2 < num_1:   
    memoria = num_2
    num_2 = num_1
    num_1 = memoria
cuenta = 0
for i in range(num_1 +1 , num_2):
    cuenta += i

print(cuenta)

'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.'''
cuenta = 0
numero = -1
while numero != 0:
    numero = int(input("Ingrese un numero para sumarlo: "))
    if numero < 0:
        print("Ingrese un numero positivo")
        continue
    cuenta = cuenta + numero

print(cuenta)

'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. '''

import random

numero_adivinar = random.randint(0, 10)
contador = 0
num = -1
while num != numero_adivinar:
    num = input("Ingrese el numero entre 0 y 9: ")
    if not num.isdigit():
        print("Ingrese un numero valido")
        continue
    num = int(num)
    if 0 < num > 9:
        print("Ingrese u numero mayor a cero y menor a nueve!")
        continue
    
    contador += 1
print(f"Se necesitaron {contador} intentos para adivinar el numero")

'''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. '''

idx = 0
for idx in range(0, 100, 2):
    print(f"{idx}") 



'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. '''

idx = 0
numero = int(input("Ingrese un numero: "))
cuenta = 0
for idx in range(numero): 
    cuenta = cuenta + idx

print(f"La suma de sus numeros intermedios es: {cuenta}")


'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).'''

num_lista = int(input("Ingrece con cuantos numeros vamos a trabjar: "))

negativo = 0
positivo = 0
par = 0
impar = 0 
for i in range(num_lista):
    num_ingresado = int(input("Ingrese numeros para verificarlos: "))
    if num_ingresado <= 0:
        negativo += 1
    elif num_ingresado > 0:
        positivo += 1
    if num_ingresado % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Ingresaste\n{negativo} Numeros negativos\n {positivo} Numeros positivos\n {par} Numeros pares\n {impar} Numeros impares")    

'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). '''

cant_num = int(input("Ingrese cantidad de numeros a trabajar: "))
suma = 0
media = 0

for i in range(cant_num):
    num = int(input("Ingrese numeros para sumar: "))
    suma = suma + num
    media = suma / cant_num

print(f"La media de todos los numeros ingresados: {media}") 

'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = int(input("Ingresa un número para invertir: "))
numero_original = numero  
numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    numero = numero // 10

print(f"El número original era: {numero_original}")
print(f"El número invertido es: {numero_invertido}")

