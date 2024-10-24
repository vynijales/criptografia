# ui.py

import customtkinter as ctk
from criptografia import criptografar1, descriptografar1, criptografar2, descriptografar2, criptografar3, descriptografar3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def executar_criptografia():
    tipo = tipo_var.get()
    texto = entry_input.get()
    if tipo == "1":
        a = int(entry_a.get())
        b = int(entry_b.get())
        texto_criptografado = criptografar1(texto, a, b)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_criptografado)
        entry_output.configure(state="readonly")
    elif tipo == "2":
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        texto_criptografado = criptografar2(texto, a, b, c)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_criptografado)
        entry_output.configure(state="readonly")
    elif tipo == "3":
        texto_criptografado = criptografar3(texto)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_criptografado)
        entry_output.configure(state="readonly")

def executar_descriptografia():
    tipo = tipo_var.get()
    texto = entry_input.get()
    if tipo == "1":
        a = int(entry_a.get())
        b = int(entry_b.get())
        texto_descriptografado = descriptografar1(texto, a, b)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_descriptografado)
        entry_output.configure(state="readonly")
    elif tipo == "2":
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        texto_descriptografado = descriptografar2(texto, a, b, c)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_descriptografado)
        entry_output.configure(state="readonly")
    elif tipo == "3":
        texto_descriptografado = descriptografar3(texto)
        entry_output.configure(state="normal")
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, texto_descriptografado)
        entry_output.configure(state="readonly")

def atualizar_parametros():
    tipo = tipo_var.get()
    entry_output.configure(state="normal")
    entry_output.delete(0, ctk.END)
    entry_output.configure(state="readonly")
    if tipo == "1":
        label_a.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_a.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        label_b.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        entry_b.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        label_c.grid_forget()
        entry_c.grid_forget()
    elif tipo == "2":
        label_a.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_a.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        label_b.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        entry_b.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        label_c.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        entry_c.grid(row=7, column=1, padx=10, pady=5, sticky="w")
    elif tipo == "3":
        label_a.grid_forget()
        entry_a.grid_forget()
        label_b.grid_forget()
        entry_b.grid_forget()
        label_c.grid_forget()
        entry_c.grid_forget()
    atualizar_grafico()

def atualizar_grafico():
    tipo = tipo_var.get()
    fig.clear()
    ax = fig.add_subplot(111)
    x = np.linspace(-10, 10, 400)
    if tipo == "1":
        a = int(entry_a.get()) if entry_a.get() else 1
        b = int(entry_b.get()) if entry_b.get() else 0
        y = a * x + b
        ax.plot(x, y, label=f'{a}x + {b}')
    elif tipo == "2":
        a = int(entry_a.get()) if entry_a.get() else 1
        b = int(entry_b.get()) if entry_b.get() else 0
        c = int(entry_c.get()) if entry_c.get() else 0
        y = a * x**2 + b * x + c
        ax.plot(x, y, label=f'{a}x² + {b}x + {c}')
    elif tipo == "3":
        y = x**3 + x**2 + 1
        ax.plot(x, y, label='x³ + x² + 1')
    
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    canvas.draw()

def main():
    global tipo_var, entry_input, entry_output, entry_a, entry_b, entry_c, label_a, label_b, label_c, fig, canvas

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Interface de Criptografia")
    root.geometry("600x600")

    ctk.CTkLabel(root, text="Escolha a função de criptografia:", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, columnspan=3, pady=15)

    fig = plt.Figure(figsize=(6, 2), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, pady=10)

    tipo_var = ctk.StringVar(value="1")
    ctk.CTkRadioButton(root, text="Criptografia 1º Grau", variable=tipo_var, value="1", command=atualizar_parametros).grid(row=2, column=0, padx=20, pady=10)
    ctk.CTkRadioButton(root, text="Criptografia 2º Grau", variable=tipo_var, value="2", command=atualizar_parametros).grid(row=2, column=1, padx=20, pady=10)
    ctk.CTkRadioButton(root, text="Criptografia 3º Grau", variable=tipo_var, value="3", command=atualizar_parametros).grid(row=2, column=2, padx=20, pady=10)

    ctk.CTkLabel(root, text="Texto de Entrada:", font=ctk.CTkFont(size=12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_input = ctk.CTkEntry(root, width=400)
    entry_input.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky="w")

    ctk.CTkLabel(root, text="Texto de Saída:", font=ctk.CTkFont(size=12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_output = ctk.CTkEntry(root, width=400, state="readonly")
    entry_output.grid(row=4, column=1, padx=10, pady=5, columnspan=2, sticky="w")

    label_a = ctk.CTkLabel(root, text="a:")
    entry_a = ctk.CTkEntry(root, width=200)
    entry_a.insert(0, "1")
    label_b = ctk.CTkLabel(root, text="b:")
    entry_b = ctk.CTkEntry(root, width=200)
    entry_b.insert(0, "1")
    label_c = ctk.CTkLabel(root, text="c:")
    entry_c = ctk.CTkEntry(root, width=200)
    entry_c.insert(0, "1")

    button_frame = ctk.CTkFrame(root)
    button_frame.grid(row=8, column=0, columnspan=3, pady=20)

    ctk.CTkButton(button_frame, text="Criptografar", command=executar_criptografia, height=50).pack(side="left", padx=10)
    ctk.CTkButton(button_frame, text="Descriptografar", command=executar_descriptografia, height=50).pack(side="left", padx=10)

    entry_a.bind("<KeyRelease>", lambda event: atualizar_grafico())
    entry_b.bind("<KeyRelease>", lambda event: atualizar_grafico())
    entry_c.bind("<KeyRelease>", lambda event: atualizar_grafico())

    atualizar_parametros()

    root.mainloop()

if __name__ == "__main__":
    main()
