class ProcesadorNoticias:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.noticias_procesadas = []

    def leer_archivo(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                self.noticias = archivo.readlines()
        except FileNotFoundError:
            print(f"Error: El archivo '{self.nombre_archivo}' no se encontró.")
            self.noticias = []

    def procesar_noticias(self):
        for noticia in self.noticias:
            palabras = noticia.split()
            palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= 3]
            noticia_procesada = ' '.join(palabras_filtradas)
            self.noticias_procesadas.append(noticia_procesada)

    def guardar_noticias_procesadas(self, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            for noticia_procesada in self.noticias_procesadas:
                archivo_salida.write(noticia_procesada + '\n')

    def mostrar_noticias_procesadas(self):
        for noticia_procesada in self.noticias_procesadas:
            print(noticia_procesada)

# Ejemplo de uso
nombre_archivo_entrada = 'frases.txt'
nombre_archivo_salida = 'noticias_procesadas.txt'

procesador = ProcesadorNoticias(nombre_archivo_entrada)
procesador.leer_archivo()
procesador.procesar_noticias()
procesador.mostrar_noticias_procesadas()
procesador.guardar_noticias_procesadas(nombre_archivo_salida)
