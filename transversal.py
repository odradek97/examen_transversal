import csv
from statistics import mean, geometric_mean
from random import randint
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez"
                ,"Pedro Rodríguez","Laura Hernández","Miguel Sánchez",
                "Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_sueldos = []
def Sueldos_Aleatorios():
    for nombre in trabajadores:
        trabajadores_sueldos.append({"Nombre": nombre, "Sueldo": randint(300000, 2500000)})

    print(trabajadores_sueldos)
    
def Clasificar_Sueldos():
    for i in trabajadores_sueldos:
        # print(i)
        if i["Sueldo"] < 800000:
            print(f"Sueldos menores a {i["Sueldo"] <= 800000} $800000")
            print(f"{i["Nombre"]} {str(i["Sueldo"])}")
        elif i["Sueldo"] > 800000 and i["Sueldo"] < 2000000:
            print(f"Sueldos entre {i["Sueldo"] > 800000 and i["Sueldo"] < 2000000} $800000 y $2000000")
            print(f"{i["Nombre"]} {str(i["Sueldo"])}")
        elif i["Sueldo"] > 2000000 and i["Sueldo"] < 2500000:
            print(f"Sueldos entre {i["Sueldo"] > 2000000 and i["Sueldo"] < 2500000} $2000000 y $2500000")
            print(f"{i["Nombre"]} {str(i["Sueldo"])}")
    
def Estadisticas():
    # for i in trabajadores_sueldos:
    #     print(i)
    try:
        sueldosxorden = [x for x in trabajadores_sueldos if x == trabajadores_sueldos["Sueldo"]]
        print(sueldosxorden)
        # for x in trabajadores_sueldos:
        #     sueldosxorden.append(x["Sueldo"])
        # print(x)
    except:
        print("Función falló")
    
def Reportes():
    try:
        with open ("registro.csv","w",newline="") as Archivo:
            writer = csv.writerow(Archivo)
            writer.writerow(["Nombre empleado", "Sueldo base", "Dcto salud", "Dcto afp", "Sueldo líquido"])
            # writer.writerow(trabajadores_sueldos)
    except:
        print("No se creó el archivo")
        # print(mean((i["Sueldo"])))

while True:
    print(f"{20*"*"}MENÚ{20*"*"}")
    print("1.- Asignar sueldos aleatorios.")
    print("2.- Clasificar sueldos.")
    print("3.- Ver estadísticas.")
    print("4.- Reporte de sueldos.")
    print("5.- Salir del programa.")
    opc = input("Ingrese opción. > ")
    if opc == "1":
        if len(trabajadores_sueldos) == 0:
            Sueldos_Aleatorios()
        else:
            print("Los sueldos ya fueron asignados")
    elif opc == "2":
        if len(trabajadores_sueldos) == 0:
            print("No hay sueldos registrados.")
        else:
            Clasificar_Sueldos()
    elif opc == "3":
        if len(trabajadores_sueldos) == 0:
            print("No hay sueldos registrados.")
        else:
            Estadisticas()
    elif opc == "4":
        if len(trabajadores_sueldos) == 0:
            print("No hay sueldos registrados.")
        else:
            Reportes()
    elif opc == "5":
        print("""Finalizando programa
Desarrollado por Daniel Betancourt
RUT 19.412.779-0""")
        break
    else:
        print("Opción inválida.")