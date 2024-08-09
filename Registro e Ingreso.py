#Impotación de librerias
import sqlite3

#Crear Conexión a la base de de datos SQLite3
conn = sqlite3.connect("Registros.db")
cursor = conn.cursor()
