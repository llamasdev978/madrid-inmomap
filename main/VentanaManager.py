import tkinter as tk
from tkinter import messagebox as mb
from tkinter import font as tkfont

# Colores
AZUL_MARINO = "#1a2456"  
BEIGE = "#f5f5dc"        


#Ventana principal
ventana = tk.Tk()
ventana.title("Manager")
ventana.geometry("600x400")
ventana.configure(bg=BEIGE)
ventana.resizable(True, True)

fuente_titulo = tkfont.Font(family="Palatino Linotype", size=36, weight="bold")
titulo = tk.Label(ventana, text="Manager", font=fuente_titulo, fg=AZUL_MARINO)
titulo.pack(pady=(80, 50))


ventana.mainloop()