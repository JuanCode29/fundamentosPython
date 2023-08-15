txt = " ella sabe programar en python "

#len: Optiene la longitud de un string, incluye espacios en blanco"

print(txt)
print("La longitud es: ",len(txt),"\n")

txt = "     banana     "
print(txt)
print("of all fruits", txt.strip(), "is my favorite\n")#Elimina espacios al inicio y final de un string(Predeterminado)

txt = ",,,,,rrttgg.....banana....rrr"
print(txt)
print(txt.strip(",.rtg"),"\n")#Elimina caracteres al inicio y final incluyendo espacios

txt = "     banana"
print(txt)
print("of all fruits", txt.lstrip(), "is my favorite\n")#Elimina espacios al inicio(Predereterminado)

txt = ",,,,,ssaaww.....banana"
print(txt)
print(txt.lstrip(",.saw"), "\n")#Elimina caracteres al inicio incluyendo espacios

txt = "banana     "
print(txt)
print("of all fruits", txt.rstrip(), "is my favorite\n")#Elimina espacios al final del string

txt = "banana,,,,,ssqqqww....."
print(txt)
print(txt.rstrip(",.sqw"),"\n")#Elimina caracteres al final, incluyendo espacios

#Mayúsculas y minúsculas:
txt = "Hello my friends"
print(txt)
print(txt.upper(),"\n") #Mayúsculas

txt = "Hello my FRIENDS"
print(txt)
print(txt.lower(),"\n") #Minúsculas

#Validación y transformación de mayúsculas y minúsculas:

txt = "hello, and welcome to my world."
print(txt)
print(txt.capitalize(), "\n")#Primera letra en Mayúscula

txt = "wello, and welcome to my WORLD."
print(txt)
print(txt.capitalize(), "\n")#Primera letra en Mayúscula y las demás que estan en mayúsculas los convierte a minúsculas

txt = "Welcome to my world"
print(txt)
print(txt.title(),"\n")#Escribe la primera letra de cada palabra en mayúsculas:

txt = "Welcome to my 2nd world"
print(txt)
print(txt.title(),"\n")#Si la palabra contiene un número o un símbolo, la primera letra después de eso se convertirá a mayúsculas.

txt = "hello b2b2b2 and 3g3g3g"
print(txt)
print(txt.title(),"\n")#Tenga en cuenta que la primera letra después de una letra que no es del alfabeto se convierte en una letra mayúscula:

txt = "Hello My Name Is PETER"
print(txt)
print(txt.swapcase(),"\n")#Retorna las letras minúsculas en mayúsculas y las letras mayúsculas en minúsculas

#Métodos de búsqueda y conteo:
cadena = "Hola, soy una cadena de caracteres. Hola."
print(cadena)

# Método find()
posicion = cadena.find("Hola")  # Devuelve 0, la primera aparición de "Hola"
print(posicion)

posicion = cadena.find("cadena")  # Devuelve 14, la posición de la primera aparición de "cadena"
print(posicion)

posicion = cadena.find("Python")  # Devuelve -1, ya que "Python" no está en la cadena
print(posicion, "\n")

# Método count()
print(cadena)
ocurrencias = cadena.count("Hola")  # Devuelve 2, "Hola" aparece dos veces en la cadena
print(ocurrencias)

ocurrencias = cadena.count("o")  # Devuelve 3, el carácter 'o' aparece tres veces en la cadena
print(ocurrencias, "\n")

#Métodos de verificación de prefijo y sufijo:

cadena = "Hola, Mundo!"
print(cadena)
print(cadena.startswith("Hola"))  # True, ya que comienza con "Hola"
print(cadena.startswith("Mundo"), "\n")  # False, no comienza con "Mundo"

print(cadena)
print(cadena.endswith("Mundo!"))  # True, ya que termina con "Mundo!"
print(cadena.endswith("Hola"),"\n") # False, no termina con "Hola"

#Métodos de validación de strings:
cadena = "Hola123"
print(cadena)
print(cadena.isdigit())  # False, ya que contiene letras además de dígitos
print(cadena.isalpha())  # False, ya que contiene dígitos además de letras
print(cadena.isalnum(), "\n")  # True, ya que solo contiene letras y dígitos

print(cadena)
print(cadena.islower())  # False, ya que tiene letras en mayúsculas
print(cadena.isupper())  # False, ya que tiene letras en minúsculas
print(cadena.isspace(), "\n")  # False, ya que no contiene solo espacios en blanco

# Métodos de verificación de caracteres:
cadena1 = "123"
cadena2 = "12.3"

print(cadena1.isnumeric())  # True, todos los caracteres son dígitos
print(cadena2.isnumeric(), "\n")  # False, contiene el punto decimal

#El método isdecimal() devuelve True si todos los caracteres son decimales (0-9).

print(cadena1.isdecimal())  # True, todos los caracteres son dígitos decimales
print(cadena2.isdecimal(), "\n")  # False, contiene el punto decimal

#Métodos de formateo avanzado de strings:
nombre = "Juan"
edad = 30

mensaje1 = "Hola, soy {} y tengo {} años.".format(nombre, edad)
print(mensaje1, "\n")# Salida: "Hola, soy Juan y tengo 30 años."

mensaje2 = "{1} tiene {0} años.".format(edad, nombre)
print(mensaje2, "\n")# Salida: "Juan tiene 30 años."

mensaje3 = "Hola, soy {nombre} y tengo {edad} años.".format(nombre=nombre, edad=edad)
print(mensaje3, "\n")# Salida: "Hola, soy Juan y tengo 30 años."

mensaje4 = f"Hola, soy {nombre} y tengo {edad} años"
print(mensaje4, "\n")# Salida: "Hola, soy Juan y tengo 30 años."

#format_map()

# Definir un diccionario con las claves y valores para formatear el string
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(datos)
# String con marcadores de posición usando las claves del diccionario
mensaje = "Hola, soy {nombre} y tengo {edad} años. Vivo en {ciudad}."

# Usar format_map() para formatear el string con los valores del diccionario
mensaje_formateado = mensaje.format_map(datos)

print(mensaje_formateado)