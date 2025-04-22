import tkinter as tk
from tkinter import messagebox
def create_manager_window():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Manager Window")
    root.geometry("300x200")  # Tamaño de la ventana

    # Crear una etiqueta con el mensaje "manager"
    label = tk.Label(root, text="manager", font=("Arial", 16))
    label.pack(pady=50)  # Añadir un poco de espacio alrededor

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

create_manager_window()