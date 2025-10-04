'''1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300'''

precios_frutas = {'Banana': 1200,
                'Ananá': 2500,
                'Melón': 3000,
                'Uva':1450}
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

'''2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800'''



precios_frutas['Banana'] =1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

'''3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.'''

print(precios_frutas.keys())

'''4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:'''

contactos = {'Hernan': 2611231234, 'Lalo': 2611231456, 'Lolo': 2619871256, 'Lola': 2617651674, 'Pepe': 2617638906, 'Patricio': 2134568732 }
print(contactos.keys())
consultar = input('Ingrese nombre para colsultar su numero: ')
if consultar in contactos:
    numero_encontrado = contactos[consultar]
    print(f'Su numero es: {numero_encontrado}')

'''5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
'''
def procesar_frase():
    frase = input('Ingrese una frase: ').lower().capitalize()
    palabras = frase.split()
    palabras_limpias = []
    puntuacion = ".,;:!?"
    for palabra in palabras:
        palabra_limpia = palabra.strip(puntuacion)
        if palabra_limpia:
            palabras_limpias.append(palabra_limpia)
    palabras_unicas = set(palabras_limpias)
    print('\n------------------------')
    print(f'Palabras unicas: {palabras_unicas}')
    conteo_palabras = {}
    for palabra in palabras_limpias:
        conteo_palabras[palabra] = conteo_palabras.get(palabra,0) + 1 
    for palabra, conteo in conteo_palabras.items():
        print(f'{palabra} : {conteo}')
    print('--------------------------')

procesar_frase()


'''6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.'''

def promedio_notas(nota):
    promedio = sum(nota) / len(nota)
    return promedio
alumnos = {}
for i in range(1, 4):
    nombre = input('Ingrese el nombre del alumno: ').strip().capitalize()
    notas = []
    for i in range(1, 4):
        nota = float(input(f'Ingrese la nota N{i}: '))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
for nombre, notas in alumnos.items():
    promedio = promedio_notas(notas)
    print(f'El promedio de {nombre} es : {promedio:.2f}')


'''7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''


'''8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''

'''9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.'''


'''10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.'''