#Impotación de librerias
import sqlite3

#Crear Conexión a la base de de datos SQLite3
conn = sqlite3.connect("Registros.db")
cursor = conn.cursor()

#Crear tabla para el registro de nuevas cuentas
cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
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

#Mensaje de bienvenida al usuario
print("\n>>>>>>>>>>>>>>>>>>>>> Bienvenido Usuario <<<<<<<<<<<<<<<<<<<<<<<<\n")

#Pedir nombre para saludarlo y preguntar si desea registrarse o ingresar
saludo = str(input("¿Cual es tu nombre?\n"))
accion = str(input("\n¿Que deseas hacer? " +saludo+" (registrarme/ingresar)\n"))

#Bucle True para pedir al usuario que ingrese una opción valida
while True:
    if accion == registro:
        break
    elif accion == ingreso:
        break
    else:
        print("Dato ingresado incorrecto")
        accion = str(input("¿Que deseas hacer? (registrarme/ingresar)\n"))

