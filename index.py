from dotenv import load_dotenv
import os

from tkinter import *
from tkinter import ttk

from utils.querys import Consultas_sql as query

from utils.cnx import Connection
from utils.querys import Consultas_sql as query
from views.venta_interfaz import Venta_app

app = Venta_app()
app.mainloop()
