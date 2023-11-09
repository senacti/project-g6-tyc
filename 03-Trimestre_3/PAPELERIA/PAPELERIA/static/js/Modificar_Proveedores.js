document.addEventListener("DOMContentLoaded", function() {
    const saludoElement = document.getElementById("saludo");
    const horaActual = new Date().getHours();

    if (horaActual >= 6 && horaActual < 12) {
        saludoElement.textContent = "BUENOS DIAS";
    } else if (horaActual >= 12 && horaActual < 18) {
        saludoElement.textContent = "BUENAS TARDES";
    } else {
        saludoElement.textContent = "BUENAS NOCHES";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const saludoElement = document.getElementById("saludoPrin");
    const horaActual = new Date().getHours();

    if (horaActual >= 6 && horaActual < 12) {
        saludoElement.textContent = "BUENOS DIAS";
    } else if (horaActual >= 12 && horaActual < 18) {
        saludoElement.textContent = "BUENAS TARDES";
    } else {
        saludoElement.textContent = "BUENAS NOCHES";
    }
});
