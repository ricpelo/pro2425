"""
El juego del ahorcado.
"""

import tkinter as tk
import random
from tkinter import messagebox

NUM_ERRORES = 10
PALABRA_A_ADIVINAR = 'LAPIZ'

class Aplicacion(tk.Tk):
    """La clase principal del juego del ahorcado."""

    def __init__(self):
        super().__init__()
        self.title('El juego del ahorcado')
        self.option_add('*Font', ('Mono', 20))
        self.reiniciar()
        self.__frame = tk.Frame(self)
        self.__label_entrada = tk.Label(self.__frame, text='Letra a probar:')
        self.__label_entrada.grid(row=0, column=0, padx=2)
        self.__entrada = tk.Entry(self.__frame, width=2)
        self.__entrada.grid(row=0, column=1, padx=2)
        self.__probar = tk.Button(self.__frame, text='Probar', command=self.probar)
        self.__probar.grid(row=0, column=2, padx=2)
        self.__frame.pack()
        self.__adivinado = tk.Label(self, text=self.texto_adivinado())
        self.__adivinado.pack()
        self.__label_intentos = tk.Label(self, text=f'Te quedan {self.__errores} errores')
        self.__label_intentos.pack()
        self.__label_erroneas = tk.Label(self, text='Letras erróneas: ', width=60)
        self.__label_erroneas.pack()
        self.__salir = tk.Button(self, text='Salir', command=self.quit)
        self.__salir.pack()
        self.bind('<Return>', self.probar)
        self.bind('<Escape>', self.salir)

    def reiniciar(self):
        """Inicializa el juego."""
        with open('/usr/share/dict/words', encoding='utf-8') as f:
            palabras = f.readlines()
        quita_acentos = str.maketrans({
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
        })
        self.__palabra_a_adivinar = random.choice(palabras) \
            .strip() \
            .upper() \
            .translate(quita_acentos)
        self.__errores = NUM_ERRORES
        self.__adivinadas = set()
        self.__erroneas = set()

    def actualizar(self):
        """Actualiza los marcadores del turno actual."""
        self.__adivinado.config(text=self.texto_adivinado())
        self.__label_intentos.config(text=f'Te quedan {self.__errores} errores')
        erroneas = ' '.join(self.__erroneas)
        self.__label_erroneas.config(text=f'Letras erróneas: {erroneas}')

    def texto_adivinado(self) -> str:
        """Devuelve el texto que tiene que mostrarse, con letras y _."""
        return ' '.join(c if c in self.__adivinadas else '_' for c in self.__palabra_a_adivinar)

    def comprobar_acierto(self) -> bool:
        """Devuelve True si el jugador ha adivinado la palabra."""
        for c in self.__palabra_a_adivinar:
            if c not in self.__adivinadas:
                return False
        return True

    def probar(self, _ = None):
        """
        El turno del juego, donde se comprueba la entrada del juegador y
        se actualiza el estado del mismo.
        """
        c = self.__entrada.get().upper()
        self.__entrada.delete(0, tk.END)
        if c in self.__palabra_a_adivinar:
            self.__adivinadas.add(c)
            if self.comprobar_acierto():
                messagebox.showinfo(
                    '¡Ganó!',
                    f'''¡Enhorabuena!
                    La palabra era:
                    {self.__palabra_a_adivinar}'''
                    )
                self.reiniciar()
        else:
            self.__erroneas.add(c)
            self.__errores -= 1
            if self.__errores == 0:
                messagebox.showerror(
                    '¡Falló!',
                    f'''La palabra era:
                    {self.__palabra_a_adivinar}
                    ¡Más suerte la próxima vez!'''
                )
                self.reiniciar()
        self.actualizar()

    def salir(self, _):
        """El método que se ejecuta cuando el usuario pulsa la tecla <Esc>."""
        self.quit()


app = Aplicacion()
app.mainloop()
