import csv

# Base de datos
datos = [
    ["argentina", 45851378, 2736690, "america"],
    ["australia", 26974026, 7682300, "oceania"],
    ["kenia", 57532493, 580370, "africa"],
    ["japon", 122905500, 377930, "asia"],
    ["espana", 47800000, 505990, "europa"],
    ["brasil", 214326223, 8515767, "america"],
    ["canada", 38929902, 9984670, "america"],
    ["estados unidos", 334914895, 9833517, "america"],
    ["china", 1411778724, 9596961, "asia"],
    ["india", 1428627663, 3287263, "asia"],
    ["rusia", 143917000, 17098242, "europa"],
    ["francia", 68400000, 551695, "europa"],
    ["italia", 58850000, 301340, "europa"],
    ["sudafrica", 60900000, 1219090, "africa"],
    ["egipto", 112716598, 1002450, "africa"],
    ["nigeria", 227882000, 923769, "africa"],
    ["mexico", 129875529, 1964375, "america"],
    ["chile", 19963276, 756102, "america"],
    ["nueva zelanda", 5228000, 268838, "oceania"],
    ["indonesia", 277534123, 1904569, "asia"]
]

columnas = ["nombre", "poblacion", "superficie", "continente"]

# Escribir los países en un archivo CSV
with open("paises.csv", "w", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(columnas)
    escritor.writerows(datos)    

# Crear la lista para guardar los diccionarios de los países
lista_paises = []

# Leer los paises del archivo csv y agregarlos a la lista
with open("paises.csv", "r") as file:
    lector = csv.DictReader(file)
    for fila in lector:
        lista_paises.append(dict(fila))

# Funcion para ver todo de todos los paises
def ver_paises(lista):
    print("\nLISTA DE PAISES")
    print("-" * 60)
    for i in lista:
        print(f"{i['nombre']} | Población: {i['poblacion']} | Superficie: {i['superficie']} | Continente: {i['continente']}")

# Funcion para agregar un pais
def agregar_pais():
    nombre_agregar = input("Ingrese el nombre del pais: ").lower()
    poblacion_agregar = int(input("Ingrese la poblacion del pais: "))
    superficie_agregar = int(input("Ingrese la superficien del pais en KM2: "))
    opcion_continente = int(input("Seleccione el continente:\n 1-America 2-Asia 3-Europa 4-Oceania 5-Africa: "))
    
    if opcion_continente == 1:
        continente_agregar = "america"
    elif opcion_continente == 2:
        continente_agregar = "asia"
    elif opcion_continente == 3:
        continente_agregar = "europa"
    elif opcion_continente == 4:
        continente_agregar = "oceania"
    elif opcion_continente == 5:
        continente_agregar = "africa"
    else:
        print("Valor invalido")
        return
    
    lista_paises.append({
        "nombre": nombre_agregar,
        "poblacion": poblacion_agregar,
        "superficie": superficie_agregar,
        "continente": continente_agregar
    })
    print("Pais añadido con exito\n")

# Funcion para buscar un pais exacto
def buscar_pais():
    pais_busca = input("Ingrese el pais que desea buscar: ").lower()
    for i in lista_paises:
        if pais_busca == i["nombre"]:
            return i
    return f"El pais {pais_busca} no se encuentra en la lista"

# Funcion filtro por continente
def filtro_continente():
    opcion_continente = int(input("Seleccione el continente:\n 1-America 2-Asia 3-Europa 4-Oceania 5-Africa: "))
    if opcion_continente == 1:
        continente_filtro = "america"
    elif opcion_continente == 2:
        continente_filtro = "asia"
    elif opcion_continente == 3:
        continente_filtro = "europa"
    elif opcion_continente == 4:
        continente_filtro = "oceania"
    elif opcion_continente == 5:
        continente_filtro = "africa"
    else:
        print("Valor invalido")
        return
    
    print(f"\nPaises del continente {continente_filtro}:")
    for i in lista_paises:
        if i["continente"] == continente_filtro:
            print(i)
    print("")

# Funcion filtro por rango de poblacion
def filtro_poblacion():
    poblacion_min = int(input("Ingrese el minimo de la poblacion: "))
    poblacion_max = int(input("Ingrese el maximo de la poblacion: "))
    if poblacion_min > poblacion_max:
        print("ERROR la poblacion minima no puede ser mayor a la poblacion maxima")
    else:
        for i in lista_paises:
            if int(i["poblacion"]) > poblacion_min and int(i["poblacion"]) < poblacion_max:
                print(i)
    print("")

# Funcion filtro por rango de superficie
def filtro_superficie():
    superficie_min = int(input("Ingrese el minimo de la superficie: "))
    superficie_max = int(input("Ingrese el maximo de la superficie: "))
    if superficie_min > superficie_max:
        print("ERROR la superficie minima no puede ser mayor a la superficie maxima")
    else:
        for i in lista_paises:
            if int(i["superficie"]) > superficie_min and int(i["superficie"]) < superficie_max:
                print(i)
    print("")

# Funcion para ordenar los paises (manteniendo lambda)
def ordenar_paises():
    print("\nORDENAR PAISES")
    print("1 - Por nombre")
    print("2 - Por población")
    print("3 - Por superficie")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lista_paises.sort(key=lambda x: x["nombre"])
    elif opcion == 2:
        lista_paises.sort(key=lambda x: int(x["poblacion"]))
    elif opcion == 3:
        lista_paises.sort(key=lambda x: int(x["superficie"]))
    else:
        print("Opción inválida")
        return
    
    print("Países ordenados correctamente.\n")
    ver_paises(lista_paises)

# Funcion para mostrar estadisticas
def mostrar_estadisticas():
    print("\nESTADÍSTICAS GENERALES")
    total = len(lista_paises)
    if total == 0:
        print("No hay países cargados.")
        return
    
    suma_poblacion = 0
    suma_superficie = 0
    mayor_poblacion = lista_paises[0]
    menor_poblacion = lista_paises[0]

    for p in lista_paises:
        pobl = int(p["poblacion"])
        sup = int(p["superficie"])
        suma_poblacion += pobl
        suma_superficie += sup
        if pobl > int(mayor_poblacion["poblacion"]):
            mayor_poblacion = p
        if pobl < int(menor_poblacion["poblacion"]):
            menor_poblacion = p

    prom_poblacion = suma_poblacion / total
    prom_superficie = suma_superficie / total

    print(f"Cantidad total de países: {total}")
    print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']})")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']})")
    print(f"Población promedio: {prom_poblacion:.2f}")
    print(f"Superficie promedio: {prom_superficie:.2f}")
    print("")

