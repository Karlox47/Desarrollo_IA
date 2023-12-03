from crud_ia import CrudApp


if __name__ == "__main__":
    app = CrudApp()

    while True:
        print("\nMenu:")
        print("1. Insertar")
        print("2. Seleccionar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")

        choice = input("Ingrese el número de la opción que desea: ")

        if choice == "1":
            nombres = input("Ingrese nombres: ")
            apellidos = input("Ingrese apellidos: ")
            correo = input("Ingrese correo: ")
            contrasena = input("Ingrese contraseña: ")
            
            app.insertar(nombres, apellidos, correo, contrasena)
        elif choice == "2":
            app.seleccionar()
        elif choice == "3":
            app.actualizar()
        elif choice == "4":
            app.eliminar()
        elif choice == "5":
            app.db.close_connection()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")