"""
Ejemplo de GUI.
"""

import tkinter as tk

class Aplicacion(tk.Tk):
    """La clase que representa la aplicación."""

    def __init__(self):
        super().__init__()
        self.__texto_cambiado = False
        self.title("Esto es una prueba")
        # self.geometry("800x600")
        self.option_add("*Font", ("Arial", 30))
        # self.option_add("*Label.Font", ("Arial", 25))

        self.texto = tk.Label(self, text="¡Hola!")
        self.texto.pack()

        self.boton = tk.Button(self, text="Púlsame", command=self.cambiar_texto)
        self.boton.pack()

    def cambiar_texto(self):
        """Cambia el texto de la etiqueta."""
        self.__texto_cambiado = not self.__texto_cambiado
        if self.__texto_cambiado:
            self.texto.config(text="¡Adiós!")
        else:
            self.texto.config(text="¡Hola!")


app = Aplicacion()
app.mainloop()
