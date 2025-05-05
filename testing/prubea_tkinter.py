import tkinter as tk
from tkinter import font as tkfont

AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"

def crear_ventana():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Madrid - Distribución")
    ventana.geometry("400x400")
    
    # Usamos un Frame principal con un grid de 3x3
    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both")

    # Configuramos las filas y columnas del grid
    for i in range(3):
        frame.rowconfigure(i, weight=1)
        frame.columnconfigure(i, weight=1)
    
    # Botones
    btn_norte = tk.Button(frame, text="Norte", bg="lightblue")
    btn_sur = tk.Button(frame, text="Sur", bg="lightgreen")
    btn_este = tk.Button(frame, text="Este", bg="lightyellow")
    btn_centro = tk.Button(frame, text="Centro", bg="gold")

    # Canvas para el botón izquierdo (triángulo)
    canvas_oeste = tk.Canvas(frame, bg="white", highlightthickness=0)
    canvas_oeste.grid(row=1, column=0, sticky="nsew")
    # Dibujar un triángulo rectángulo
    canvas_oeste.create_polygon(
        0, 0,  # Punto superior izquierdo
        0, 200,  # Punto inferior izquierdo
        200, 100,  # Punto medio derecho
        fill="lightcoral", outline="black"
    )
    # Asociar un evento de clic al triángulo
    canvas_oeste.bind("<Button-1>", lambda event: mostrar_mensaje("Oeste"))

    # Posicionamiento de los botones
    btn_norte.grid(row=0, column=1, sticky="nsew")
    btn_sur.grid(row=2, column=1, sticky="nsew")
    btn_este.grid(row=1, column=2, sticky="nsew")
    btn_centro.grid(row=1, column=1, sticky="nsew")
    
    ventana.mainloop()

def mostrar_mensaje(region):
    tk.messagebox.showinfo("Información", f"Has seleccionado la región: {region}")

# Ejecutar la función para crear la ventana
crear_ventana()

