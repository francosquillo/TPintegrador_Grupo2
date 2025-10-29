# TPintegrador_Grupo2

DESCRIPCION DEL PROGRAMA

Este programa permite gestionar una base de datos de países utilizando un archivo CSV.
A través de un menú interactivo, el usuario puede realizar distintas acciones como:

| Ver todos los países cargados

| Agregar un nuevo país con sus datos

| Buscar un país específico

| Filtrar países por continente, población o superficie

| Ordenar los países por nombre, población o superficie

| Mostrar estadísticas generales de la base de datos

El programa lee los datos del archivo paises.csv, los convierte en diccionarios y los almacena en una lista para su gestión durante la ejecución.


INSTRUCCIONES DE USO

Ejecutar el programa en un entorno Python compatible.

Se mostrará un menú principal con opciones numeradas.

El usuario debe ingresar el número de la acción que desea realizar:

1 → Ver todos los países

2 → Agregar un país

3 → Buscar un país por nombre

4 → Filtrar países

5 → Ordenar países

6 → Mostrar estadísticas

0 → Salir del programa

Seguir las instrucciones en pantalla según la opción elegida.

Si se ingresa un valor inválido, el sistema mostrará un mensaje de error y permitirá reintentar.

El programa continúa en funcionamiento hasta que el usuario elige la opción 0


EJEMPLOS DE ENTRADAS Y SALIDAS

Ejemplo 1: Ver todos los países

| Entrada:

Seleccione una opción: 1


| Salida esperada:

LISTA DE PAISES
------------------------------------------------------------------------------------
Argentina  | Población: 45851378  | Superficie: 2736690  | Continente: america
Australia  | Población: 26974026  | Superficie: 377930   | Continente: oceania
Kenia      | Población: 57532493  | Superficie: 377930   | Continente: asia
Japon      | Población: 122905500 | Superficie: 377930   | Continente: asia
España     | Población: 47800000  | Superficie: 377930   | Continente: europa
...


Ejemplo 2: Buscar un país

| Entrada:

Seleccione una opción: 3
Ingrese el país que desea buscar: Kenia


| Salida esperada:

{'nombre': 'Kenia', 'poblacion': '57532493', 'superficie': '580370', 'continente': 'africa'}


Ejemplo 3: Agregar un país

| Entrada:

Seleccione una opción: 2
Ingrese el nombre del país: Chile
Ingrese la población del país: 19120000
Ingrese la superficie del país en KM2: 756102
Seleccione el continente:
 1-America 2-Asia 3-Europa 4-Oceania 5-Africa: 1


| Salida esperada:

País añadido con éxito


Ejemplo 4: Mostrar estadísticas

| Entrada:

Seleccione una opción: 6


| Salida esperada:

--- Estadísticas ---
País con mayor población: Japón (122905500)

País con menor población: Australia (26974026)

Promedio de población: 60028079.40

Promedio de superficie: 2783300.00

Cantidad de países por continente:
  America    : 1
  Oceania    : 1
  Africa     : 1
  Asia       : 1
  Europa     : 1



Participación de los Integrantes
-------------------------------------------------------------------------------------
Los tres integrantes colaboraron de forma conjunta en el desarrollo del programa,
distribuyendo tareas y revisando el funcionamiento del código para lograr 
un resultado completo y correcto.
 
TRABAJO REALIZADO POR: Franco Squillo, Uriel Vega y Elias perez 