import tkinter as tk
from tkinter import messagebox

def radioButton_Selected():
    sel = rbSeleccion.get()

    if sel == "Celsius":
        tbCelsius.config(state="normal")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="disabled")
    elif sel == "Kelvin":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="normal")
    elif sel == "Fahrenheit":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="normal")
        tbKelvin.config(state="disabled")

def btnCalcular_Click():
    try:
        if rbSeleccion.get() == "Celsius":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            celsius = float(tbCelsius.get())
            print(celsius)
            fahrenheit = (celsius * 9.0 / 5.0) + 32.0
            print(fahrenheit)
            ##tbFahrenheit.insert(0, f"{fahrenheintt :. 2f}")
            tbFahrenheit.insert(0,str(round(fahrenheit, 2)))
            kelvin = celsius + 273.0
            print(kelvin)
            ##tbKelvin.insert(0, f"{kelvin :. 2f}")
            tbKelvin.insert(0,str(round(kelvin, 2)))

        elif rbSeleccion.get() == "Kelvin":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            kelvin = float(tbKelvin.get())
            celsius = kelvin - 273.0
            tbCelsius.insert(0,str(round(celsius,2)))
            print(celsius)
            fahrenheit = (celsius * 9.0 / 5.0) + 32.0
            print(fahrenheit)
            tbFahrenheit.insert(0,str(round(fahrenheit, 2)))

        elif rbSeleccion.get() == "Fahrenheit":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            fahrenheit = float(tbFahrenheit.get())
            print(fahrenheit)
            celsius = (fahrenheit - 32.0) * 5.0 / 9.0
            print(celsius)
            kelvin = celsius + 273.0
            print(kelvin)
            tbCelsius.insert(0,str(round(celsius, 2)))
            tbKelvin.insert(0,str(round(kelvin,2)))

        else:
            messagebox.showwarning(
            "Temperatura Seleccionada",
            "Seleccione una temperatura de entrada (Kelvin/Fahrenheit/Celsius)."
            )

    except ValueError:
        messagebox. showerror("Error", "Ingrese un numero valido en el campo habilitado.")

def btnLimpiar_Click():
    tbKelvin.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)

    tbCelsius.config(state="normal")
    tbFahrenheit.config(state="normal")
    tbKelvin.config(state="normal")
    rbSeleccion.set("")

ventana = tk.Tk()
ventana.title("Actividad 03 - Conversor Temperatura")
ventana.geometry("450x400")
ventana.configure(bg="white")
rbSeleccion = tk.StringVar(value="")

tk.Label(ventana, text="Temp. en Celsius:", font=("Segoe UI", 12, "bold")).pack()
tbCelsius = tk.Entry(ventana, width=18, justify="center")
tbCelsius.pack()
tk.Label(ventana, text="Temp. en Fahrenheit:", font=("Segoe UI", 12, "bold")).pack()
tbFahrenheit = tk.Entry(ventana, width=18, justify="center")
tbFahrenheit.pack()
tk.Label(ventana, text="Temp. en Kelvin:", font=("Segoe UI", 12, "bold")).pack()
tbKelvin = tk.Entry(ventana, width=18, justify="center")
tbKelvin.pack()
gb = tk.LabelFrame(ventana, text="Seleccione Temperatura de Entrada:", padx=12, pady=12)
gb.pack()
rbCelsius = tk.Radiobutton(gb, text="Celsius", value="Celsius", variable=rbSeleccion, command=radioButton_Selected)
rbCelsius.grid(row=0, column=0)
rbFahrenheit = tk.Radiobutton(gb, text="Fahrenheit", value="Fahrenheit", variable=rbSeleccion, command=radioButton_Selected)
rbFahrenheit.grid(row=0, column=1)
rbKelvin = tk.Radiobutton(gb, text="Kelvin", value="Kelvin", variable=rbSeleccion, command=radioButton_Selected)
rbKelvin.grid(row=0, column=2)
btnCalcular = tk.Button(ventana, text="Calcular", width=12, bg="#7CFCe0", command=btnCalcular_Click, padx=6, pady=5)
btnCalcular.pack()
btnLimpiar = tk.Button(ventana, text="Limpiar", width=12, bg="#FF3030", fg="white", command=btnLimpiar_Click, padx=6, pady=5)
btnLimpiar.pack()
tbCelsius.config(state="normal")
tbFahrenheit.config(state="normal")
tbKelvin.config(state="normal")
ventana.mainloop()