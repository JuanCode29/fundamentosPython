mensaje = "Hola, Mundo!"
print(mensaje)
print(mensaje[0])
print(mensaje[1])

size = len(mensaje)
print(size)

#print(mensaje[size])# Error porque el tamaño del string es 16 pero los indices van desde 0 a 15
print(mensaje[size-1], "\n")

#Indexing:
'''El indexing (indexación) se utiliza para acceder a elementos individuales de una secuencia utilizando su posición o índice. En Python, los índices comienzan desde 0 para el primer elemento, -1 para el último elemento, -2 para el penúltimo elemento y así sucesivamente.'''
print(mensaje)
print(mensaje[0])         # Salida: 'H'
print(mensaje[7])         # Salida: 'n'
print(mensaje[-1])        # Salida: '!'
print(mensaje[-2], "\n")  # Salida: 'o'

#Slicing:
'''El slicing (rebanado) se utiliza para obtener una subsecuencia de elementos de una secuencia. Permite seleccionar una parte o segmento de la secuencia original.'''

# Sintaxis del slicing: secuencia[inicio:fin:paso]

'''
inicio: Índice del primer elemento de la subsecuencia.
fin: Índice del primer elemento que no se incluirá en la subsecuencia.
paso: Paso opcional que determina cuántos elementos se saltan entre cada elemento seleccionado.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros, "\n")
print(numeros[2:6])#[3, 4, 5, 6]
print(numeros[:6])#[1, 2, 3, 4, 5, 6]
print(numeros[6:])#[7, 8, 9, 10]
print(numeros[2::2])#[3, 5, 7, 9]
print(numeros[:6:2])#[1, 3, 5]
print(numeros[::2])#[1, 3, 5, 7, 9]
print(numeros[::-1])#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

