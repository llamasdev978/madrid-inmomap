import tkinter as tk
from tkinter import messagebox as mb
import tkinter.font as tkFont

usuarios={}
def crear_login():
    ventana = tk.Tk()
    ventana.title("Inmomap-Login")
    ventana.geometry("300x200")

    titulo_label = tk.Label(ventana, 
                      text="MADRID INMOMAP", 
                      font=("Arial", 18, "bold"),  # Cambiamos a Arial y aumentamos tamaño
                      bg="#f0f0f0",
                      fg="navy")  
    titulo_label.pack(pady=15)
    

    usuario_var=tk.StringVar()
    password_var=tk.StringVar()
      # Crear el frame principal
    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(expand=True)
    # Etiquetas y campos de entrada
    tk.Label(frame, text="Usuario:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=usuario_var).grid(row=0, column=1, pady=5)
    
    tk.Label(frame, text="Contraseña:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=password_var, show="*").grid(row=1, column=1, pady=5)

    def verificar_login():
        usuario = usuario_var.get()
        password = password_var.get()

        if usuario in usuarios and usuarios[usuario] == password:
            mb.showinfo("Login", "Login exitoso, bienvenido " + usuario)
           #Cerrar la ventana de login 
            ventana.destroy()

        else:
            mb.showerror("Login", "Usuario o contraseña incorrectos")
     # Función para abrir ventana de registro
    def abrir_registro():
        ventana.destroy()  # Cerrar ventana de login
        crear_registro()   # Abrir ventana de registro
    
    # Botones
    botones_frame = tk.Frame(frame, bg="#f0f0f0")
    botones_frame.grid(row=2, column=0, columnspan=2, pady=10)
    
    tk.Button(botones_frame, text="Iniciar Sesión", command=verificar_login).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Registrarse", command=abrir_registro).pack(side=tk.LEFT, padx=5)
    
    ventana.mainloop()

#registro de usuario   
def crear_registro():
    ventana= tk.Tk()
    ventana.title("Inmomap-Registro")
    ventana.geometry("300x200")

    usuario_var=tk.StringVar()
    password_var=tk.StringVar()

    # Crear el frame principal
    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(expand=True)
    
    # Etiquetas y campos de entrada
    tk.Label(frame, text="Nuevo Usuario:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=usuario_var).grid(row=0, column=1, pady=5)
    
    tk.Label(frame, text="Contraseña:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=password_var, show="*").grid(row=1, column=1, pady=5)
    

    def registrar_ususario():
        usuario= usuario_var.get()
        password= password_var.get()

        if usuario in usuarios:
            mb.showerror("Registro", "El usuario ya existe")
            return
        if not usuario or not password:
            mb.showerror("Registro", "Por favor complete todos los campos")
            return
        
        usuarios[usuario]= password
        mb.showinfo("Registro", "Usuario registrado exitosamente")
        ventana.destroy()
        crear_login()
    
    # Botones
    tk.Button(frame, text="Registrar Usuario", command=registrar_ususario).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Volver al Login", command=lambda: [ventana.destroy(), crear_login()]).grid(row=3, column=0, columnspan=2, pady=10)
    ventana.mainloop()


crear_login()





