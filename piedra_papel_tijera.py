import random

plays = ("piedra", "papel", "tijera")

#Obtener jugadas de la PC
computer_option = random.choice(plays)

#Obtener jugadas del usuario
user_option = input("Elige: piedra, papel o tijera: ")

if user_option.lower().strip() in plays:
  if computer_option == user_option:
    result = "¡ES UN EMPATE!"
  elif computer_option == plays[0]:
    if user_option == plays[1]:
      result = "¡TU GANASTE!"
    else:
      result = "¡COMPUTADORA GANA!" 
  elif computer_option == plays[1]:
    if user_option == plays[0]:
      result = "¡COMPUTADORA GANA!"
    else:
      result = "¡TU GANASTE!"
  elif computer_option == plays[2]:
    if user_option == plays[0]:
      result = "¡TU GANASTE!"
    else:
      result = "¡COMPUTADORA GANA!"
  print(f"Usuario = {user_option}\nComputadora = {computer_option} \n")
  print(result)
else:
  print("\nOPCIÓN SELECCIONADA ES INCORRECTA")
  