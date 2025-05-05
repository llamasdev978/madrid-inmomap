import tkinter as tk
from tkinter import font as tkfont, messagebox

AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"

class VentanaAdmin(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=BEIGE)
        self.pack(fill="both", expand=True)

        fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
        titulo = tk.Label(self, text="Admin", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
        titulo.pack(pady=(20, 10))

        # Crear la lista de usuarios
        self.crear_listbox_usuarios()

    def crear_listbox_usuarios(self):
        # Etiqueta para la lista de usuarios
        label_usuarios = tk.Label(self, text="Usuarios:", bg=BEIGE, fg=AZUL_MARINO, font=("Arial", 14))
        label_usuarios.pack(pady=(10, 5))

        # Listbox para mostrar los usuarios
        self.listbox_usuarios = tk.Listbox(self, font=("Arial", 12), selectmode=tk.MULTIPLE, width=30, height=10)
        self.listbox_usuarios.pack(pady=(0, 10))

        # Agregar usuarios inventados  AGREGAR LA CONEXION A LA BASE DE DATOS( PENDIENTE)
        usuarios = ["David", "es", "un", "gran", "penco"]
        for usuario in usuarios:
            self.listbox_usuarios.insert(tk.END, usuario)

        # Botón para eliminar usuarios seleccionados
        boton_eliminar = tk.Button(self, text="Eliminar Usuarios", font=("Arial", 14), bg="red", fg="white",
                                   command=self.eliminar_usuarios)
        boton_eliminar.pack(pady=(10, 10))

    def eliminar_usuarios(self):
        # Obtener índices de los usuarios seleccionados
        seleccionados = self.listbox_usuarios.curselection()

        if not seleccionados:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún usuario.")
            return

        # Confirmar eliminación
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar los usuarios seleccionados?")
        if respuesta:
            # Eliminar usuarios seleccionados
            for indice in reversed(seleccionados):  # Recorremos en orden inverso para evitar problemas al eliminar
                self.listbox_usuarios.delete(indice)

            messagebox.showinfo("Éxito", "Usuarios eliminados correctamente.")

# # Código para ejecutar la ventana
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Ventana Admin")
#     root.geometry("600x400")  # Tamaño de la ventana
#     app = VentanaAdmin(master=root)
#     app.mainloop()
        


