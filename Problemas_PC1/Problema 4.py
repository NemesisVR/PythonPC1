# Ingresar número entero positivo
N = int(input("Introduce un entero positivo: "))

# Asegurarse que N es positivo
if N > 0:
    suma = N * (N + 1) // 2  # Usamos // para realizar una división entera
    print(f"La suma de todos los enteros es: {suma}")
else:
    print("El número no es entero positivo, ingresar otro número que cumpla el requisito.")