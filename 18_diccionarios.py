#DICCIONARIOS
#Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor. Un diccionario es una colección ordenada(Los elementos establecidos no se pueden cambiar, pero puede eliminar y/o agregar elementos cuando lo desee.), modificable y que no admite duplicados.

#CREACIÓN DE UN DICCIONARIO:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Elementos del diccionario: Los elementos del diccionario están ordenados, se pueden modificar y no permiten duplicados. Los elementos del diccionario se presentan en pares clave:valor y se puede hacer referencia a ellos mediante el nombre de la clave.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Cambiable: Los diccionarios se pueden cambiar, lo que significa que podemos cambiar, agregar o eliminar elementos después de que se haya creado el diccionario.

#No se permiten duplicados: Los diccionarios no pueden tener dos elementos con la misma clave:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Longitud del diccionario:
print(len(thisdict))

#TIPO DE DATOS: Los valores en los elementos del diccionario pueden ser de cualquier tipo de datos:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#tipo():Desde la perspectiva de Python, los diccionarios se definen como objetos con el tipo de datos 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#El constructor dict(): Usando el método dict() para hacer un diccionario:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#ACCEDER A ELEMENTOS A ELEMENTOS DEL DICCIONARIO:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#También hay un método llamado get()que le dará el mismo resultado:

x = thisdict.get("model")
print(x)

#OBTENER CLAVES(keys)
#El método keys() devolverá una lista de todas las claves del diccionario.
x = thisdict.keys()
print(x)

#La lista de claves es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de claves.

#EJEMPLO: Agregue un nuevo elemento al diccionario original y vea que la lista de claves también se actualice:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#OBTENER LOS VALORES 
#El método values() devolverá una lista de todos los valores en el diccionario.
x = thisdict.values()
print(x)
#La lista de valores es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de valores.

#ejemplo: Realice un cambio en el diccionario original y vea que la lista de valores también se actualice:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#ejemplo:Agregue un nuevo elemento al diccionario original y vea que la lista de valores también se actualice:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#OBTENER ITEMS
#El método items() devolverá cada elemento en un diccionario, como tuplas en una lista.
x = thisdict.items()
print(x)

#COMPROBAR SI EXISTE CLAVE
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#CAMBIAR ELEMENTOS DEL DICCIONARIO:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#ACTUALIZAR DICCIONARIO:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#AGREGAR ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Con el método update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#ELIMINAR ITEMS:
#El método pop() elimina el elemento con el nombre de clave especificado:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#El método popitem() elimina el último elemento insertado:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#La palabra clave "del" elimina el elemento con el nombre de clave especificado:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#La palabra clave "del" también puede eliminar el diccionario por completo:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#El método clear() vacía el diccionario:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#RECORRIDO DE UN DICCIONARIO

#Puede recorrer un diccionario utilizando un forbucle. Al recorrer un diccionario, el valor devuelto son las claves del diccionario, pero también hay métodos para devolver los valores .

for x in thisdict:
  print(x)

#Imprime todos los valores en el diccionario, uno por uno:

for x in thisdict:
  print(thisdict[x])

#También puede usar el método values() para devolver valores de un diccionario:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Puede usar el método keys() para devolver las claves de un diccionario:
for x in thisdict.keys():
  print(x)

#Recorra las claves y los valores usando el método items():
for x, y in thisdict.items():
  print(x, y)

#COPIAR DICCIONARIOS:

#Método copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Funcción dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#DICCIONARIOS ANIDADOS
#Cree un diccionario que contenga tres diccionarios:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["year"])
#Cree tres diccionarios, luego cree un diccionario que contenga los otros tres diccionarios:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#ACCEDER A ELEMENTOS EN DICCIONARIOS ANIDADOS: Para acceder a los elementos de un diccionario anidado, use el nombre de los diccionarios, comenzando con el diccionario externo:
print(myfamily["child2"]["name"])

#MÉTODOS

#Método fromkeys():
#Ejemplo: Cree un diccionario con 3 claves, todas con el valor 0:

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#Mismo ejemplo que el anterior, pero sin especificar el valor:
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)

#Método setdefault():devuelve el valor del elemento con la clave especificada. Si la clave no existe, inserte la clave, con el valor especificado, vea el ejemplo a continuación

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

#Obtenga el valor del elemento "color", si el elemento "color" no existe, inserte "color" con el valor "blanco":

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
print(car)

 
