"""
Ejercicio 3 opción B.
"""

import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    """La aplicación."""

    def __init__(self):
        super().__init__()
        self.option_add('*Font', ('Arial', 18))
        self.titulo = tk.Label(self, text="Gastos:")
        self.titulo.grid(row=0, column=0, columnspan=2)
        self.lista = tk.Listbox(self, width=40)
        self.lista.grid(row=1, column=0, columnspan=2)
        self.descripcion = tk.Entry(self)
        self.descripcion.grid(row=2, column=0)
        self.importe = tk.Entry(self)
        self.importe.grid(row=2, column=1)
        self.boton_agregar = tk.Button(self, text="Agregar", command=self.agregar)
        self.boton_agregar.grid(row=3, column=0)
        self.suma_total = 0.00
        self.total = tk.Label(self, text=f'Total: {self.suma_total:.2f} €')
        self.total.grid(row=3, column=1)

    def agregar(self):
        """Agrega un gasto."""
        try:
            self.suma_total += float(self.importe.get())
            self.lista.insert(tk.END, f'{self.descripcion.get()} {self.importe.get()} €')
            self.total.config(text=f'Total: {self.suma_total:.2f} €')
        except ValueError:
            messagebox.showerror('Error', 'El importe introducido no es un número válido.')


app = Aplicacion()
app.mainloop()
