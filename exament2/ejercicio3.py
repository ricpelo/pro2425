"""
Ejercicio 3.
"""

import tkinter as tk

class Aplicacion(tk.Tk):
    """La aplicación."""

    def __init__(self):
        super().__init__()
        self.option_add('*Font', ('Arial', 18))
        self.titulo = tk.Label(self, text="Tareas:")
        self.titulo.pack()
        self.lista = tk.Listbox(self, width=40)
        self.lista.pack()
        self.entrada = tk.Entry(self)
        self.entrada.pack()
        self.boton_agregar = tk.Button(self, text="Agregar", command=self.agregar)
        self.boton_agregar.pack()
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar)
        self.boton_guardar.pack()

    def agregar(self):
        """Agrega una entrada en la lista de tareas."""
        self.lista.insert(tk.END, self.entrada.get())

    def guardar(self):
        """Guarda la lista de tareas en un archivo de texto."""
        with open('tareas.txt', 'w', encoding='utf-8') as f:
            f.writelines(x + '\n' for x in self.lista.get(0, tk.END))


app = Aplicacion()
app.mainloop()
