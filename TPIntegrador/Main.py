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
    for i in lista:
        print(i)

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
#Bucle principal
while True:
    print("Seleccione una opcion")
    opcion=int(input("0-Salir 1-Ver todos los paises 2-Agregar pais 3-buscar pais 4-filtrar 5-ordenar 6-mostrar estadisticas: "))
    if opcion==0:
        print("programa finalizado")
        break
    elif opcion==1:
        ver_paises(lista_paises)
    elif opcion==2:
        agregar_pais()
    elif opcion==3:
        print(buscar_pais())
    elif opcion==4:
        print("Ingrese como desea filtrar los paises?")
        opcion_filtro=int(input("1-continente 2-Rango de poblacion 3-Rango de superficie: "))
        if opcion_filtro==1:
            filtro_continente()
        elif opcion_filtro==2:
            filtro_poblacion()
        elif opcion_filtro==3:
            filtro_superficie()
        else:
            print("Opcion invalida")