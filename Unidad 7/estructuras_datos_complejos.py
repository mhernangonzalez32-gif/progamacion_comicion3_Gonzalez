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
