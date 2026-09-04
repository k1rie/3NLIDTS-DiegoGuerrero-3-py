"""Actividad 03 - Conversor de temperatura entre Celsius, Fahrenheit y Kelvin."""

import tkinter as tk
from tkinter import messagebox

# 0 grados Celsius en kelvin. La conversion correcta usa 273.15, no 273.
CERO_ABSOLUTO = 273.15


def campo_de_entrada():
    """Devuelve la caja de texto de la escala marcada, o None si no hay ninguna."""
    return {
        "Celsius": tbCelsius,
        "Fahrenheit": tbFahrenheit,
        "Kelvin": tbKelvin,
    }.get(rbSeleccion.get())


def radioButton_Selected():
    """Deja habilitada solo la caja de la escala elegida."""
    entrada = campo_de_entrada()
    if entrada is None:
        return

    for caja in (tbCelsius, tbFahrenheit, tbKelvin):
        caja.config(state="normal" if caja is entrada else "disabled")
    entrada.focus()


def mostrar(caja, valor):
    """Escribe un resultado en la caja, borrando antes lo que hubiera."""
    caja.config(state="normal")
    caja.delete(0, tk.END)
    caja.insert(0, str(round(valor, 2)))


def btnCalcular_Click():
    """Convierte el valor capturado a las otras dos escalas."""
    entrada = campo_de_entrada()

    if entrada is None:
        messagebox.showwarning(
            "Temperatura Seleccionada",
            "Seleccione una temperatura de entrada (Kelvin/Fahrenheit/Celsius).")
        return

    try:
        valor = float(entrada.get().strip())
    except ValueError:
        messagebox.showerror(
            "Error", "Ingrese un numero valido en el campo habilitado.")
        entrada.focus()
        return

    # Todo se pasa primero a Celsius y desde ahi a las demas escalas
    if entrada is tbCelsius:
        celsius = valor
    elif entrada is tbFahrenheit:
        celsius = (valor - 32.0) * 5.0 / 9.0
    else:
        celsius = valor - CERO_ABSOLUTO

    mostrar(tbCelsius, celsius)
    mostrar(tbFahrenheit, celsius * 9.0 / 5.0 + 32.0)
    mostrar(tbKelvin, celsius + CERO_ABSOLUTO)


def btnLimpiar_Click():
    """Borra los tres campos y deja la pantalla lista para otro calculo."""
    for caja in (tbCelsius, tbFahrenheit, tbKelvin):
        caja.config(state="normal")
        caja.delete(0, tk.END)
    rbSeleccion.set("")
    tbCelsius.focus()


ventana = tk.Tk()
ventana.title("Actividad 03 - Conversor Temperatura")
ventana.geometry("450x400")
ventana.resizable(False, False)
ventana.configure(bg="white")
rbSeleccion = tk.StringVar(value="")

tk.Label(ventana, text="Temp. en Celsius:", font=("Segoe UI", 12, "bold"), bg="white").pack()
tbCelsius = tk.Entry(ventana, width=18, justify="center")
tbCelsius.pack()

tk.Label(ventana, text="Temp. en Fahrenheit:", font=("Segoe UI", 12, "bold"), bg="white").pack()
tbFahrenheit = tk.Entry(ventana, width=18, justify="center")
tbFahrenheit.pack()

tk.Label(ventana, text="Temp. en Kelvin:", font=("Segoe UI", 12, "bold"), bg="white").pack()
tbKelvin = tk.Entry(ventana, width=18, justify="center")
tbKelvin.pack()

gb = tk.LabelFrame(ventana, text="Seleccione Temperatura de Entrada:", padx=12, pady=12, bg="white")
gb.pack()
rbCelsius = tk.Radiobutton(gb, text="Celsius", value="Celsius", variable=rbSeleccion,
                           command=radioButton_Selected, bg="white")
rbCelsius.grid(row=0, column=0)
rbFahrenheit = tk.Radiobutton(gb, text="Fahrenheit", value="Fahrenheit", variable=rbSeleccion,
                              command=radioButton_Selected, bg="white")
rbFahrenheit.grid(row=0, column=1)
rbKelvin = tk.Radiobutton(gb, text="Kelvin", value="Kelvin", variable=rbSeleccion,
                          command=radioButton_Selected, bg="white")
rbKelvin.grid(row=0, column=2)

btnCalcular = tk.Button(ventana, text="Calcular", width=12, bg="#7CFCe0",
                        command=btnCalcular_Click, padx=6, pady=5)
btnCalcular.pack()
btnLimpiar = tk.Button(ventana, text="Limpiar", width=12, bg="#FF3030", fg="white",
                       command=btnLimpiar_Click, padx=6, pady=5)
btnLimpiar.pack()

# Enter tambien calcula, sin tener que ir al boton con el mouse
ventana.bind("<Return>", lambda evento: btnCalcular_Click())

ventana.mainloop()