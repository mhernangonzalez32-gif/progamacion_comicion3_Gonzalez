dias_validos = ["lunes","martes","miercoles","jueves","viernes"]
fecha = input("Ingrese la fecha (ej: lunes, 15/03): ").split(", ") #Pedimos la fecha


dia_semana = fecha[0].lower()   #dividimos el string en lista y lo guardamos en dia_semana
fecha_num = fecha[1].split("/") #separamos el string en /,  y lo guardamos en fecha_num 
dia_num = int(fecha_num[0])     #guardamos la fecha
mes_num = int(fecha_num[1])     #guardamos el mes 



if dia_semana not in dias_validos or dia_num > 31 or mes_num > 12: #En dias de semana guardamos un string y lo comparamos con la lista de los dias, los dias que no superen 31 y los meses que no superen 12
    print("Error, fecha ingresada no valida")
if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles":
    examen = input("Hubo examenes? (S/N)").lower()
    if examen == "s":
        aprobados = int(input("Cuantos aprobaron? "))
        desaprobados = int(input("Cuantos desaprobaron? "))
        total_alumnos = aprobados + desaprobados
        porcentaje = (aprobados / total_alumnos) * 100
        print(f"El porcentaje de alumnos aprovados es: {porcentaje:.2f}%")

    elif dia_semana == "jueves":
        porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if porcentaje_asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")

elif dia_semana == "viernes":
    if dia_num == 1 and (mes_num == 1 or mes_num == 7):
        print("Comienzo de nuevo ciclo")
        alunos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo "))
        arancel = float(input("Ingrese el arancel en $ por cada alumno "))  
        ingreso_total = alunos_nuevo_ciclo * arancel
        print(f"El ingreso total es: ${ingreso_total:.2f}")      



