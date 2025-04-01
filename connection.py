# pip install python-connector-mysql
import mysql.connector

class DbManager:
    # Constructor de clase para realizar la conexion
    def __init__(self, host="127.0.0.1", user="root", pwd="", db="inmomapbdd"):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=pwd,
                database=db,
            )
            print("Conexión con la base de datos realizada con éxito")
            self.cursor = self.connection.cursor() # Definimos el cursor para operar sobre la base
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos.\n{e}")
            self.connection = None

    
    def get_usuarios(self):
        self.cursor.execute("SELECT * FROM usuario")
        return self.cursor.fetchall()
    
    def get_roles(self):
        self.cursor.execute("SELECT * FROM rol")
        return self.cursor.fetchall()
    
    def get_zonas(self):
        self.cursor.execute("SELECT * FROM zonas")
        return self.cursor.fetchall()
    
    def get_usuarios_dict(self):
        self.cursor.execute("SELECT nombre, password FROM usuario")
        usuarios = self.cursor.fetchall()
        return {usuario[0]: usuario[1] for usuario in usuarios}

    # Funcion para desconectarse de la base de datos
    def desconectar(self):
        self.connection.disconnect()
        print("Fin de la conexion con la base de datos")