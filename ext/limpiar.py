def almacenar_frases(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        lineas = file.readlines()

    frases = []

    for linea in lineas:
        # Verificar si la línea tiene más de una palabra
        if len(linea.split()) > 3:
            frases.append(linea.strip())

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        for frase in frases:
            file.write(frase + '\n')

# Nombre del archivo de entrada y salida
archivo_entrada = 'page_content.txt'
archivo_salida = 'frases.txt'

# Almacenar las frases
almacenar_frases(archivo_entrada, archivo_salida)

