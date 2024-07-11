from app import *

if __name__ == "__main__":
    
    biblioteca = Biblioteca()
    vista = Vista_Biblioteca()
    controlador = Controlador_Biblioteca(biblioteca, vista)
    

    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            controlador.agregar_libro()
        elif opcion == 2:
            controlador.eliminar_libro()
        elif opcion == 3:
            controlador.prestar_libro()
        elif opcion == 4:
            controlador.devolver_libro()
        elif opcion == 5:
            controlador.mostrar_libros_disponibles()
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")