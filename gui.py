import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry("640x200")
        self.option_add("*Font", ("Arial", 18))
        self.title("Ejemplo de prueba")
        self.contenedor = tk.Frame(self)
        self.saludo = tk.Label(self.contenedor, text="Introduce tu nombre:")
        self.saludo.grid(row=0, column=0, padx=2.5, pady=5)
        self.entrada = tk.Entry(self.contenedor, width=20)
        self.entrada.grid(row=0, column=1, padx=2.5, pady=5)
        self.contenedor.pack()
        self.boton = tk.Button(self, text="Púlsame", command=self.pulsar)
        self.boton.pack()
        self.salida = tk.Label(self)
        self.salida.pack()
        self.lista = tk.Listbox(self, height=5)
        self.lista.pack()

    def pulsar(self, _evento=None):
        nombre = self.entrada.get()
        # messagebox.showinfo('Saludo', f'Hola {nombre}')
        self.salida.config(text=f'Hola {nombre}')
        self.entrada.delete(0, tk.END)
        self.lista.insert(tk.END, nombre)

if __name__ == '__main__':
    app = App()
    app.mainloop()
