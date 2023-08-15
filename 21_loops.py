matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz)

for fila in matriz:
  for elemento in fila:
    print(elemento, end="\t")
  print()

# Mostrar solo hasta la segunda columna:
for fila in matriz:
  for elemento in fila[:2]:
    print(elemento, end="\t")
  print()

#Mostrar solo la segunda columna:
for fila in matriz:
  segunda_columna = fila[1]
  print(segunda_columna)
  print()

#Mostar solo las 2 primeras filas:
for fila in matriz[:2]:
  for elemento in fila:
    print(elemento, end="\t")
  print()

#ITERAR SOBRE UNA LISTA DE DICCIONARIOS
lista_de_diccionarios = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Carlos", "edad": 28}
]

for persona in lista_de_diccionarios:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")