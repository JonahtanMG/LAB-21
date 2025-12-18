def copiar_texto(origen, destino):
    try:
        with open(origen, 'rb') as archivo_origen:
            contenido = archivo_origen.read()
        
        with open(destino, 'wb') as archivo_destino:
            archivo_destino.write(contenido)
    
    except FileNotFoundError:
        print("Error: Archivo no encontrado")

copiar_texto("foto.png", "copia_foto.png")