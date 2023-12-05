from mysql.connector import Error
# from datetime import datetime
from .DatabaseConnection import DatabaseConnection

class HistorialCRUD:
    def __init__(self):
        self.connection = DatabaseConnection().connection
        self.cursor = self.connection.cursor()
        
    def leerHistorial(self):
        try:
            sql_select = "SELECT * FROM historial"
            self.cursor.execute(sql_select)
            records = self.cursor.fetchall()
            
            # for row in records:
            #     print(f"ID = {row[0]}, Código = {row[1]}, Respuesta = {row[2]}, Palabra clave = {row[3]}\n")
                
            return records
        except Error as e:
            print(f"Error al mostrar: {e}")
        
    def agregarHistorial(self, consulta, fecha, id_usuario, id_respuesta):
        try:
            sql_insert = "INSERT INTO historial (consulta, fecha, id_usuario, id_respuesta) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql_insert, (consulta, fecha, id_usuario, id_respuesta,))
            self.connection.commit()
            
            # print(f"Agregando respuesta:\nConsulta: {consulta}\nFecha: {fecha}\nUsuario: {id_usuario}\nRespuesta: {id_respuesta}")
            
            # historial = self.getHistorial(fecha)
            # print(f"\nRespuesta agregada: \nID: {historial[0]}\nConsulta: {historial[1]}\nFecha: {historial[2]}\nId usuario: {historial[3]}\nId respuesta: {id_respuesta}")            

        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            
    def getHistorial(self, fecha):
        try:
            sql_select = "SELECT * FROM historial WHERE fecha = %s"
            self.cursor.execute(sql_select, (fecha,))
            record = self.cursor.fetchone()

            if record:
                return record
            else:
                return "No se encontró historial para la fecha ingresada."
            
        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            
# a = HistorialCRUD()

# a.agregarHistorial("hola", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1, 1)
# a.leerHistorial()