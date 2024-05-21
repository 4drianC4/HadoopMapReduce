class ProcesadorFrases:
    def __init__(self, nombre_archivo_entrada, nombre_archivo_salida):
        self.nombre_archivo_entrada = nombre_archivo_entrada
        self.nombre_archivo_salida = nombre_archivo_salida
        self.frases = []

    def procesar_frases(self):
        with open(self.nombre_archivo_entrada, 'r', encoding='utf-8') as file:
            lineas = file.readlines()

        for linea in lineas:
            # Verificar si la línea tiene más de una palabra
            if len(linea.split()) > 3:
                self.frases.append(linea.strip())

    def almacenar_frases(self):
        with open(self.nombre_archivo_salida, 'w', encoding='utf-8') as file:
            for frase in self.frases:
                file.write(frase + '\n')

# Nombre del archivo de entrada y salida para procesar frases
archivo_entrada_procesar = 'page_content.txt'
archivo_salida_procesar = 'frases.txt'

# Procesar y almacenar frases
procesador_frases = ProcesadorFrases(archivo_entrada_procesar, archivo_salida_procesar)
procesador_frases.procesar_frases()
procesador_frases.almacenar_frases()


class ProcesadorNoticias:
    def __init__(self, nombre_archivo_entrada, nombre_archivo_salida):
        self.nombre_archivo_entrada = nombre_archivo_entrada
        self.nombre_archivo_salida = nombre_archivo_salida
        self.noticias_procesadas = []

    def leer_archivo(self):
        try:
            with open(self.nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
                self.noticias = archivo.readlines()
        except FileNotFoundError:
            print(f"Error: El archivo '{self.nombre_archivo_entrada}' no se encontró.")
            self.noticias = []

    def procesar_noticias(self):
        for noticia in self.noticias:
            palabras = noticia.split()
            palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= 3]
            noticia_procesada = ' '.join(palabras_filtradas)
            self.noticias_procesadas.append(noticia_procesada)

    def guardar_noticias_procesadas(self):
        with open(self.nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            for noticia_procesada in self.noticias_procesadas:
                archivo_salida.write(noticia_procesada + '\n')

    def mostrar_noticias_procesadas(self):
        for noticia_procesada in self.noticias_procesadas:
            print(noticia_procesada)

# Nombre del archivo de entrada y salida para procesar noticias
archivo_entrada_procesar = 'frases.txt'
archivo_salida_procesar = 'noticias_procesadas.txt'

# Procesar noticias
procesador_noticias = ProcesadorNoticias(archivo_entrada_procesar, archivo_salida_procesar)
procesador_noticias.leer_archivo()
procesador_noticias.procesar_noticias()
procesador_noticias.guardar_noticias_procesadas()
procesador_noticias.mostrar_noticias_procesadas()
