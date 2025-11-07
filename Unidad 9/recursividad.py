# 1 - Crea una función recursiva que calcule el factorial de un número. Luego, utiliza
# esa función para calcular y mostrar en pantalla el factorial de todos los números
# enteros entre 1 y el número que indique el usuario

def calcular_factorial(numero):
    if numero <= 1:
        return 1
    return numero * calcular_factorial(numero - 1)

try:
    limite = int(input("Escribí un número entero positivo: "))
    if limite < 1:
        print("El número debe ser mayor que cero.")
    else:
        print(f"\nFactoriales del 1 al {limite}:")
        for n in range(1, limite + 1):
            print(f"{n}! = {calcular_factorial(n)}")
except ValueError:
    print("Error: ingresá un número válido.")

# 2 - Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def obtener_fibonacci(n):
    if n < 2:
        return n
    return obtener_fibonacci(n - 1) + obtener_fibonacci(n - 2)

try:
    hasta = int(input("¿Hasta qué posición querés ver la serie de Fibonacci? "))
    if hasta < 0:
        print("La posición debe ser un número no negativo.")
    else:
        print(f"\nSerie de Fibonacci (0 a {hasta}):")
        for i in range(hasta + 1):
            print(obtener_fibonacci(i), end=" ")
        print()
except ValueError:
    print("Por favor, ingresá un número entero.")

# 3 - Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un algoritmo general.

def elevar(base, exp):
    if exp == 0:
        return 1
    return base * elevar(base, exp - 1)

try:
    b = int(input("Ingresá la base: "))
    e = int(input("Ingresá el exponente: "))
    print(f"\n{b} elevado a la {e} es: {elevar(b, e)}")
except ValueError:
    print("Error: ingresá números válidos.")

# 4 - Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.

def convertir_a_binario(num):
    if num < 2:
        return str(num)
    return convertir_a_binario(num // 2) + str(num % 2)

try:
    valor = int(input("Ingresá un número decimal para convertir a binario: "))
    if valor < 0:
        print("El número debe ser positivo.")
    else:
        binario = convertir_a_binario(valor)
        print(f"El número {valor} en binario es: {binario}")
except ValueError:
    print("Entrada inválida. Usá solo números enteros.")

# 5 - Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def verificar_palindromo(texto):
    texto = texto.lower()
    if len(texto) <= 1:
        return True
    if texto[0] == texto[-1]:
        return verificar_palindromo(texto[1:-1])
    return False

while True:
    palabra = input("Escribí una palabra para verificar si es palíndromo: ").strip()
    resultado = verificar_palindromo(palabra)
    print(f"¿'{palabra}' es palíndromo? {'Sí' if resultado else 'No'}")

    continuar = input("¿Querés probar otra palabra? (s/n): ").lower()
    if continuar != 's':
        break

# 6 - Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo
# y devuelva la suma de todos sus dígitos. No se puede convertir el número a string.

def sumar_digitos(n):
    if n < 10:
        return n
    return (n % 10) + sumar_digitos(n // 10)

try:
    numero = int(input("Ingresá un número entero positivo: "))
    if numero < 0:
        print("Debe ser un número positivo.")
    else:
        print(f"La suma de los dígitos de {numero} es: {sumar_digitos(numero)}")
except ValueError:
    print("Número inválido.")

# 7 - Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
# y devuelva el total de bloques que necesita para construir toda la pirámide.

def total_bloques(base):
    if base == 1:
        return 1
    return base + total_bloques(base - 1)

try:
    nivel_base = int(input("¿Cuántos bloques hay en la base de la pirámide? "))
    if nivel_base < 1:
        print("La base debe tener al menos un bloque.")
    else:
        print(f"Total de bloques necesarios: {total_bloques(nivel_base)}")
except ValueError:
    print("Ingresá un número válido.")

# 8 - Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_apariciones(num, dig):
    if num == 0:
        return 1 if dig == 0 else 0
    if num < 10:
        return 1 if num == dig else 0
    return (1 if num % 10 == dig else 0) + contar_apariciones(num // 10, dig)

try:
    numero = int(input("Ingresá un número entero positivo: "))
    digito = int(input("Ingresá el dígito a contar (0-9): "))
    if 0 <= digito <= 9:
        cantidad = contar_apariciones(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")
    else:
        print("El dígito debe estar entre 0 y 9.")
except ValueError:
    print("Entrada inválida.")