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

        self.entrada = tk.Entry(self)
        self.entrada.pack()

        self.boton = tk.Button(self, text="Púlsame", command=self.cambiar_texto)
        self.boton.pack()

        self.salida = tk.Label(self, text="")
        self.salida.pack()

        self.bind("<Return>", self.cambiar_texto)
        self.bind("<KP_Enter>", self.cambiar_texto)

    def cambiar_texto(self, event=None):
        """
        Cambia el texto de la etiqueta.
        El parámetro `event` es necesario para que funcione el bind().
        """
        self.__texto_cambiado = not self.__texto_cambiado
        if self.__texto_cambiado:
            self.texto.config(text="¡Adiós!")
        else:
            self.texto.config(text="¡Hola!")
        self.salida.config(text=self.entrada.get())

        # if self.texto.cget("text") == "¡Adiós!":
        #     self.texto.config(text="¡Hola!")
        # else:
        #     self.texto.config(text="¡Adiós!")


app = Aplicacion()
app.mainloop()
