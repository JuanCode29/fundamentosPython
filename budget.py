#Promedio de gastos
#Se utiliza float para convertir el valor ingresado como string a numero de coma flotante.
budget_january = float(input("Ingrese presupuesto de january: "))
budget_february = float(input("Ingrese presupuesto de february: "))
budget_march = float(input("Ingrese presupuesto de march: "))

budget_average = (budget_january + budget_february + budget_march)/3
print(f"El promedio de presupuesto entre los meses indicados es: s/. {budget_average}")