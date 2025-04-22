import tkinter as tk
from tkinter import font as tkfont

def iniciar_sesion():
    # Función para manejar el inicio de sesión
    print("Iniciando sesión...")

def registrarse():
    # Función para manejar el registro
    print("Abriendo registro...")

# Colores
AZUL_MARINO = "#1a2456"  # Azul marino elegante
BEIGE = "#f5f5dc"        # Beige suave para el fondo
BLANCO = "#ffffff"       # Blanco para los campos de texto

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Madrid InmoMap")
ventana.geometry("600x400")
ventana.configure(bg=BEIGE)
ventana.resizable(False, False)

# Crear fuente elegante para el título
fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
fuente_etiqueta = tkfont.Font(family="Palatino Linotype", size=12)
fuente_boton = tkfont.Font(family="Palatino Linotype", size=12, weight="bold")

# Título de la aplicación
titulo = tk.Label(ventana, text="Madrid InmoMap", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
titulo.pack(pady=(50, 30))

# Frame para los campos de entrada
frame_entrada = tk.Frame(ventana, bg=BEIGE)
frame_entrada.pack(pady=20)

# Usuario
etiqueta_usuario = tk.Label(frame_entrada, text="Usuario:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_usuario = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, bg=BLANCO)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

# Contraseña
etiqueta_password = tk.Label(frame_entrada, text="Contraseña:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
etiqueta_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_password = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, show="•", bg=BLANCO)
entrada_password.grid(row=1, column=1, padx=10, pady=10)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg=BEIGE)
frame_botones.pack(pady=20)

# Estilos para los botones
estilo_boton = {
    "font": fuente_boton,
    "bg": AZUL_MARINO,
    "fg": BLANCO,
    "activebackground": "#2a3466",  # Azul marino un poco más claro para el hover
    "activeforeground": BLANCO,
    "relief": tk.FLAT,
    "width": 15,
    "padx": 10,
    "pady": 5,
    "cursor": "hand2"
}

# Botón de inicio de sesión
boton_iniciar = tk.Button(frame_botones, text="Iniciar sesión", command=iniciar_sesion, **estilo_boton)
boton_iniciar.grid(row=0, column=0, padx=20, pady=10)

# Botón de registro
boton_registrar = tk.Button(frame_botones, text="Registrarse", command=registrarse, **estilo_boton)
boton_registrar.grid(row=0, column=1, padx=20, pady=10)

# Iniciar la aplicación
ventana.mainloop()