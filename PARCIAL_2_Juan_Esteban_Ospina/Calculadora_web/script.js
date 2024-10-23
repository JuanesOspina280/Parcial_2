function potencia() {
    realizarOperacion("potencia");
}

function realizarOperacion(operacion) {
    var num1 = parseFloat(document.getElementById("numero1").value);
    var num2 = parseFloat(document.getElementById("numero2").value);
    var resultado;

    switch (operacion) {
        case "suma":
            resultado = num1 + num2;
            break;
        case "resta":
            resultado = num1 - num2;
            break;
        case "multiplicacion":
            resultado = num1 * num2;
            break;
        case "division":
            if (num2 !== 0) {
                resultado = num1 / num2;
            } else {
                resultado = "Error: No se puede dividir por cero";
            }
            break;
        case "potencia":  // Completa la operación de potencia
            resultado = Math.pow(num1, num2);
            break;
        default:
            resultado = "Operación no válida";
    }
  document.getElementById("resultado").innerText = resultado;
}














/*
function realizarOperacion(operacion) {
    const num1 = parseFloat(document.getElementById('numero1').value);
    const num2 = parseFloat(document.getElementById('numero2').value);
    let resultado;

    // Validar entrada
    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('resultado').innerText = 'Por favor, ingresa ambos números.';
        return;
    }

    switch (operacion) {
        case 'suma':
            resultado = num1 + num2;
            break;
        case 'resta':
            resultado = num1 - num2;
            break;
        case 'multiplicacion':
            resultado = num1 * num2;
            break;
        case 'division':
            if (num2 === 0) {
                document.getElementById('resultado').innerText = 'No se puede dividir por cero.';
                return;
            }
            resultado = num1 / num2;
            break;
        case 'modulo':
            resultado = num1 % num2;
            break;
        case 'potencia':
            resultado = Math.pow(num1, num2); 
            break;
        default:
            resultado = 'Operación no válida.';
    }

    document.getElementById('resultado').innerText = `Resultado: ${resultado}`;
}
*/