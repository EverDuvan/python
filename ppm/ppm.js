function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

let intervalId;

function startGeneratingNumbers(intervalInSeconds, durationInSeconds, callback) {
    const interval = intervalInSeconds * 1000;
    const duration = durationInSeconds * 1000;

    intervalId = setInterval(() => {
        const randomNumber = getRandomInt(251);
        callback(randomNumber); // Llama a la función callback con el número aleatorio
    }, interval);

    setTimeout(() => {
        clearInterval(intervalId);
    }, duration);
}


function alerta_pulsaciones(edad, pulsaciones, genero) {
    // ppm *inadecuado*, *normal*, *bueno*, *excelente*
    const rangos_hombres = {
        '20-29': [[86, Infinity], [70, 84], [62, 68], [0, 60]],
        '30-39': [[86, Infinity], [72, 84], [64, 70], [0, 62]],
        '40-49': [[90, Infinity], [74, 88], [66, 72], [0, 64]],
        '50+': [[90, Infinity], [76, 88], [68, 74], [0, 66]]
    };

    const rangos_mujeres = {
        '20-29': [[96, Infinity], [78, 94], [72, 76], [0, 70]],
        '30-39': [[98, Infinity], [80, 96], [72, 78], [0, 70]],
        '40-49': [[100, Infinity], [80, 98], [74, 78], [0, 72]],
        '50+': [[104, Infinity], [84, 102], [76, 82], [0, 74]]
    };

    const categorias = ['INADECUADO', 'NORMAL', 'BUENO', 'EXCELENTE'];

    if (["HOMBRE", "H"].includes(genero.toUpperCase())) {
        var rangos = rangos_hombres;
    } else if (["MUJER", "M"].includes(genero.toUpperCase())) {
        var rangos = rangos_mujeres;
    } else {
        return "Género no reconocido";
    }

    for (const rango_edad in rangos) {
        if (rango_edad.includes('+')) {
            if (edad >= parseInt(rango_edad.split('+')[0])) {
                for (let i = 0; i < 4; i++) {
                    if (pulsaciones >= rangos[rango_edad][i][0] && pulsaciones <= rangos[rango_edad][i][1]) {
                        return categorias[i];
                    }
                }
            }
        } else {
            const [inicio, fin] = rango_edad.split('-').map(Number);
            if (edad >= inicio && edad <= fin) {
                for (let i = 0; i < 4; i++) {
                    if (pulsaciones >= rangos[rango_edad][i][0] && pulsaciones <= rangos[rango_edad][i][1]) {
                        return categorias[i];
                    }
                }
            }
        }
    }

    return "Edad fuera de rango";
}

// Llama a la función para comenzar a generar números aleatorios
// Cada 3 segundos y durante 12 segundos
startGeneratingNumbers(3, 18, (ppm_values) => {
    const categoria = alerta_pulsaciones(70, ppm_values, "H"); // Usa ppm_values como entrada para alerta_pulsaciones
    console.log(`ppm: ${ppm_values}, Categoría: ${categoria}`); // Imprime las pulsaciones y la categoría
});