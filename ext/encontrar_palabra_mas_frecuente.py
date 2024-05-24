from collections import Counter

def palabras_mas_frecuentes(nombre_archivo, num_palabras=10):
    # Crear un diccionario para almacenar las palabras y sus cantidades
    frecuencias = Counter()

    # Abrir y leer el archivo línea por línea
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Dividir cada línea en palabra y cantidad
            partes = linea.strip().split()
            if len(partes) == 2:
                palabra = partes[0]
                cantidad = int(partes[1])
                # Actualizar el contador de frecuencias
                frecuencias[palabra] += cantidad

    # Obtener las n palabras más frecuentes
    palabras_mas_comunes = frecuencias.most_common(num_palabras)
    return palabras_mas_comunes



# Ejemplo de uso
nombre_archivo = "part-r-00000"
palabras_comunes = palabras_mas_frecuentes(nombre_archivo)

with open("palabras_mas_frecuentes.txt", 'w', encoding='utf-8') as file:
    file.write("-------------------------------------------------------------\n")
    file.write("Las 10 noticias más relevantes son acerca de:\n")
    for palabra, cantidad in palabras_comunes:
        file.write(f"'{palabra}': {cantidad}\n")
