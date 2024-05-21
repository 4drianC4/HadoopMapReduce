def palabra_mas_frecuente(nombre_archivo):
    # Crear un diccionario para almacenar las palabras y sus cantidades
    frecuencias = {}

    # Abrir y leer el archivo línea por línea
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        for linea in archivo:
            # Dividir cada línea en palabra y cantidad
            partes = linea.strip().split()
            if len(partes) == 2:
                palabra = partes[0]
                cantidad = int(partes[1])
                # Almacenar en el diccionario
                frecuencias[palabra] = cantidad

    # Encontrar la palabra con la mayor cantidad
    palabra_maxima = max(frecuencias, key=frecuencias.get)
    return palabra_maxima, frecuencias[palabra_maxima]

# Ejemplo de uso
nombre_archivo = 'ejemp.txt'
palabra, cantidad = palabra_mas_frecuente(nombre_archivo)
print(f"La palabra que aparece más veces es '{palabra}' con una cantidad de {cantidad}.")
