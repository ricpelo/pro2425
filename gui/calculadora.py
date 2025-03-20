"""
Una calculadora sencilla.
"""

import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    """La calculadora."""

    def __init__(self):
        super().__init__()
        self.option_add("*Font", ("Arial", 18))

        self.op1_label = tk.Label(self, text="Primer operando:")
        self.op1_label.pack()
        self.op1 = tk.Entry(self)
        self.op1.pack()

        self.op2_label = tk.Label(self, text="Segundo operando:")
        self.op2_label.pack()
        self.op2 = tk.Entry(self)
        self.op2.pack()

        self.op_label = tk.Label(self, text="Operación (+, -, *, /):")
        self.op_label.pack()
        self.op = tk.Entry(self)
        self.op.pack()

        self.boton = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton.pack()

        self.bind("<Return>", self.calcular)
        self.bind("<KP_Enter>", self.calcular)

        self.res_label = tk.Label(self, text="Resultado:")
        self.res_label.pack()
        self.res = tk.Label(self, text="")
        self.res.pack()

        self.salir = tk.Button(self, text="Salir", command=self.quit)
        self.salir.pack()


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
            # if op == '+': res = op1 + op2
            # elif op == '-': res = op1 - op2
            # elif op == '*': res = op1 * op2
            # else: res = op1 / op2
            self.res.config(text=res)
        except ValueError:
            messagebox.showerror("Error", "El dato introducido es incorrecto.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")


app = Aplicacion()
app.mainloop()
