import tkinter as tk

def bienvenida():
    nombre = entry_nombre.get()
    if nombre:
        label_mensaje.config(text=f"¡Bienvenido, {nombre}!")
    else:
        label_mensaje.config(text="Error")

root = tk.Tk()
root.title("Formulario de Usuario")
root.geometry("400x100")

label_instruccion = tk.Label(root, text="Ingrese su nombre, por favor:", font=("Courier", 14))
label_instruccion.pack(pady=10)

entry_nombre = tk.Entry(root, font=("Courier", 14))
entry_nombre.pack(pady=5)

boton_bienvenida = tk.Button(root, text="Entrar", font=("Courier", 12), command=bienvenida)
boton_bienvenida.pack(pady=10)

label_mensaje = tk.Label(root, text="", font=("Courier", 14), fg="black")
label_mensaje.pack(pady=10)

root.mainloop()
