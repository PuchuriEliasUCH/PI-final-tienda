import mysql.connector
from .mensaje import Mensaje
from dotenv import load_dotenv
import os

from .mensaje import Mensaje


class Connection:
    load_dotenv()

    def __init__(self):
        self.cnx = None

    def conectar(self):
        try:
            self.cnx = mysql.connector.connect(
                user=os.getenv("BD_USER"),
                password=os.getenv("BD_PASS"),
                host=os.getenv("BD_HOST"),
                database=os.getenv("BD_NAME"),

            )

            if self.cnx.is_connected():
                print("Conexion extablecida")
        except mysql.connector.Error as e:
            print(e)
            self.cnx = None

    def ejecutar_consulta(self, query, args=()):
        self.conectar()
        cursor = self.cnx.cursor()
        cursor.execute(query, args)
        return cursor

    def insert(self, query, args=()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        self.cnx.close()
        return Mensaje.NUEVO_REGISTRO

    def select_by_id(self, query, args=()):
        res = None
        cursor = self.ejecutar_consulta(query, args)
        if cursor.with_rows:
            res = cursor.fetchone()
        cursor.close()
        self.cnx.close()
        return res

    def select_all(self, query, args=()):
        res = None
        cursor = self.ejecutar_consulta(query, args)
        if cursor.with_rows:
            res = cursor.fetchall()
        cursor.close()
        self.cnx.close()
        return res

    def update(self, query, args=()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        self.cnx.close()
        return "Registro actualizado correctamente"

    def delete(self, query, args=()):
        cursor = self.ejecutar_consulta(query, args)
        self.cnx.commit()
        cursor.close()
        self.cnx.close()
        return "Registo eliminado coerrectamente"

    # Reportes y consultas especificas


