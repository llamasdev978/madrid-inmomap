import tkinter as tk
from tkinter import messagebox as mb
from tkinter import font as tkfont
from VentanaAdmin import VentanaAdmin
from VentanaManager import VentanaManager
from VentanaUsuario import VentanaUsuario

# Diccionario de usuarios predefinidos
usuarios = {
    "1": "1",  # Admin
    "2": "2",  # Manager
    "3": "3"   # Usuario
}

# Colores
AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"
BLANCO = "#ffffff"

# Ventana principal
root = tk.Tk()
root.title("Madrid InmoMap")
root.geometry("1020x600")
root.configure(bg=BEIGE)
root.resizable(True, True)

# Fuentes
fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
fuente_etiqueta = tkfont.Font(family="Palatino Linotype", size=14)
fuente_boton = tkfont.Font(family="Palatino Linotype", size=12, weight="bold")

# Contenedor actual de frame de usuario
frame_actual = None

def mostrar_frame_usuario(frame_class):
    global frame_actual
    limpiar_root()
    frame_actual = frame_class(root)
    frame_actual.pack(fill="both", expand=True)

    boton_volver = tk.Button(root, text="Cerrar sesión", command=volver_inicio, font=fuente_boton)
    boton_volver.pack(pady=10)

def volver_inicio():
    global frame_actual
    if frame_actual is not None:
        frame_actual.destroy()
        frame_actual = None
    crear_interfaz_login()

def verificar_login(usuario_var, password_var):
    usuario = usuario_var.get()
    password = password_var.get()

    if usuario in usuarios and usuarios[usuario] == password:
        mb.showinfo("Login", f"Bienvenido usuario {usuario}")
        if usuario == "1":
            mostrar_frame_usuario(VentanaAdmin)
        elif usuario == "2":
            mostrar_frame_usuario(VentanaManager)
        elif usuario == "3":
            mostrar_frame_usuario(VentanaUsuario)
    else:
        mb.showerror("Error", "Usuario o contraseña incorrectos")

def crear_login():
    limpiar_root()
    tk.Label(root, text="Iniciar Sesión", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE).pack(pady=30)

    usuario_var = tk.StringVar()
    password_var = tk.StringVar()

    frame = tk.Frame(root, bg=BEIGE)
    frame.pack(pady=10)

    tk.Label(frame, text="Usuario:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=usuario_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Password:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, show="•", bg=BLANCO, textvariable=password_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Button(
        frame,
        text="Iniciar sesión",
        command=lambda: verificar_login(usuario_var, password_var),
        font=fuente_boton,
        bg=AZUL_MARINO,
        fg=BLANCO,
        activebackground="#2a3466",
        activeforeground=BLANCO,
        relief=tk.RAISED,
        width=15,
        padx=10,
        pady=10,
        height=2,
        borderwidth=2,
        cursor="hand2"
    ).grid(row=2, column=0, columnspan=2, pady=20)

def crear_registro():
    limpiar_root()
    tk.Label(root, text="Registro", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE).pack(pady=30)

    usuario_var = tk.StringVar()
    nombre_var = tk.StringVar()
    correo_var = tk.StringVar()
    password_var = tk.StringVar()

    frame = tk.Frame(root, bg=BEIGE)
    frame.pack(pady=10)

    tk.Label(frame, text="Usuario:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=usuario_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Nombre:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=nombre_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame, text="Correo:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=correo_var).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(frame, text="Contraseña:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(frame, width=30, font=fuente_etiqueta, show="•", bg=BLANCO, textvariable=password_var).grid(row=3, column=1, padx=10, pady=10)

    tk.Button(
        frame,
        text="Registrarse",
        command=lambda: [mb.showinfo("Registro", "Registro simulado correctamente"), crear_interfaz_login()],
        font=fuente_boton,
        bg=AZUL_MARINO,
        fg=BLANCO,
        activebackground="#2a3466",
        activeforeground=BLANCO,
        relief=tk.RAISED,
        width=10,
        padx=10,
        pady=10,
        height=1,
        borderwidth=2,
        cursor="hand2"
    ).grid(row=4, column=0, columnspan=2, pady=20)

def crear_interfaz_login():
    limpiar_root()
    tk.Label(root, text="Madrid InmoMap", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE).pack(pady=(80, 50))

    frame_botones = tk.Frame(root, bg=BEIGE)
    frame_botones.pack(pady=30)

    estilo_boton = {
        "font": fuente_boton,
        "bg": AZUL_MARINO,
        "fg": BLANCO,
        "activebackground": "#2a3466",
        "activeforeground": BLANCO,
        "relief": tk.RAISED,
        "width": 15,
        "padx": 10,
        "pady": 10,
        "height": 2,
        "borderwidth": 2,
        "cursor": "hand2"
    }

    tk.Button(frame_botones, text="Iniciar sesión", command=crear_login, **estilo_boton).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(frame_botones, text="Registrarse", command=crear_registro, **estilo_boton).grid(row=0, column=1, padx=20, pady=10)

def limpiar_root():
    for widget in root.winfo_children():
        widget.destroy()

# Mostrar interfaz de login al arrancar
crear_interfaz_login()
root.mainloop()
