# peso en gramos
peso_payaso = 112  
peso_muneca = 75  

# número de payasos y muñecas vendidos
num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_munecas = int(input("Introduce el número de muñecas vendidas: "))

# peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# peso del paquete
print(f"El peso total del paquete es: {peso_total} gramos")

