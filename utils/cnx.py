import mysql.connector

class Connection:
    def __init__(self, config):
        self.cnx = None
        self.cnx = mysql.connector.connect(**config)

    def ejecutar_consulta(self, query, args = ()):
        cursor = self.cnx.cursor()
        cursor.execute(query, args)
        return cursor
    
    def insert(self, query, args = ()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        return "Nuevo registro añadido correctamente"

    def select_by_id(self, query, args = ()):
        res = None
        cursor = self.ejecutar_consulta(query, args)
        if cursor.with_rows:
            res = cursor.fetchone()
        cursor.close()
        return res

    def select_all(self, query, args = ()):
        res = None
        cursor = self.ejecutar_consulta(query, args)
        if cursor.with_rows:
            res = cursor.fetchall()
        cursor.close()
        return res

    def update(self, query, args = ()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        return "Registro actualizado correctamente"

    def delete(self, query, args = ()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        return "Registo eliminado coerrectamente"
    
    # Reportes y consultas especificas

    
    def __del__(self):
        if self.cnx != None:
            self.cnx.close()