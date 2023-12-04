import mysql.connector
from mysql.connector import Error
import getpass  # Para ocultar la contraseña al ingresar

class CrudApp:
    def __init__(self):
        # Conexión a la base de datos MySQL
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host='app-ia-1.c3cf7ysdloxz.sa-east-1.rds.amazonaws.com',
                database='app-ia',
                user='admin',
                password='admin1234'
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

    def obtener_usuario_por_correo(self, correo):
        try:
            cursor = self.connection.cursor()
            sql_select = "SELECT * FROM usuarios WHERE correo = %s"
            cursor.execute(sql_select, (correo,))
            user_data = cursor.fetchone()
            return user_data
        except Error as e:
            print(f"Error al obtener información del usuario: {e}")
            return None
        
    def verificar_correo_existente(self, correo):
        try:
            cursor = self.connection.cursor()
            sql_select = "SELECT * FROM usuarios WHERE correo = %s"
            cursor.execute(sql_select, (correo,))
            user_data = cursor.fetchone()
            return user_data is not None
        except Error as e:
            print(f"Error al verificar correo existente: {e}")
            return False

    def insertar(self, nombres, apellidos, correo, contraseña):
        try:
            cursor = self.connection.cursor()
            sql_insert = "INSERT INTO usuarios (nombres, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (nombres, apellidos, correo, contraseña))
            self.connection.commit()
            print("Usuario creado con éxito.")
        except Error as e:
            print(f"Error al crear: {e}")

    def seleccionar(self):
        try:
            cursor = self.connection.cursor()
            sql_select = "SELECT * FROM usuarios"
            cursor.execute(sql_select)
            records = cursor.fetchall()

            for row in records:
                print(f"ID = {row[0]}, Nombres = {row[1]}, Apellidos = {row[2]}, Correo = {row[3]}, Contraseña = {row[4]}\n")
        except Error as e:
            print(f"Error al mostrar: {e}")

    def actualizar(self):
        id_usuario = input("Ingrese el ID del usuario para actualizar: ")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE id = {id_usuario}")
            user_data = cursor.fetchone()

            if user_data:
                nuevos_nombres = input("Actualice Nombres: ")
                nuevos_apellidos = input("Actualice Apellidos: ")
                nuevo_correo = input("Actualice Correo: ")
                nueva_contraseña = input("Actualice Contraseña: ")

                sql_update = "UPDATE usuarios SET nombres = %s, apellidos = %s, correo = %s, contraseña = %s  WHERE id = %s"
                cursor.execute(sql_update, (nuevos_nombres, nuevos_apellidos, nuevo_correo, nueva_contraseña, id_usuario))
                self.connection.commit()
                print("Se actualizó con éxito.")
            else:
                print(f"No se encontró ningún usuario con ID {id_usuario}")
        except Error as e:
            print(f"Error al actualizar: {e}")

    def eliminar(self):
        id_usuario = input("Ingrese el ID del usuario que desea eliminar: ")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE id = {id_usuario}")
            user_data = cursor.fetchone()

            if user_data:
                sql_delete = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql_delete, (id_usuario,))
                self.connection.commit()
                print("Usuario eliminado.")
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
            nombres = input("Ingrese nombres: ")
            apellidos = input("Ingrese apellidos: ")
            correo = input("Ingrese correo: ")
            contraseña = getpass.getpass("Ingrese contraseña: ")
            
            app.insertar(nombres, apellidos, correo, contraseña)
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
            print("Opción no válida.")