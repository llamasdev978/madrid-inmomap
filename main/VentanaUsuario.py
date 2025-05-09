import tkinter as tk
from tkinter import font as tkfont

AZUL_MARINO = "#1a2456"
BEIGE = "#f5f5dc"

class VentanaUsuario(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=BEIGE)
        self.pack(fill="both", expand=True)

        fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
        titulo = tk.Label(self, text="pene", font=fuente_titulo, fg=AZUL_MARINO, bg=BEIGE)
        titulo.pack(pady=(80, 50))