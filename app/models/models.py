class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True

    def prestar(self):
        # Cambia el estado del libro a no disponible.
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no esta disponible."

    def devolver(self):
        # Cambia el estado del libro a disponible.
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya esta disponible."

    def __str__(self) -> str:
        # Devuelve una representación en cadena del libro con su información.
        if self.disponible:
            estado = "disponible"
        else:
            estado = "no disponible"
        return f"{self.titulo}, Autor: {self.autor}, Año: {self.anio_publicacion}, Estado: {estado}"

class Biblioteca:
    def __init__(self) -> None:
        self.libros = []

    def agregar_libro(self,libro):
        # Añade un libro a la biblioteca.
        self.libros.append(libro)
        return f"El libro '{libro.titulo}' ha sido agregado a la bibloteca."

    def eliminar_libro(self,titulo):
        # Elimina un libro de la biblioteca por su título.
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                return f'El libro "{titulo}" ha sido eliminado de la biblioteca.'
        return f'El libro "{titulo}" no se encontró en la biblioteca.'

    def mostrar_libros_disponibles(self):
        # Muestra todos los libros que están disponibles.
        libros_disponibles = []
        for libro in self.libros:
            if libro.disponible == True:
               libros_disponibles.append(libro.titulo)
        if libros_disponibles:
                return libros_disponibles
        else: 
            return f"No hay libros disponibles."

    def buscar_libro(self,titulo):
        # Devuelve el libro con el título dado, si existe en la biblioteca.
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return f"El libro '{titulo}', no se encontró en la biblioteca."