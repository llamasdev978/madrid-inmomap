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
    
    def registro_usuario(self,nombre,correo,pwd,fnacimiento):
        self.cursor.execute(f"INSERT INTO `usuario` (`id_user`, `nombre`, `correo`, `password`, `fecha_nacimiento`, `rol_id`) VALUES (NULL, '{nombre}', '{correo}', '{pwd}', '{fnacimiento}', '3')")

    def crear_usuario_admin(self,nombre,correo,pwd,fnacimiento,rolid):
        rol = ''
        match rolid:
            case 'admin':
                rol = '1'
            case 'manager':
                rol = '2'
            case 'usuario':
                rol = '3'
            case _:
                rol = 'NULL'

        self.cursor.execute(f"INSERT INTO `usuario` (`id_user`, `nombre`, `correo`, `password`, `fecha_nacimiento`, `rol_id`) VALUES (NULL, '{nombre}', '{correo}', '{pwd}', '{fnacimiento}', '{rol}')")

    # Funcion para desconectarse de la base de datos
    def desconectar(self):
        self.connection.disconnect()
        print("Fin de la conexion con la base de datos")