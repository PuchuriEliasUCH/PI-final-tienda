import mysql.connector

class Connection:
    def __init__(self, config):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def insert(self, query, params):
        self.cursor.execute(query, params)
        self.cnx.commit()
        return "Insertado correctamente"

    def execute(self, query, params):
        self.cursor.execute(query, params)
        self.cnx.commit()

    def close(self):
        self.cursor.close()
        self.cnx.close()
