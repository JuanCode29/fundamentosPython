is_single = True
print(type(is_single))
is_single =  False
print(is_single)

print(not True)
print(not False)

is_single = not is_single
print(is_single)

#tipos de datos y valores que se pueden interpretar como False en un contexto booleano.
valor1 = True
valor2 = False
valor3 = None
valor4 = 0
valor5 = 0.0
valor6 = ''
valor7 = []
valor8 = {}

print(f"{bool(valor1)} {bool(valor2)} {bool(valor3)} {bool(valor4)} {bool(valor5)} {bool(valor6)} {bool(valor7)} {bool(valor8)}")

#Cualquier valor diferente de los mencionados anteriormente se interpreta como True
valor4 = 1
valor5 = 2.2
valor6 = 'Hola'
valor7 = ["Juan", "Jose"]
valor8 = {"Pedro", "Pablo"}

print(f"{bool(valor4)} {bool(valor5)} {bool(valor6)} {bool(valor7)} {bool(valor8)}")
