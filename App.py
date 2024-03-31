import numpy as np
import tkinter as tk
from tkinter import ttk
from sympy import lambdify, symbols
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0

    steps = []  # Lista para almacenar los pasos utilizados para resolver la ecuación

    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])
        x[i+1] = x[i] + h

        step = f"Paso {i+1}: x = {x[i]:.2f}, y = {y[i]:.4f}"
        steps.append(step)

    return x, y, steps

def plot_graph():
    equation = equation_entry.get()  # Obtener la ecuación ingresada por el usuario
    x0 = float(x0_entry.get())  # Obtener el valor inicial de x ingresado por el usuario
    y0 = float(y0_entry.get())  # Obtener el valor inicial de y ingresado por el usuario
    h = float(h_entry.get())    # Obtener el tamaño del paso ingresado por el usuario
    n = int(n_entry.get())      # Obtener el número de iteraciones ingresado por el usuario

    try:
        x, y = symbols('x y')
        f = lambdify((x, y), equation)  # Convertir la ecuación en una función lambda

        x_vals, y_vals, steps = euler_method(f, x0, y0, h, n)

        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica de la Ecuación Diferencial')
        plt.grid(True)
        plt.show()

        # Crear una nueva ventana para mostrar los pasos utilizados
        steps_window = tk.Toplevel(root)
        steps_window.title("Pasos para Resolver la Ecuación Diferencial")

        steps_text = tk.Text(steps_window, height=10, width=40, bd=0, font=('Arial', 12))
        steps_text.pack(pady=20)
        steps_text.insert(tk.END, "Pasos utilizados para resolver la ecuación:\n")
        for step in steps:
            steps_text.insert(tk.END, f"{step}\n")

    except:
        error_label.config(text="¡Ecuación inválida! Inténtalo de nuevo.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ingresar Ecuación Diferencial")

# Estilo para los elementos de la interfaz
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))

# Etiqueta y entrada de texto para ingresar la ecuación
equation_label = ttk.Label(root, text="Ecuación Diferencial:")
equation_label.pack(pady=10)

equation_entry = ttk.Entry(root, font=('Arial', 12))
equation_entry.pack()

# Etiquetas y entradas de texto para los valores iniciales, tamaño del paso y número de iteraciones
x0_label = ttk.Label(root, text="Valor Inicial de x:")
x0_label.pack(pady=5)

x0_entry = ttk.Entry(root, font=('Arial', 12))
x0_entry.pack()

y0_label = ttk.Label(root, text="Valor Inicial de y:")
y0_label.pack(pady=5)

y0_entry = ttk.Entry(root, font=('Arial', 12))
y0_entry.pack()

h_label = ttk.Label(root, text="Tamaño del Paso:")
h_label.pack(pady=5)

h_entry = ttk.Entry(root, font=('Arial', 12))
h_entry.pack()

n_label = ttk.Label(root, text="Número de Iteraciones:")
n_label.pack(pady=5)

n_entry = ttk.Entry(root, font=('Arial', 12))
n_entry.pack()

# Botón para resolver la ecuación
solve_button = ttk.Button(root, text="Resolver", command=plot_graph)
solve_button.pack(pady=10)

# Etiqueta para mostrar errores
error_label = ttk.Label(root, text="", foreground='red')
error_label.pack(pady=10)

# Mostrar la ventana principal
root.mainloop()