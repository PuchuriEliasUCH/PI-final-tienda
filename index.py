from dotenv import load_dotenv
import os

from tkinter import *
from tkinter import ttk

from utils.querys import Consultas_sql as query

from utils.cnx import Connection
from utils.querys import Consultas_sql as query
from views.venta_interfaz import Venta_app

load_dotenv()

config = {
    'user': os.getenv("BD_USER"),
    'password': os.getenv("BD_PASS"),
    'host': os.getenv("BD_HOST"),
    'database': os.getenv("BD_NAME")
}

cnx = Connection(config)

print(cnx.select_all(query.SP_LISTADO))

app = Venta_app(cnx)
app.mainloop()

