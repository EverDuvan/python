def saludar(saludo, *nombres, hora, despedida='Adiós...'):

    for nombre in nombres:
        print(f'{saludo}, {nombre}')

    print(f'Esta es la hora: {hora}')
    print(despedida)

saludar('Buenos días', 'Carlos', 'Manuel', hora='09:15am')
print()
saludar('Buenas noches', 'Roberto', 'Fernando', hora='23:30', despedida='Hasta mañana')