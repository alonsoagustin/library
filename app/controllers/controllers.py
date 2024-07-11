from app.models.models import Libro, Biblioteca

class Controlador_Biblioteca:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_libro(self):
        titulo, autor, anio_publicacion = self.vista.obtener_datos_libro()
        libro = Libro(titulo, autor, anio_publicacion)
        mensaje = self.modelo.agregar_libro(libro)
        self.vista.mostrar_mensaje(mensaje)

    def eliminar_libro(self):
        titulo = self.vista.obtener_titulo_libro()
        mensaje = self.modelo.eliminar_libro(titulo)
        self.vista.mostrar_mensaje(mensaje)

    def prestar_libro(self):
        titulo = self.vista.obtener_titulo_libro()
        libro = self.modelo.buscar_libro(titulo)
        if libro:
            mensaje = self.modelo.prestar()
        else:
            mensaje = f'El libro "{titulo}" no se encontró en la biblioteca.'
        self.vista.mostrar_mensaje(mensaje)

    def devolver_libro(self):
        titulo = self.vista.obtener_titulo_libro()
        libro = self.modelo.buscar_libro(titulo)
        if libro:
            mensaje = libro.devolver()
        else:
            mensaje = f'El libro "{titulo}" no se encontró en la biblioteca.'
        self.vista.mostrar_mensaje(mensaje)

    def mostrar_libros_disponibles(self):
        libros = self.modelo.mostrar_libros_disponibles()
        self.vista.mostrar_libros(libros)