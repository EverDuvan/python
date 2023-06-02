import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login' )
ventana.resizable(False, False)

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

entrada1 = ttk.Entry(ventana, width=20)
entrada1.grid(row=0, column=1)

entrada2 = ttk.Entry(ventana, width=20)
entrada2.grid(row=1, column=1)

etiqueta1 = tk.Label(ventana, text='Usuario: ')
etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

etiqueta2 = tk.Label(ventana, text='Password: ')
etiqueta2.grid(row=1, column=0,  sticky=tk.E, padx=5, pady=5)

def enviar():
    mensaje1 = entrada1.get()
    mensaje2 = entrada2.get()
    if mensaje1:
        messagebox.showinfo('Datos Login', 'Usuario: ' + mensaje1 + '\nPassword: ' + mensaje2)

boton1 = ttk.Button(ventana, text='Login', command=enviar)
boton1.grid(row=3, column=1)


ventana.mainloop()
