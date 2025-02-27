#Impotación de librerias
import sqlite3
import sys
import time

#Crear Conexión a la base de de datos SQLite3
conn = sqlite3.connect("Cuentas.db")
cursor = conn.cursor()

#Crear tabla para el registro de nuevas cuentas
cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    Correo TEXT PRIMARY KEY,
                    Nombre1 TEXT,
                    Nombre2 TEXT,
                    Apellido_Paterno TEXT,
                    Apellido_Materno TEXT,
                    Celular INTEGER,
                    Contraseña TEXT
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
        
#Bucle True para pedir al usuario que ingrese sus datos
while True: 
    #Bucle en caso de uqe usuario desee registrarse
    if accion == registro:
        nombre_1 = str(input("\nIngresa tu primer nombre\n"))
        nombre_2 = str(input("\nIngresa tu segundo nombre\n"))
        apellido_1 = str(input("\nIngresa tu primer apellido\n"))
        apellido_2 = str(input("\nIngresa tu segundo apellido\n"))
        correo = str(input("\nIngresa tu correo\n"))
        
        #Bucle True para pedir al usuario que ingrese un número de celular valido
        while True:
            try:
                telefono = int(input("\nIngresa tu número de celular\n"))
                break
            except:
                print("\nIngresa un número de celular valido\n")
    
        #Bucle True para verificar que las contraseñas coincidan
        while True:
            contraseña_1 = str(input("\nIngresa tu contraseña\n"))
            contraseña_2 = str(input("\nRepite tu contraseña\n"))
            if contraseña_1 != contraseña_2:
                print("Error la contraseñas ingresadas no coinciden")
            else:
                break
        #Validación de la existencia de la cuenta en la base de datos
        conn_login = sqlite3.connect("Cuentas.db")
        cursor_login = conn_login.cursor()
        cursor_login.execute("SELECT * FROM usuarios WHERE correo=?",(correo,))
        result_login = cursor_login.fetchone()
        if result_login:
            print("\nEl correo " +correo+ " ya esta registrado\n")
            time.sleep(5)
            sys.exit()
        else:
            cursor_login.execute("INSERT INTO usuarios (Correo,Nombre1,Nombre2,Apellido_Paterno,Apellido_Materno,Celular,Contraseña)VALUES(?,?,?,?,?,?,?)",
            (correo,nombre_1,nombre_2,apellido_1,apellido_2,telefono,contraseña_2))
            print("\nRegistro con exito\n")
            print(f"Bienvenido ' {nombre_1}''{apellido_1}'")
            conn_login.commit()
            conn_login.close()
            break
        #Bucle en caso de que el usuario desee ingresar
    if accion == ingreso:
        #Ingreso de correo y contraseña
        correo = str(input("Ingresa su correo: \n"))
        contraseña_1 = str(input("\nIngrese su contraseña: \n"))
            
        #Crea la Variable Query para buscar los datos ingresados
        conn_correo =sqlite3.connect("Registros.db")
        cursor_correo = conn_correo.cursor()
        query = """SELECT *FROM usuarios WHERE correo = ? AND contraseña = ?"""
            
        #Ejecutar el query para relaizar la busqueda
        cursor_correo.execute(query, (correo, contraseña_1))
        result_correo = cursor_correo.fetchone()
            
        #Validación si se cuentra en la base de datos, contar las columas de la tabla para que jale la info
        if result_correo:
            print("Bienvenido " +result_correo[2]+" "+result_correo[3])
            break
        else:
            print(f"No existe ningun correo registrado como: '{correo}'\no ingreso erroneamente la contraseña ")
            
            

