import csv

# Base de datos
datos = [
    ["Argentina", 45851378, 2736690, "america"],
    ["Australia", 26974026, 7682300, "oceania"],
    ["Kenia", 57532493, 580370, "africa"],
    ["Japon", 122905500, 377930, "asia"],
    ["España", 47800000, 505990, "europa"]
]

columnas = ["nombre", "poblacion", "superficie", "continente"]

# Escribir los países en un archivo CSV
with open("paises.csv", "w") as file:
    escritor = csv.writer(file)
    escritor.writerow(columnas)
    escritor.writerows(datos)    

# Crear la lista para guardar los diccionarios de los países
lista_paises = []
#Leer los paises del archivo csv y agregarlos a la lista
with open("paises.csv", "r",) as file:
    lector = csv.DictReader(file)
    for fila in lector:
        lista_paises.append(dict(fila))

#funcion para ver todo de todos los paises

def ver_paises(lista):
   print("\nLISTA DE PAISES")
   print("-" * 60)
   for i in lista:
    print(f"{i['nombre']:15} | Población: {i['poblacion']:10} | Superficie: {i['superficie']:10} | Continente: {i['continente']}")

#funcion para agregar un pais
def agregar_pais():
    nombre_agregar=input("Ingrese el nombre del pais: ")
    poblacion_agregar=int(input("Ingrese la poblacion del pais: "))
    superficie_agregar=int(input("Ingrese la superficien del pais en KM2: "))
    opcion_continente=int(input("Seleccione el continente:\n 1-America 2-Asia 3-Europa 4-Oceania 5-Africa: "))
    if opcion_continente == 1:
        continente_agregar="america"
        lista_paises.append({"nombre":nombre_agregar.title(),"poblacion":poblacion_agregar,"superficie":superficie_agregar,"continente":continente_agregar})
        print("Pais añadido con exito")
        print("")
    elif opcion_continente==2:
        continente_agregar="asia"
        lista_paises.append({"nombre":nombre_agregar.title(),"poblacion":poblacion_agregar,"superficie":superficie_agregar,"continente":continente_agregar})
        print("Pais añadido con exito")
        print("")
    elif  opcion_continente==3:
        continente_agregar="europa"
        lista_paises.append({"nombre":nombre_agregar.title(),"poblacion":poblacion_agregar,"superficie":superficie_agregar,"continente":continente_agregar})
        print("Pais añadido con exito")
        print("")
    elif opcion_continente ==4:
        continente_agregar="oceania"
        lista_paises.append({"nombre":nombre_agregar.title(),"poblacion":poblacion_agregar,"superficie":superficie_agregar,"continente":continente_agregar})
        print("Pais añadido con exito")
        print("")
    elif opcion_continente ==5:
        continente_agregar ="africa"
        lista_paises.append({"nombre":nombre_agregar.title(),"poblacion":poblacion_agregar,"superficie":superficie_agregar,"continente":continente_agregar})
        print("Pais añadido con exito")
        print("")
    else:
        print("Valor invalido")
        
#Funcion para buscar un pais exacto
def buscar_pais():
    pais_busca=input("Ingrese el pais que desea buscar: ")
    for i in lista_paises:
        if pais_busca.title()==i["nombre"]:
            return i
    return f"El pais {pais_busca} no se encuentra en la lista"

#Funcion filtro por continente
def filtro_continente():
    opcion_continente=int(input("Seleccione el continente:\n 1-America 2-Asia 3-Europa 4-Oceania 5-Africa: "))
    if opcion_continente==1:
        continente_filtro="america"
    elif opcion_continente==2:
        continente_filtro="asia"
    elif opcion_continente==3:
        continente_filtro="europa"
    elif opcion_continente==4:
        continente_filtro="oceania"
    elif opcion_continente==5:
        opcion_continente="africa"
    else:
        print("Valor invalido")
        return None
    
    for i in lista_paises:
        if i["continente"]==continente_filtro:
            print(i)
    print("")

#Funcion filtro por rango de poblacion
def filtro_poblacion():
    poblacion_min=int(input("Ingrese el minimo de la poblacion: "))
    poblacion_max=int(input("Ingrese el maximo de la poblacion: "))
    if poblacion_min>poblacion_max:
        print("ERROR la poblacion minima no puede ser mayor a la poblacion maxima")
    else:
        for i in lista_paises:
            if int(i["poblacion"])>poblacion_min and int(i["poblacion"])<poblacion_max:
                print(i)
    print("")

#Funcion filtro por rango de superficie
def filtro_superficie():
    superficie_min=int(input("Ingrese el minimo de la superficie: "))
    superficie_max=int(input("Ingrese el maximo de la superficie: "))
    if superficie_min>superficie_max:
        print("ERROR la superficie minima no puede ser mayor a la poblacion maxima")
    else:
        for i in lista_paises:
            if int(i["superficie"])>superficie_min and int(i["superficie"])<superficie_max:
                print(i)
    print("")

def ordenar_paises():
    print("Ordenar países por:")
    print("1 - Nombre")
    print("2 - Población")
    print("3 - Superficie (ascendente o descendente)")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lista_ordenada = sorted(lista_paises, key=lambda x: x["nombre"])
    elif opcion == 2:
        lista_ordenada = sorted(lista_paises, key=lambda x: int(x["poblacion"]))
    elif opcion == 3:
        sentido = input("¿Desea ordenar de forma descendente? (s/n): ").lower()
        reversa = True if sentido == "s" else False
        lista_ordenada = sorted(lista_paises, key=lambda x: int(x["superficie"]), reverse=reversa)
    else:
        print("Opción inválida")
        return
    
    print("\n--- Países ordenados ---")
    for pais in lista_ordenada:
        print(f"{pais['nombre']:15} | Población: {pais['poblacion']:10} | Superficie: {pais['superficie']:10} | Continente: {pais['continente']}")
    print("")

# Mostrar estadísticas
def mostrar_estadisticas():
    for p in lista_paises:
        p["poblacion"] = int(p["poblacion"])
        p["superficie"] = int(p["superficie"])
    
    mayor = max(lista_paises, key=lambda x: x["poblacion"])
    menor = min(lista_paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in lista_paises) / len(lista_paises)
    promedio_superficie = sum(p["superficie"] for p in lista_paises) / len(lista_paises)

    print("\n--- Estadísticas ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    continentes = {}
    for p in lista_paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\nCantidad de países por continente:")
    for c, cantidad in continentes.items():
        print(f"  {c.capitalize():10}: {cantidad}")
    print("")


#Bucle principal
while True:
    print("\n" + "=" )
    print("MENÚ PRINCIPAL - GESTIÓN DE PAÍSES ")
    print("============================================" )
    print("1-Ver todos los países")
    print("2-Agregar país")
    print("3-Buscar país")
    print("4-Filtrar países")
    print("5-Ordenar países")
    print("6-Mostrar estadísticas")
    print("0-Salir")
    print("===========================================" )
    
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