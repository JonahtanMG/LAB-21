def copiar_texto(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:
            contenido = archivo_origen.read()
        
        with open(destino, 'w') as archivo_destino:
            archivo_destino.write(contenido)
    
    except FileNotFoundError:
        print("Error: Archivo no encontrado")

copiar_texto("original.txt", "copia.txt")