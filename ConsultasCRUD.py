from DatabaseConnection import DatabaseConnection
from mysql.connector import Error

class CrudConsultas:
    def __init__(self):
        self.connection = DatabaseConnection().connection
        self.cursor = self.connection.cursor()
        
    # Mostrar todos las respuestas
    def leer(self):
        try:
            sql_select = "SELECT * FROM consultas"
            self.cursor.execute(sql_select)
            records = self.cursor.fetchall()

            for row in records:
                print(f"ID = {row[0]}, Consulta = {row[1]}, Código = {row[2]}, Palabra clave = {row[3]}\n")
        except Error as e:
            print(f"Error al mostrar: {e}")
    
    def respuesta(self, palabra_clave):
        try:
            sql_select = "SELECT respuesta FROM consultas WHERE palabra_clave = %s"
            self.cursor.execute(sql_select, (palabra_clave,))
            record = self.cursor.fetchone()

            if record:
                return record[0]
            else:
                return "No se encontró respuesta para la palabra clave ingresada."
            
        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            return "Error al obtener respuesta."

a = CrudConsultas()
a.leer()
print(a.respuesta("proxima"))