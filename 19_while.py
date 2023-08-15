#VALIDACIÓN DE ENTRADA DE USUARIO:
while True:
 age = input("Ingresa tu edad: ")
 if age.isdigit():
   age = int(age)
   print(f"Tu edad es: {age}")
   break
 else:
   print("Ingresa un número válido")

#SUMA DE NÚMEROS HASTA DETENERSE:

sum = 0
continuar = True
while continuar:
  numero = float(input("Ingresa un número (0 para detenerse):"))
  if numero == 0:
    continuar = False
  else:
    sum = sum + numero
print(f"La suma de los números ingresados es: {sum}")

#GENERACIÓN DE SECUENCIAS:

# El cuadrado de los 10 primeros números:
numero = 1
limite = 10
while numero <= limite:
  cuadrado = numero**2
  print(f"El cuadrado de {numero} es {cuadrado}")
  numero +=1

#FACTORIAL DE UN NÚMERO:
n=5
origina_n = n
factorial = 1
while n >= 1:
  factorial = factorial*n
  n = n-1
print(f"El factorial de {origina_n} es: {factorial}")