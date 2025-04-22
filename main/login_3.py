import tkinter as tk
from tkinter import messagebox as mb
from tkinter import font as tkfont

usuarios = {}

# Colores
AZUL_MARINO = "#1a2456"  
BEIGE = "#f5f5dc"        
BLANCO = "#ffffff"       

# Función para verificar el login 
def verificar_login(ventana_login, usuario_var, password_var):
    usuario = usuario_var.get()
    password = password_var.get()

    if usuario in usuarios and usuarios[usuario] == password:
        mb.showinfo("Login", "Login exitoso, bienvenido " + usuario)
        # Cerrar la ventana de login 
        ventana_login.destroy()
    else:
        mb.showerror("Login", "Usuario o contraseña incorrectos")

def crear_login():
    
    ventana_login = tk.Toplevel(ventana)
    ventana_login.title("Iniciar sesión")
    ventana_login.geometry("600x400")
    ventana_login.configure(bg=BEIGE)
    ventana_login.resizable(True, True)
    ventana_login.transient(ventana)  # Hace que esta ventana sea dependiente de la principal
    ventana_login.grab_set()  # Mantiene esta ventana como activa

    # Título de la ventana de login
    titulo_login = tk.Label(ventana_login, text="Iniciar Sesión", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
    titulo_login.pack(pady=(30, 20))

    # Variables 
    usuario_var = tk.StringVar()
    password_var = tk.StringVar()

    # Crear el frame principal
    frame = tk.Frame(ventana_login, bg=BEIGE)
    frame.pack(pady=20)

    # Usuario
    etiqueta_usuario = tk.Label(frame, text="Usuario:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_usuario = tk.Entry(frame, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=usuario_var)
    entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

    # Contraseña
    etiqueta_password = tk.Label(frame, text="Password:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entrada_password = tk.Entry(frame, width=30, font=fuente_etiqueta, show="•", bg=BLANCO, textvariable=password_var)
    entrada_password.grid(row=1, column=1, padx=10, pady=10)

    # Botón de acceso 
    boton_acceder = tk.Button(
        frame,
        text="Iniciar sesión",
        command=lambda: verificar_login(ventana_login, usuario_var, password_var),
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
    )
    boton_acceder.grid(row=2, column=0, columnspan=2, pady=20)  

  

def registrar_usuario(ventana_registro, usuario_var, nombre_var, correo_var, password_var):
   
    usuario = usuario_var.get()
    nombre = nombre_var.get()
    correo = correo_var.get()
    password = password_var.get()
    
    # Verificación de campos vacíos
    if not all([nombre, usuario, correo, password]):
        mb.showerror("Error", "Por favor, complete todos los campos")
        return

    '''  
    # Verificación simple de formato de correo
    if '@' not in correo or '.' not in correo:
        mb.showerror("Error", "Por favor, ingrese un correo electrónico válido")
        return
    '''
    # Verificar si el usuario ya existe
    if usuario in usuarios:
        mb.showerror("Error", "El usuario ya existe")
        return
        
    # Registrar nuevo usuario
    usuarios[usuario] = password
    mb.showinfo("Registro Exitoso", f"Usuario {usuario} registrado correctamente")
    ventana_registro.destroy()

def crear_registro():
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro - Madrid InmoMap")
    ventana_registro.geometry("500x400")
    ventana_registro.configure(bg=BEIGE)
    ventana_registro.resizable(True, True)
    ventana_registro.transient(ventana)
    ventana_registro.grab_set()

    # Variables para los campos de entrada
    usuario_var = tk.StringVar()
    nombre_var = tk.StringVar()
    correo_var = tk.StringVar()
    password_var = tk.StringVar()

    # Título de la ventana de registro
    titulo_registro = tk.Label(ventana_registro, text="Registro", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
    titulo_registro.pack(pady=(10, 10))

    # Frame para los campos de entrada
    frame_entrada = tk.Frame(ventana_registro, bg=BEIGE)
    frame_entrada.pack(pady=20)

    # Usuario
    etiqueta_usuario = tk.Label(frame_entrada, text="Usuario:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_usuario = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=usuario_var)
    entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

    # Nombre 
    etiqueta_nombre = tk.Label(frame_entrada, text="Nombre:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entrada_nombre = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=nombre_var)
    entrada_nombre.grid(row=1, column=1, padx=10, pady=10)

    # Correo
    etiqueta_correo = tk.Label(frame_entrada, text="Correo:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_correo.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entrada_correo = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, bg=BLANCO, textvariable=correo_var)
    entrada_correo.grid(row=2, column=1, padx=10, pady=10)

    # Password
    etiqueta_password = tk.Label(frame_entrada, text="Contraseña:", font=fuente_etiqueta, bg=BEIGE, fg=AZUL_MARINO)
    etiqueta_password.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entrada_password = tk.Entry(frame_entrada, width=30, font=fuente_etiqueta, show="•", bg=BLANCO, textvariable=password_var)
    entrada_password.grid(row=3, column=1, padx=10, pady=10)

    # Botón de registro
    boton_registrar = tk.Button(
        frame_entrada, 
        text="Registrarse", 
        command=lambda: registrar_usuario(ventana_registro, usuario_var, nombre_var, correo_var, password_var), 
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
    )
    boton_registrar.grid(row=4, column=0, columnspan=2, pady=10)

    # Dar foco al campo de usuario
    entrada_usuario.focus_set()

# Ventana principal
ventana = tk.Tk()
ventana.title("Madrid InmoMap")
ventana.geometry("600x400")
ventana.configure(bg=BEIGE)
ventana.resizable(True, True)

# Fuentes
fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
fuente_etiqueta = tkfont.Font(family="Palatino Linotype", size=14)
fuente_boton = tkfont.Font(family="Palatino Linotype", size=12, weight="bold")

# Título principal
titulo = tk.Label(ventana, text="Madrid InmoMap", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
titulo.pack(pady=(80, 50))

# Frame para los botones
frame_botones = tk.Frame(ventana, bg=BEIGE)
frame_botones.pack(pady=30)  

# Estilos para los botones
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

# Botón de inicio de sesión
boton_iniciar = tk.Button(frame_botones, text="Iniciar sesión", command=crear_login, **estilo_boton)
boton_iniciar.grid(row=0, column=0, padx=20, pady=10)

# Botón de registro (descomentado y actualizado)
boton_registrar = tk.Button(frame_botones, text="Registrarse", command=crear_registro, **estilo_boton)
boton_registrar.grid(row=0, column=1, padx=20, pady=10)

# Iniciar la aplicación
ventana.mainloop()