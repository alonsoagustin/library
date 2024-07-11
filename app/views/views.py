class Vista_Biblioteca:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def mostrar_libros(libros):
        if libros:
            for libro in libros:
                print(libro)
        else:
            print("No hay libros disponibles.")

    @staticmethod
    def obtener_datos_libro():
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio_publicacion = int(input("Ingrese el año de publicación del libro: "))
        return titulo, autor, anio_publicacion

    @staticmethod
    def obtener_titulo_libro():
        return input("Ingrese el título del libro: ")
    
