'''1) Crear un programa que imprima por pantalla el mensaje: Hola Mundo!.'''

print(" Hola mundo" )

'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.'''

nombre = input("Ingrese su nombre ")

print(f"Hola {nombre}!")

'''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.'''

nombre = input ("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input(f"Ingrese su edad {nombre} ")
nacionalidad = input("Ingrese la localidad donde vive ")

print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {nacionalidad} ")

'''4) Crear un programa que pida al usuario cls
el radio de un círculo e imprima por pantalla su área y
su perímetro.'''

radio = float(input("Ingrese el radio de un circulo "))

area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio

print(f"El area es {area}")
print(f"El perimetro es : {perimetro}")

'''5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.'''

segundos = int(input("Ingrese la cantidad de segundos "))

horas = segundos // 3600

print (f"Esa cantidad de segundos son en horas {horas} ")

'''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número'''

numero = int(input("Ingrese el numero deseado "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

'''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.'''

primer_numero = int(input("Ingrese el primer numero, distinto de cero "))
segundo_numero = int(input("Ingrese el segundo numero, distinto de cero "))

print(f"La suma de estos numeros es: {primer_numero + segundo_numero}")
print(f"Su resta es: {primer_numero - segundo_numero}")
print(f"su divicion es: {primer_numero / segundo_numero}")
print(f"su multiplicacion es: {primer_numero * segundo_numero}")

'''Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:'''

altura = float(input("Ingrese su altura (m) "))
peso = float(input("Ingrese su peso (kg) "))

icm = peso // (altura * altura)

print(f"Su indece de masa corporal es de: {icm}")


'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:'''

temperatura_celsius = float(input("Ingrese la temperatura en celsius "))
fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"{temperatura_celsius} °C equivale a {fahrenheit} °F")


'''10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.'''

primer_numero = int(input("Ingrese un numero natural "))
segundo_numero = int(input("Ingrese el segundo numero natural "))
tercer_numero = int(input("Ingrese el segundo numero natural "))

promedio = (primer_numero + segundo_numero + tercer_numero) / 3                    
print(f"El promedio de estos numero es: {promedio}")                    

nom = input("Ingrese edad")