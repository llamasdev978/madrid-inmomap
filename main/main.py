import tkinter as tk
from VentanaAdmin import VentanaAdmin
from VentanaManager import VentanaManager
from VentanaUsuario import VentanaUsuario

def abrir_admin():
    VentanaAdmin(root)

def abrir_manager():
    VentanaManager(root)

def abrir_usuario():
    VentanaUsuario(root)

root = tk.Tk()
root.title("Main")
root.geometry("300x200")

btn_admin = tk.Button(root, text="Abrir Admin", command=abrir_admin)
btn_admin.pack(pady=10)

btn_manager = tk.Button(root, text="Abrir Manager", command=abrir_manager)
btn_manager.pack(pady=10)

btn_usuario = tk.Button(root, text="Abrir Usuario", command=abrir_usuario)
btn_usuario.pack(pady=10)

root.mainloop()
