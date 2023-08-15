#AGREGAMOS NUMEROS A UN LISTA 
lista = []
for i in range(1,10): #NO INCLUYE EL 10
  print(i)
  lista.append(i)
print(lista)

#RECORREMOS UNA LISTA
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#RECORREMOS UNA CADENA

string = "EL MUNDO ES ANCHO Y AGENO"
for x in string:
  if x == " ":
    continue
  print(x)

for x in "banana":
  print(x) 

#BREAK
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#FUNCIÓN range(): Tenga en cuenta que range(6) no son los valores de 0 a 6, sino los valores de 0 a 5.

for i in range(6):
  print(i)

#La función range() por defecto incrementa la secuencia en 1, sin embargo, es posible especificar el valor del incremento agregando un tercer parámetro: range(2, 30, 3 ) :
for x in range(2, 30, 3):
  print(x)

#ELSE
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nota: El bloque elsE NO se ejecutará si el bucle se detiene mediante una breakinstrucción.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#BUCLE ANIDADO: El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#DECLARACION pass:los bucles for no pueden estar vacíos, pero si por alguna razón tiene un bucle for sin contenido, ingrese la declaración pass para evitar recibir un error.

for x in [0, 1, 2]:
  pass

#IMPRESIÓN DE PATRON TRIANGULAR
n = 5

for i in range(1, n + 1):
    print("*" * i)

#RECORRIDO DE UN DICCIONARIO:

persona = {
  "nombre": "Juan", 
  "edad": 30, 
  "profesion": "ingeniero"
}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#ITERAR UNA LISTA DE DICCIONARIOS:
lista_de_diccionarios = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Carlos", "edad": 28}
]

for persona in lista_de_diccionarios:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
  