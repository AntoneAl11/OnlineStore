#Impotación de librerias
import sqlite3

#Crear Conexión a la base de de datos SQLite3
conn = sqlite3.connect("Registros.db")
cursor = conn.cursor()

#Crear tabla para el registro de nuevas cuentas
cursor.execute("""
                CREATE TABLE IF NOT EXIST Usuarios (
                    correo TEXT PRIMARY KEY,
                    nombre1 TEXT,
                    nombre2 TEXT,
                    apellido1 TEXT,
                    apellido2 TEXT,
                    celular INTEGER,
                    conexion TEXT
                    )
                    """)
conn.commit()
conn.close()

#Declarar variables del usuario
nombre_1 = ""
nombre_2 = ""
apellido_1 = ""
apellido_2 = ""
correo = ""
telefono = ""
contraseña_1 = ""
conytaseña_2 = ""
registro = "registrarme"
ingreso = "ingresar"
nombre_buscar = ""

