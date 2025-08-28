'''from utiles_es import(


)'''
hist = input('ingreso alguna opcion: (malo, regular, bueno): ').lower()
if hist == "malo":
    print("Rechazo inmediato ")
    exit(1)
else:
    exit(0)
nombre_completo = input('Ingrese nomber y apellido: ')
cuil = input('ingrese numero de cuil; ')
if int(len(str(cuil))) != 11:
    print('El numero de cuil es incorrecto')
ingreso_m = input('ingrese un monto; ')
antig = input('ingrese la cantida de años trabajados: ')


