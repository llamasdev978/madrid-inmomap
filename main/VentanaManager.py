import tkinter as tk
from tkinter import font as tkfont

AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"

class VentanaManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=BEIGE)
        self.pack(fill="both", expand=True)

        fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
        titulo = tk.Label(self, text="Manager", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
        titulo.pack(pady=(80, 50))

        # BOTONES
        boton_centro = tk.Button(self, text="Centro", font=("Arial",14), bg="blue", fg="white")
        boton_centro.place(relx=0.5, rely=0.5, anchor="center",height=30)
        boton_norte  = tk.Button(self, text="Norte", font=("Arial",14), bg="blue", fg="white")
        boton_norte.place(relx=0.5, rely=0.3, anchor="center",height=30)
        boton_sur = tk.Button(self, text="Sur", font=("Arial",14), bg="blue", fg="white")
        boton_sur.place(relx=0.5, rely=0.7, anchor="center",height=30)
        boton_este = tk.Button(self, text="Este", font=("Arial",14), bg="blue", fg="white")
        boton_este.place(relx=0.3, rely=0.5, anchor="center",height=30)
        boton_oeste = tk.Button(self, text="Oeste", font=("Arial",14), bg="blue", fg="white")
        boton_oeste.place(relx=0.7, rely=0.5, anchor="center",height=30)

   

# Código para ejecutar la ventana
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Ventana Manager")
#     root.attributes("-fullscreen", True)  # Hacer la ventana en pantalla completa
#     app = VentanaManager(master=root)
#     app.mainloop()