import tkinter as tk
from tkinter import font as tkfont

AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"

class VentanaUsuario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Usuario")
        self.geometry("600x400")
        self.configure(bg=BEIGE)
        self.resizable(True, True)

        fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
        titulo = tk.Label(self, text="Usuario", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
        titulo.pack(pady=(80, 50))
