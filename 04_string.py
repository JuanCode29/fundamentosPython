name = "Juan"
las_name = "Quispe Molina"
print(name)
print(las_name)

full_name = name + " " + las_name
print(full_name)

quote = "I'AM, JUAN"
print(quote)
quote2 = 'she said, "hello"'
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + las_name
print("v1",template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, las_name)
print("v2", template)

template = f"Hola, mi nombre es {name} y mi apellido es {las_name}"
print("V3", template)