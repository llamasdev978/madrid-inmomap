import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar usuarios (en una aplicación real usarías una base de datos)
usuarios = {}

# Función para crear toda la aplicación
def crear_app_login():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Madrid InmoMap - Acceso")
    ventana.geometry("350x400")
    ventana.configure(bg="#f0f0f0")
    
    # Variables para almacenar los datos de entrada
    usuario_var = tk.StringVar()
    password_var = tk.StringVar()
    
    # Función para validar el login
    def validar_login():
        usuario = usuario_var.get()
        password = password_var.get()
        
        # Verificar si el usuario existe y la contraseña es correcta
        if usuario in usuarios and usuarios[usuario] == password:
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}")
            # Aquí puedes añadir el código para abrir la ventana principal de tu aplicación
            # Por ejemplo: abrir_ventana_principal(usuario)
            ventana.destroy()  # Cierra la ventana de login
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    # Función para registrar un nuevo usuario
    def registrar_usuario():
        usuario = usuario_var.get()
        password = password_var.get()
        
        # Validaciones básicas
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
            
        if usuario in usuarios:
            messagebox.showerror("Error", "Este nombre de usuario ya existe")
            return
            
        # Registrar el nuevo usuario
        usuarios[usuario] = password
        messagebox.showinfo("Éxito", f"Usuario {usuario} registrado correctamente")
        
        # Limpiar los campos después del registro
        usuario_var.set("")
        password_var.set("")
    
    # Crear título de la aplicación
    titulo = tk.Label(ventana, text="Madrid InmoMap", 
                    font=("Arial", 18, "bold"), bg="#f0f0f0")
    titulo.pack(pady=(30, 10))
    
    subtitulo = tk.Label(ventana, text="Acceso al Sistema", 
                        font=("Arial", 12), bg="#f0f0f0")
    subtitulo.pack(pady=(0, 20))
    
    # Frame para organizar los elementos del formulario
    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(pady=10)
    
    # Etiquetas y campos de entrada
    tk.Label(frame, text="Usuario:", font=("Arial", 11), 
            bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=usuario_var, font=("Arial", 11), 
            width=20).grid(row=0, column=1, pady=5, padx=5)
    
    tk.Label(frame, text="Contraseña:", font=("Arial", 11), 
            bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=password_var, font=("Arial", 11), 
            width=20, show="*").grid(row=1, column=1, pady=5, padx=5)
    
    # Frame para los botones
    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=20)
    
    # Botón de inicio de sesión
    boton_login = tk.Button(frame_botones, text="Iniciar Sesión", 
                          command=validar_login, bg="#4CAF50", fg="white",
                          font=("Arial", 11), width=12)
    boton_login.grid(row=0, column=0, padx=10)
    
    # Botón de registro
    boton_registro = tk.Button(frame_botones, text="Registrarse", 
                             command=registrar_usuario, bg="#2196F3", fg="white",
                             font=("Arial", 11), width=12)
    boton_registro.grid(row=0, column=1, padx=10)
    
    # Vincular la tecla Enter para iniciar sesión
    ventana.bind("<Return>", lambda event: validar_login())
    
    # Iniciar el bucle principal
    ventana.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    crear_app_login()