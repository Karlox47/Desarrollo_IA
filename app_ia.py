import mysql.connector
from mysql.connector import Error
import getpass  # Para ocultar la contraseña al ingresarla

class CrudApp:
    def __init__(self):
        # Conexión a la base de datos MySQL
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='app_ia',
                user='root',
                password=''
            )
            if connection.is_connected():
                print("Conectado a la base de datos")
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    # CRUD => Create Read Update Delete

    def insertar(self):
        # Función para insertar un nuevo registro en la base de datos
        nombres = input("Nombres: ")
        apellidos = input("Apellidos: ")
        correo = input("Correo: ")
        contrasena = getpass.getpass("Contraseña: ")  # Para ocultar la contraseña

        try:
            cursor = self.connection.cursor()
            sql_insert = "INSERT INTO usuarios (nombres, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (nombres, apellidos, correo, contrasena))
            self.connection.commit()
            print("Registro insertado!")
        except Error as e:
            print(f"Error al insertar: {e}")

    def seleccionar(self):
        # Función para seleccionar y mostrar todos los registros de la base de datos
        try:
            cursor = self.connection.cursor()
            sql_select = "SELECT * FROM usuarios"
            cursor.execute(sql_select)
            records = cursor.fetchall()

            for row in records:
                print(f"ID = {row[0]}, Nombres = {row[1]}, Apellidos = {row[2]}, Correo = {row[3]}, Contraseña = {row[4]}\n")
        except Error as e:
            print(f"Error al seleccionar: {e}")

    def actualizar(self):
        # Función para actualizar un registro existente en la base de datos
        idusuario = input("Ingrese el ID del usuario a actualizar: ")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE idusuarios = {idusuario}")
            user_data = cursor.fetchone()

            if user_data:
                nuevos_nombres = input("Nuevos Nombres: ")
                nuevos_apellidos = input("Nuevos Apellidos: ")
                nuevo_correo = input("Nuevo Correo: ")
                nueva_contrasena = input("Nueva Contraseña: ")

                sql_update = "UPDATE usuarios SET nombres = %s, apellidos = %s, correo = %s, contraseña = %s  WHERE idusuarios = %s"
                cursor.execute(sql_update, (nuevos_nombres, nuevos_apellidos, nuevo_correo, nueva_contrasena, idusuario))
                self.connection.commit()
                print("Registro actualizado!")
            else:
                print(f"No se encontró ningún usuario con ID {idusuario}")
        except Error as e:
            print(f"Error al actualizar: {e}")

    def eliminar(self):
        # Función para eliminar un registro de la base de datos
        id_usuario = input("Ingrese el ID del usuario que desea eliminar: ")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE idusuarios = {id_usuario}")
            user_data = cursor.fetchone()

            if user_data:
                sql_delete = "DELETE FROM usuarios WHERE idusuarios = %s"
                cursor.execute(sql_delete, (id_usuario,))
                self.connection.commit()
                print("Registro eliminado!")
            else:
                print(f"No se encontró ningún usuario con ID {id_usuario}")
        except Error as e:
            print(f"Error al eliminar: {e}")

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
            app.insertar()
        elif choice == "2":
            app.seleccionar()
        elif choice == "3":
            app.actualizar()
        elif choice == "4":
            app.eliminar()
        elif choice == "5":
            app.close_connection()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")