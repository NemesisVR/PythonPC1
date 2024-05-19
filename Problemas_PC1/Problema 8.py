# Solicitar una hora
hora = input("Introduce la hora en formato HH:MM: ")

# Extraer la hora indicada
hora = hora.split(":")[0]

# Convertir la hora a entero
hora = int(hora)

# Verificar si es hora de desayunar, almorzar o cenar
if 7 <= hora <= 8:
    print("Es hora de desayunar.")
elif 12 <= hora <= 13:
    print("Es hora de almorzar.")
elif 18 <= hora <= 19:
    print("Es hora de cenar.")
