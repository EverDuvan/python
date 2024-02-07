def alerta_pulsaciones(edad, pulsaciones, genero):
    # ppm *inadecuado*, *normal*, *bueno*, *excelente*
    rangos_hombres = {
        '20-29': [(86, float('inf')), (70, 84), (62, 68), (0, 60)],
        '30-39': [(86, float('inf')), (72, 84), (64, 70), (0, 62)],
        '40-49': [(90, float('inf')), (74, 88), (66, 72), (0, 64)],
        '50+':   [(90, float('inf')), (76, 88), (68 ,74), (0 ,66)]
    }

    rangos_mujeres = {
        '20-29': [(96,float('inf')),   (78 ,94) ,(72 ,76) ,(0 ,70)],
        '30-39': [(98,float('inf')) ,(80 ,96) ,(72 ,78) ,(0 ,70)],
        '40-49': [(100,float('inf')) ,(80 ,98) ,(74 ,78) ,(0 ,72)],
        '50+':   [(104,float('inf')),(84 ,102),(76 ,82),(0 ,74)]
    }

    categorias = ['INADECUADO', 'NORMAL', 'BUENO', 'EXCELENTE']

    if genero.upper() in ["HOMBRE", "H"]:
        rangos = rangos_hombres
    elif genero.upper() in ["MUJER", "M"]:
        rangos = rangos_mujeres
    else:
        return "Género no reconocido"

    for rango_edad in rangos:
        if '+' in rango_edad:
            if edad >= int(rango_edad.split('+')[0]):
                for i in range(4):
                    if pulsaciones >= rangos[rango_edad][i][0] and pulsaciones <= rangos[rango_edad][i][1]:
                        return print(categorias[i])
        else:
            inicio, fin = map(int, rango_edad.split('-'))
            if inicio <= edad <= fin:
                for i in range(4):
                    if pulsaciones >= rangos[rango_edad][i][0] and pulsaciones <= rangos[rango_edad][i][1]:
                        return print(categorias[i])

    return "Edad fuera de rango"

alerta_pulsaciones(35, 86, "m")