# Solicitar su edad al usuario
edad = int(input("Introduce la edad del cliente: "))

# Precio de la entrada en base a su edad
if  edad < 4:
    print ('La entrada del cliente es gratis')
elif 4 <= edad <= 18:
    precio = print('El precio de la entrada es 5')
else:
    precio = print('El precio de la entrada es 10')
