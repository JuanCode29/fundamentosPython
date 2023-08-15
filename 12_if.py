print("Bienvenido a la calculadora simple")
number1 = float(input("Ingresa el primer número: "))
number2 = float(input("Ingresa el segundo número: "))
print("Seleccione una operación: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divición")
operation = int(input("OPERACIÓN: "))
if operation == 1:
  result = number1 + number2
elif operation == 2:
 result = number1 - number2
elif operation == 3:
 result = number1 * number2 
elif operation == 4:
  if number2 != 0:
    result = number1 / number2 
  else:
    print(f"Error: no es posible dividir entre [{number2}]")
    result = None
else:
  print("Opcion inválida")
  result = None

if result is not None:
  print(f"El resultado de la operación es: {result}")