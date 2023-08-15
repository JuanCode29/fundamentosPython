# string
my_name = "Juan"
my_name1 = 'Pablo'
print(f"Hola, soy {my_name} {my_name1}")
print(f"El tipo de dato de mi nombre ({my_name} {my_name1}) es: {type(my_name)}")

# int
print(" ")
my_age = 37
print(f"Mi nombre es: {my_name} {my_name1} y tengo {my_age} años")
print(f"Mi edad ({my_age}) es un tipo de dato:{type(my_age)}")

# bool
print("  ")
is_single = True
is_single1 = False
print(f"({is_single} y {is_single1}) son tipos de dato: {type(is_single)}")

# inputs
print("  ")
my_age = input("Cuál es tu edad: ")
print("  ")
print(f"Tu edad es: {my_age} y soy un tipo de dato: {type(my_age)}")
print("Porque capture la edad con la funcion (input()). Esto significa que independientemente de lo que ingreses (input()) lo considera como (string)")
print(" ")
print(f"Lo puedes convertir al tipo de dato correcto con (int(my_age)), ahora el tipo de dato correcto es :  {type(int(my_age))}")

# Listas (List)
print(" ")
numbers = [1, 2, 3, 4, 5]
names = ["Juan", "Pablo"]
print(f"{numbers} y {names} son tipos de datos: {type(numbers)} {type(names)}")

# Tuplas (tuple)
print(" ")
colors = ("Red", "Blue", "white")
print(f"{colors} es un tipo de datos: {type(colors)}")

# Conjuntos (set)
print(" ")
fruits = {"aplle", "orange", "pear"}
print(f"{fruits} es un tipo de datos: {type(fruits)}")

# Diccionarios (dic)
print(" ")
person = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "email": "juan@example.com"
}
print(f"{person} es un tipo de datos: {type(person)}")