from mysql.connector import Error
from .DatabaseConnection import DatabaseConnection

class ConsultasCRUD:
    def __init__(self):
        self.connection = DatabaseConnection().connection
        self.cursor = self.connection.cursor()
        
    # Mostrar todos las respuestas
    def leer(self):
        try:
            sql_select = "SELECT * FROM consultas"
            self.cursor.execute(sql_select)
            records = self.cursor.fetchall()
            
            # for row in records:
            #     print(f"ID = {row[0]}, Código = {row[1]}, Respuesta = {row[2]}, Palabra clave = {row[3]}\n")
            # print(records)
            return records
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
            
    def agregarConsulta(self, codigo, respuesta, palabra_clave):
        try:
            sql_insert = "INSERT INTO consultas (codigo, respuesta, palabra_clave) VALUES (%s, %s, %s)"
            self.cursor.execute(sql_insert, (codigo, respuesta, palabra_clave,))
            self.connection.commit()
            print(f"Agregando respuesta:\nCódigo: {codigo}\nRespuesta: {respuesta}\nPalabra clave: {palabra_clave}")
            
            consulta = self.getConsultaByPalabraClave(palabra_clave)
            print(f"\nRespuesta agregada: \nID: {consulta[0]}\nCódigo: {consulta[1]}\nRespuesta: {consulta[2]}\nPalabra clave: {consulta[3]}")            

        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            
    def getConsultaByPalabraClave(self, palabra_clave):
        try:
            sql_select = "SELECT * FROM consultas WHERE palabra_clave = %s"
            self.cursor.execute(sql_select, (palabra_clave,))
            record = self.cursor.fetchone()

            if record:
                return record
            else:
                return "No se encontró respuesta para la palabra clave ingresada."
            
        except Error as e:
            print(f"Error al obtener respuesta: {e}")
        
    def getConsultaByRespuesta(self, respuesta):
        try:
            sql_select = "SELECT * FROM consultas WHERE respuesta = %s"
            self.cursor.execute(sql_select, (respuesta,))
            record = self.cursor.fetchone()
            
            if record:
                return record
            else:
                return "No se encontró la consulta para la respuesta ingresada."
            
        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            
    def getConsultaByID(self, id):
        try:
            sql_select = "SELECT * FROM consultas WHERE id = %s"
            self.cursor.execute(sql_select, (id,))
            record = self.cursor.fetchone()
            
            if record:
                return record
            else:
                return "No se encontró la consulta para la respuesta ingresada."
            
        except Error as e:
            print(f"Error al obtener respuesta: {e}")
            
# a = ConsultasCRUD()
# a.leer()
# a.agregarConsulta(1, "¡Hola Soy CerBot! ¿En qué puedo ayudarte?", "como tas")