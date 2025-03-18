# pip install python-connector-mysql
import mysql.connector

class DbManager:
    def __init__(self, host="127.0.0.1", user="root", pwd="", db="inmomapbdd"):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=pwd,
                database=db,
            )
            print("Conexión con la base de datos realizada con éxito")
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos.\n{e}")
            self.connection = None

        
    
    def desconectar(self):
        self.connection.disconnect()
        print("Fin de la conexion con la base de datos")