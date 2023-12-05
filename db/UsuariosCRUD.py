import mysql.connector
from mysql.connector import Error
import getpass
from .DatabaseConnection import DatabaseConnection  # Para ocultar la contraseña al ingresarla

class UsuariosCRUD:
    def __init__(self):
        # Conexión a la base de datos MySQL
        self.db = DatabaseConnection()
        self.connection = self.db.connection
            
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
    
#===============================================================================================================================================================================
                                                                #REALIZANDO UN CRUD => CREATE READ UPDATE DELETE
#===============================================================================================================================================================================
    # Crear usuarios
    def insertar(self, nombres, apellidos, correo, contrasena):
        try:
            cursor = self.connection.cursor()
            sql_insert = "INSERT INTO usuarios (nombres, apellidos, correo, contrasena) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (nombres, apellidos, correo, contrasena))
            self.connection.commit()
            print("Usuario creado jaaa!!!")
            return True
        except Error as e:
            print(f"Error al crear: {e}")

    # Mostrar todos los usuarios
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

    # Actualizar usuarios
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
                nueva_contrasena = input("Actualice Contraseña: ")

                sql_update = "UPDATE usuarios SET nombres = %s, apellidos = %s, correo = %s, contrasena = %s  WHERE id = %s"
                cursor.execute(sql_update, (nuevos_nombres, nuevos_apellidos, nuevo_correo, nueva_contrasena, id_usuario))
                self.connection.commit()
                print("Se actualizó con éxito.")
            else:
                print(f"No se encontró ningún usuario con ID {id_usuario}")
        except Error as e:
            print(f"Error al actualizar: {e}")

    # Eliminar usuario por ID
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

# if __name__ == "__main__":
#     app = CrudApp()

#     while True:
#         print("\nMenu:")
#         print("1. Insertar")
#         print("2. Lista de usuarios")
#         print("3. Actualizar")
#         print("4. Eliminar")
#         print("5. Salir")

#         choice = input("Ingrese el número de la opción que desea: ")

#         if choice == "1":
#             nombres = input("Ingrese nombres: ")
#             apellidos = input("Ingrese apellidos: ")
#             correo = input("Ingrese correo: ")
#             contrasena = input("Ingrese contrasena: ")
            
#             app.insertar(nombres, apellidos, correo, contrasena)
#         elif choice == "2":
#             app.seleccionar()
#         elif choice == "3":
#             app.actualizar()
#         elif choice == "4":
#             app.eliminar()
#         elif choice == "5":
#             app.close_connection()
#             print("Saliendo del programa. ¡Hasta luego!")
#             break
#         else:
#             print("Opción no válida.")
