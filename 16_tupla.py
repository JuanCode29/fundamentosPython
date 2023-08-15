#Las tuplas se utilizan para almacenar varios elementos en una sola variable. Una tupla es una colección ordenada e inmutable, lo que significa que no podemos cambiar, agregar o eliminar elementos después de que se haya creado la tupla. .Permite elementos duplicados, están ordenados (significa que los elementos tienen un orden definido y ese orden no cambiará.) y no se pueden modificar.

#CREACIÓN DE UNA TUPLA:
#Tupla de varios elementos:
mytuple = ("apple", "banana", "cherry")
print(mytuple)
#Tupla de un elemento: Para crear una tupla con un solo elemento, debe agregar una coma después del elemento; de lo contrario, Python no lo reconocerá como una tupla.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Permite duplicados:Dado que las tuplas están indexadas, pueden tener elementos con el mismo valor:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#LONGITUD DE LA TUPLA
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#TIPOS DE DATOS:Tipos de datos de cadena, int y booleanos:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#Una tupla puede contener diferentes tipos de datos:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#Cuál es el tipo de dato:
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#El constructor tupla():También es posible usar el constructor tuple() para hacer una tupla.
thistuple = ["apple", "banana", "cherry"]
print(type(thistuple))#<class 'list'>
thistuple = tuple(["apple", "banana", "cherry"])
print(type(thistuple))#<class 'tuple'>
print(thistuple)

#ACCEDER A LOS ELEMENTOS DELA TUPLA
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Indexación negativa:La indexación negativa significa comenzar desde el final.-1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Gama de índices:La búsqueda comenzará en el índice 2 (incluido) y terminará en el índice 5 (no incluido).
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Al omitir el valor inicial, el rango comenzará en el primer elemento:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#Al omitir el valor final, el rango pasará al final de la lista:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Rango de índices negativos:Este ejemplo devuelve los elementos del índice -4 (incluido) al índice -1 (excluido)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Comprobar si el artículo existe:
thistuple = ("apple", "banana", "cherry")
print("apple" in thistuple)

#ACTUALIZAR TUPLA

#Cambiar valores de tupla: Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables. Pero hay una solución. Puede convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Agregar elementos:Convierta la tupla en una lista, agregue "naranja" y vuelva a convertirla en una tupla:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#Agregue una tupla a una tupla . Puede agregar tuplas a tuplas, por lo que si desea agregar un elemento (o muchos), cree una nueva tupla con los elementos y agréguela a la tupla existente:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Eliminar elementos:Convierta la tupla en una lista, elimine "manzana" y vuelva a convertirla en una tupla:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#O puede eliminar la tupla por completo:La palabra clave "del" puede eliminar la tupla por completo:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) # esto generará un error porque la tupla ya no existe

#DESEMPAQUETAR ELEMENTOS DE LA TUPLA
#Cuando creamos una tupla, normalmente le asignamos valores. Esto se llama "empaquetar" una tupla:
fruits = ("apple", "banana", "cherry")
#Pero, en Python, también podemos volver a extraer los valores en variables. Esto se llama "desempacar":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Nota: El número de variables debe coincidir con el número de valores en la tupla, de lo contrario, debe usar un asterisco para recopilar los valores restantes como una lista.

#Usando asterisco*:Si el número de variables es menor que el número de valores, puede agregar un *al nombre de la variable y los valores se asignarán a la variable como una lista:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#Si el asterisco se agrega a otro nombre de variable que no sea el último, Python asignará valores a la variable hasta que la cantidad de valores restantes coincida con la cantidad de variables restantes.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#RECORRIDO DE TUPLAS CON BUCLE
#Puede recorrer los elementos de la tupla mediante un forbucle.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#Bucle a través de los números de índice. También puede recorrer los elementos de la tupla haciendo referencia a su número de índice. Utilice las funciones range()y len()para crear un iterable adecuado.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Usar un ciclo while
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#UNIR TUPLAS
#Une dos tuplas. Para unir dos o más tuplas puedes usar el + operador:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiplicar tuplas. Si desea multiplicar el contenido de una tupla un número determinado de veces, puede utilizar el * operador:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#MÉTODOS DE TUPLA
#El método count() devuelve el número de veces que aparece un valor especificado en la tupla.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

#El método index() encuentra la primera aparición del valor especificado. El método index() genera una excepción si no se encuentra el valor.

#Busque la primera aparición del valor 8 y devuelva su posición:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