# Bucle principal
while True:
    print("")
    print("MENÚ PRINCIPAL - GESTIÓN DE PAÍSES ")
    print("============================================")
    print("1-Ver todos los países")
    print("2-Agregar país")
    print("3-Buscar país")
    print("4-Filtrar países")
    print("5-Ordenar países")
    print("6-Mostrar estadísticas")
    print("0-Salir")
    print("===========================================")
    
    try:
        opcion = int(input("Seleccione una opción:"))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opcion == 0:
        print("GRACIAS POR USAR")
        print("Programa finalizado")
        break
    elif opcion == 1:
        ver_paises(lista_paises)
    elif opcion == 2:
        agregar_pais()
    elif opcion == 3:
        print(buscar_pais())
    elif opcion == 4:
        print("Ingrese cómo desea filtrar los países:")
        opcion_filtro = int(input("1-Continente 2-Rango de población 3-Rango de superficie: "))
        if opcion_filtro == 1:
            filtro_continente()
        elif opcion_filtro == 2:
            filtro_poblacion()
        elif opcion_filtro == 3:
            filtro_superficie()
        else:
            print("Opción inválida")
    elif opcion == 5:
        ordenar_paises()
    elif opcion == 6:
        mostrar_estadisticas()
    else:
        print("Opción inválida")
