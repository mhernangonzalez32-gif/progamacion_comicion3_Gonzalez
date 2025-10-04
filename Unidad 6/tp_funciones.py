
'''1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.'''

def saludo():
    print("Hola mundo.")

saludo()

'''2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.'''

def saludar_usuario(nomb):
    print(f"Bienvenido {nomb}!")

nombre = input("Ingrese su nombre: ").strip().capitalize()
saludar_usuario(nombre)

'''3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.'''

def informacion_personal(n, a, e, d):
    print(f"Nombre: {n}\nApellido: {a}\nEdad: {e}\nDireccion: {d}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
direccion = input("Ingrese su Direccion: ")
informacion_personal(nombre, apellido, edad, direccion)
'''4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.'''

import math
def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio_circulo = int(input('Ingrese el radio: '))
area_obtenida = calcular_area_circulo(radio_circulo)
perimetro_obtenido = calcular_perimetro_circulo(radio_circulo)
print(f'El radio ingresado es: {radio_circulo}')
print(f'Su area es de: {area_obtenida}')
print(f'Su perimetro es: {perimetro_obtenido}')

'''5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.'''

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos_input = float(input('Ingrese la cantidad de segundos: '))

hora_convertidas = segundos_a_horas(segundos_input)
print(f'{segundos_input} segundos equivale a {hora_convertidas:.2f} horas')

'''6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.'''

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i

        print(f'{numero} x {i} = {resultado}')

numero_input = int(input('Ingrese el numero que desea sabes su tabla: '))
tabla_multiplicar(numero_input)

'''7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.'''

def operaciones_basicas(num1, num2):
    suma = num1 + num2 
    resta = num1 - num2
    multiplicacion = num1 * num2 
    if num2 != 0:
        divicion = num1 / num2
    else :
        divicion = 'No se puede divivir por CERO. '
    return (suma, resta, multiplicacion, divicion)

num1_input = int(input('Ingrese un numero: '))
num2_input = int(input('Ingrese otro numero: '))

resultados = operaciones_basicas(num1_input, num2_input)
suma, resta, multiplicacion, divicion = resultados 
print(f'Suma {num1_input} + {num2_input} = {suma}')
print(f'Resta {num1_input} - {num2_input} = {resta}')
print(f'Multiplicacion {num1_input} x {num2_input} = {multiplicacion}')
print(f'divicion {num1_input} / {num2_input} = {divicion}')


'''8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.'''

def calcular_imc(peso, altura):
    icm = peso / (altura**2)
    return icm

peso_inp = float(input('Ingrese el peso: '))
altura_inp = float(input('Ingrese la altura en metros: '))

icm = calcular_imc(peso_inp, altura_inp)
print(f'Su indice de masa corporal es: {icm}')

'''9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.'''

def celsius_a_fahrenheit(celsius):
    
    fahrenheit = (temperatura_celsius * 9/5) + 32
    print(f"°C {temperatura_celsius}  equivale a °F {fahrenheit}")

temperatura_celsius = float(input("Ingrese la temperatura en celsius: "))
celsius_a_fahrenheit(temperatura_celsius)

'''10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.'''

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3                    
    print(f"El promedio de estos numero es: {promedio}")     

primer_numero = int(input("Ingrese un numero natural "))
segundo_numero = int(input("Ingrese el segundo numero natural "))
tercer_numero = int(input("Ingrese el segundo numero natural "))
calcular_promedio(primer_numero, segundo_numero, tercer_numero)
