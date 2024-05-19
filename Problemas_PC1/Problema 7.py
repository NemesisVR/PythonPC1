# Ingresar los dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Opciones disponibles
print("\nElige una opción:")
print("1. Sumar los dos números")
print("2. Restar el primero menos el segundo")
print("3. Multiplicar los dos números")

# Realizar la opción elegida
opcion = int(input("\nIntroduce tu opción (1, 2, 3): "))

# Resultado según operación
if opcion == 1:
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"La resta de {num1} menos {num2} es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
else:
    print("La opción no es válida. Por favor, introduce una opción correcta (1, 2, 3).")
