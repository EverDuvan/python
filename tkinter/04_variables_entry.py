import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
#ventana.iconbitmap('icono.ico')

# Creamos una caja de texto
entrada1_var = tk.StringVar(value='valor por defecto')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada1_var)
entrada1.grid(row=0, column=0)

#  Creamos una etiqueta(label)
etiqueta1 = ttk.Label(ventana, text='Escribe algo:')
etiqueta1.grid(row=1, column=0, columnspan=2) 

def enviar():
    # recuperamos la info a partir de la variable asociada a la caja de texto
    #boton1.config(text=entrada1_var.get())
    ### para modificar usamos la variable y no el componente 
    # entrada1_var.set('Nuevo valor')
    ### recuperar la informacion
    #print(entrada1_var.get())
    #print(entrada1.get())
    etiqueta1.config(text=entrada1_var.get())


# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
