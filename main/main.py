import tkinter as tk
from VentanaAdmin import VentanaAdmin
from VentanaManager import VentanaManager
from VentanaUsuario import VentanaUsuario

def mostrar_frame(frame_class):
    global frame_actual
    # Ocultar botones
    frame_botones.pack_forget()

    # Eliminar el frame actual si existe
    if frame_actual is not None:
        frame_actual.destroy()

    # Crear nuevo frame con botón "Volver"
    frame_actual = frame_class(root)
    boton_volver = tk.Button(frame_actual, text="Volver al inicio", command=volver_inicio)
    boton_volver.pack(pady=10)

def volver_inicio():
    global frame_actual
    if frame_actual is not None:
        frame_actual.destroy()
        frame_actual = None
    frame_botones.pack(pady=50)

# Ventana principal
root = tk.Tk()
root.title("Madrid InmoMap")
root.geometry("600x400")
root.configure(bg="#f5f5dc")

frame_actual = None

# Frame para botones de selección
frame_botones = tk.Frame(root, bg="#f5f5dc")
frame_botones.pack(pady=50)

btn_admin = tk.Button(frame_botones, text="Admin", command=lambda: mostrar_frame(VentanaAdmin))
btn_admin.grid(row=0, column=0, padx=10, pady=10)

btn_manager = tk.Button(frame_botones, text="Manager", command=lambda: mostrar_frame(VentanaManager))
btn_manager.grid(row=0, column=1, padx=10, pady=10)

btn_usuario = tk.Button(frame_botones, text="Usuario", command=lambda: mostrar_frame(VentanaUsuario))
btn_usuario.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
