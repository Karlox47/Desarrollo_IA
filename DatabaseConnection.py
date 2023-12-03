import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='app-ia-1.c3cf7ysdloxz.sa-east-1.rds.amazonaws.com',
                database='app-ia',
                user='admin',
                password='admin1234'
            )
            if self.connection.is_connected():
                print("Conectado a la base de datos")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")
