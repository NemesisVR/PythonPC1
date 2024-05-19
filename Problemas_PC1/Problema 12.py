def obtener_tipo_mimetype(nombre_archivo):
    # Convertir el nombre del archivo a minúsculas para hacer la comparación 
    nombre_archivo = nombre_archivo.lower()
    
    # Verificar si el nombre del archivo termina con alguna de las extensiones señaladas
    if nombre_archivo.endswith(('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')):
        return {
            '.gif': 'image/gif',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.pdf': 'application/pdf',
            '.txt': 'text/plain',
            '.zip': 'application/zip'
        }[nombre_archivo[nombre_archivo.rfind('.'):]]
    
    # Si no coincide con ninguna extensión conocida
    return 'application/octet-stream'

# Solicitar nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener el tipo MIME que corresponde
tipo_mimetype = obtener_tipo_mimetype(nombre_archivo)

# Imprimir el resultado
print("Tipo MIME:", tipo_mimetype)
