def operaciones_basicas(a, b):
  """
  Realiza suma, resta, multiplicación y división de dos números.

  :param a: El primer número.
  :param b: El segundo número (divisor en la división).
  :return: Una tupla que contiene (suma, resta, multiplicacion, division).
  """
  # Realizamos las cuatro operaciones
  suma = a + b
  resta = a - b
  multiplicacion = a * b

  # Manejamos la división por cero para evitar un error.
  if b != 0:
    division = a / b
  else:
    division = "Indefinida (División por cero)"

  # Devolvemos los resultados empaquetados en una tupla
  return (suma, resta, multiplicacion, division)

# --- Programa Principal ---

# 1. Definir los números de ejemplo (puedes pedirlos al usuario si lo deseas)
num1 = 5
num2 = 20

# 2. Llamar a la función y desempaquetar la tupla
# La tupla se desempaqueta directamente en variables individuales
try:
    resultados = operaciones_basicas(num1, num2)

    # Desempaquetado para una impresión más clara
    suma, resta, multiplicacion, division = resultados

    # 3. Mostrar los resultados de forma clara
    print(f"--- Operaciones Básicas entre {num1} y {num2} ---")
    print(f"Suma ({num1} + {num2}):            {suma}")
    print(f"Resta ({num1} - {num2}):           {resta}")
    print(f"Multiplicación ({num1} * {num2}):  {multiplicacion}")
    print(f"División ({num1} / {num2}):        {division}")

except TypeError:
    # Esto atraparía el error si la división es indefinida
    print(f"Error en los cálculos. Revisa el segundo número.")