from connection import DbManager
db = DbManager()

a = db.get_usuarios_dict()

for i in a:
    print("usuario:",i,"contraseña:",a[i], sep=" ")

logindata = {}

