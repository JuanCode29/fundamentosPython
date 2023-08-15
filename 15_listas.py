#TIPOS DE LISTAS
# Lista de números
numeros = [1, 2, 3, 4, 5]
print(numeros)
# Lista de strings
frutas = ["manzana", "banana", "naranja"]
print(frutas)
# Lista mixta
mixta = [10, "hola", True, [1, 2, 3]]
print(mixta, "\n")

#OPERACIONES CON LISTAS:

#Acceso a elementos por índice:
numeros = [1, 2, 3, 4, 5]
print(numeros[0])   # Salida: 1
print(numeros[2], "\n")   # Salida: 3

#Acceso con Slicing (rebanado):
numeros = [1, 2, 3, 4, 5]
sublista = numeros[1:4]
print(sublista, "\n")   # Salida: [2, 3, 4]

#MODIFICAR ELEMENTOS:
#Reemplazar un elemento en la lista
frutas = ["manzana", "banana", "naranja"]
print(frutas)
frutas[1] = "pera"
print(frutas, "\n")   # Salida: ["manzana", "pera", "naranja"]

#AGREGAR ELEMENTOS:
#Al inicio:
#Método insert():
frutas = ["manzana", "banana", "naranja"]
print(frutas)
frutas.insert(0, "mango")   # Inserta "mango" al inicio de la lista
print(frutas, "\n")   # Salida: ["mango", "manzana", "banana", "naranja"]

#Método Operador de concatenación +:
frutas = ["manzana", "banana", "naranja"]
print(frutas)
nuevas_frutas = ["mango"]
frutas = nuevas_frutas + frutas
print(frutas, "\n")   # Salida: ["mango", "manzana", "banana", "naranja"]

#Agregar elementos al final:
numeros = [1, 2, 3]
print(numeros)
#append Agrega un elemento al final de la lista
numeros.append(4)
print(numeros,"\n")

#extend Agrega varios elementos al final de la lista
numeros.extend([5, 6, 7])
print(numeros,"\n")   # Salida: [1, 2, 3, 4, 5, 6, 7]

#ELIMINAR ELEMENTOS DE UNA LISTA
#Método remove():
frutas = ["manzana", "pera", "banana", "naranja", "manzana"]
print(frutas)
frutas.remove("manzana")  # Elimina la primera aparición de "manzana"
print(frutas,"\n")   # Salida: ["pera", "banana", "naranja", "manzana"]

# Método pop():
frutas = ["manzana", "pera", "banana", "naranja"]
print(frutas)
fruta_eliminada = frutas.pop(1)  # Elimina el elemento en el índice 1 ("pera") y por defecto elimina el ultimo elemento: frutas.pop()
print(frutas)  # Salida: ["manzana", "banana", "naranja"]
print(fruta_eliminada,"\n")  # Salida: "pera"

#Método index():
frutas = ["manzana", "pera", "banana", "naranja"]
print(frutas)
indice = frutas.index("banana")  # Encuentra el índice del elemento "banana"
frutas.pop(indice)# Elimina el elemento en el índice encontrado
# O también se puede usar frutas.remove("banana") para eliminarlo directamente
print(frutas,"\n")  # Salida: ["manzana", "pera", "naranja"]

#BUSCAR ELEMENTOS EN LA LISTA
frutas = ["manzana", "pera", "naranja"]
print(frutas)
print("manzana" in frutas) # Salida: True
print(frutas.index("naranja"),"\n") # Salida: 2 (índice del elemento "naranja")

#LONGITUD DE LA LISTA
frutas = ["manzana", "pera", "naranja"]
print(frutas)
cantidad = len(frutas)
print(cantidad,"\n")   # Salida: 3

#CAMBIO DE DIRECCIÓN DE LA LISTA y ORDENAR:

#Método reverse(): se utiliza para invertir el orden de los elementos en una lista.
numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.reverse()
print(numeros,"\n")

#Método sort():El método sort() se utiliza para ordenar los elementos de una lista en orden ascendente de manera predeterminada. Si la lista contiene elementos de diferentes tipos, el método generará un error, ya que solo se pueden comparar elementos del mismo tipo.

numeros = [5, 2, 1, 4, 3]
print(numeros)
numeros.sort()
print(numeros, "\n")

#El método sort() también acepta un argumento opcional llamado reverse, que permite ordenar los elementos en orden descendente si se establece como True.
numeros.sort(reverse=True)
print(numeros)