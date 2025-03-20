"""
Una calculadora sencilla.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion(tk.Tk):
    """La calculadora."""

    def __init__(self):
        super().__init__()
        self.option_add("*Font", ("Arial", 18))

        self.op1_label = tk.Label(self, text="Primer operando:")
        self.op1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.op1 = tk.Entry(self, width=10)
        self.op1.grid(row=0, column=1, padx=5)

        self.op2_label = tk.Label(self, text="Segundo operando:")
        self.op2_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.op2 = tk.Entry(self, width=10)
        self.op2.grid(row=1, column=1, padx=5)

        self.op_label = tk.Label(self, text="Operación:")
        self.op_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.op = ttk.Combobox(self, values=["+", "-", "*", "/"], state="readonly", width=3)
        self.op.grid(row=2, column=1, padx=6, sticky="w")
        self.op.current(0)

        # self.op = tk.Entry(self, width=10)
        # self.op.grid(row=2, column=1, padx=5)

        self.boton = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton.grid(row=3, column=0, columnspan=2, pady=10)

        self.bind("<Return>", self.calcular)
        self.bind("<KP_Enter>", self.calcular)

        self.res_label = tk.Label(self, text="Resultado:", fg="blue", font=("Monospace", 18))
        self.res_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.res = tk.Label(self, text="", fg="blue", font=("Monospace", 18))
        self.res.grid(row=4, column=1, sticky="w")

        self.salir = tk.Button(self, text="Salir", command=self.quit)
        self.salir.grid(row=5, column=0, columnspan=2, pady=10)


    def calcular(self, event=None) -> None:
        """Calcula el resultado."""
        try:
            # Validación de los datos de entrada:
            op1 = float(self.op1.get())
            op2 = float(self.op2.get())
            op = self.op.get()
            if op not in ('+', '-', '*', '/'):
                raise ValueError("Operación incorrecta.")
            # Calcular la operación:
            match op:
                case '+': res = op1 + op2
                case '-': res = op1 - op2
                case '*': res = op1 * op2
                case '/': res = op1 / op2
            self.res.config(text=res)
        except ValueError:
            messagebox.showerror("Error", "El dato introducido es incorrecto.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")


app = Aplicacion()
app.mainloop()
