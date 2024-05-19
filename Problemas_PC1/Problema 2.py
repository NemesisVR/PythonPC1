# Solicitar al usuario que ingrese el costo y porcentaje 
costo_comida = float(input("¿Cuánto fue el costo de su comida en el restaurante? $"))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar al mesero? (%) "))

# Cantidad de propina
propina = costo_comida * (porcentaje_propina / 100)

# Mostrar la cantidad de propina 
print("Debe dejar $", propina, "como propina al mesero.")
