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
aprobados_parcial1 = set()
aprobados_parcial2 = set()
alumnos_cant = int(input('Cuantos alumnos hay en el curso: ')) + 1
print('Ingrese los nombre de los alumnos que aprobaron el parcial "1".')
for i in range(1, alumnos_cant):
    nombres = input(f'Alumno {i}:').strip().capitalize()
    aprobados_parcial1.add(nombres)
print('Ingrese los nombre de los alumnos que aprobaron el parcial "2". ')
for j in range(1, alumnos_cant):
        nombres_2 = input(f'Nota {j}: ').strip().capitalize()
        aprobados_parcial2.add(nombres_2)

ambos = aprobados_parcial1 & aprobados_parcial2
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
al_menos_uno = aprobados_parcial1 | aprobados_parcial2

print(f'Estudiantes que aprobaron ambos parciales {ambos}.')
print(f'Estudiantes que aprobaron solo uno {solo_uno}.')
print(f'Estudiantes que aprobaron alenos uno {al_menos_uno}')


'''8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''

stock_productos = {
    "Arroz": 50,
    "Fideos": 30,
    "Aceite": 20,
    "Azúcar": 40,
    "Sal": 25,
    "Harina": 35,
    "Yerba": 45,
    "Leche": 60,
    "Galletitas": 15,
    "Café": 10
}
stock_normalizado = {k.lower(): v for k, v in stock_productos.items()}
seguir = True
while seguir:
    print("Menu")
    print('1) Ver el stock. ')
    print('2) Agregar unidades.')
    print('3) Agregar nuevo producto.')
    print('0) Finalizar.')
    opcion = int(input('Elija una opcion: '))
    match opcion:
        case 1:
            for producto, stock in stock_productos.items():
                print(f'-{producto}: {stock} unidades.')
        case 2: 
            consulta = input('Que producto desea actualizar su stock?:').strip().lower()
            if consulta not in stock_normalizado:
                print('El producto que ingreso no existe.')
                
            else:
                stock_nuevo = int(input('Ingrese la cantidad del nuevo stock: '))
                nombre_original = next(k for k in stock_productos.keys() if k.lower() == consulta)
                
                stock_productos[nombre_original] += stock_nuevo
                stock_normalizado[consulta] = stock_productos[nombre_original]

        case 3:
            producto_nuevo = input('Ingrese el producto nuevo: ').strip().lower()
            if producto_nuevo in stock_normalizado:
                print(f'El producto {producto_nuevo.capitalize()} ya existe.')
            else: 
                stock_inicial = int(input(f'Ingrese el stock inicial para {producto_nuevo.capitalize()}: '))
                nombre_guardar = producto_nuevo.capitalize()
                stock_productos[nombre_guardar] = stock_inicial
                stock_normalizado[producto_nuevo.lower()] = stock_inicial
                print(f'El producto {producto_nuevo} agregado con {stock_inicial}')
        case 0:
            seguir = False
            print('Hasta luego.')
        case _:
            print('Ingrese una opcion valida.')
        

'''9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.'''
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input('Ingresa el dia: ').lower()
hora = input('Ingresa la hora, ej: 10:00 : ')   
clave =  (dia, hora)
if clave in agenda:
    print(f'Actividad {agenda[clave]}')
else:
    print('No hay actividades ese dia.')

'''10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.'''

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}
invertido = {}
for clave,  valor in paises.items():
    invertido[valor] = clave

print(f'Original {paises}')
print(f'Invertido {invertido}')