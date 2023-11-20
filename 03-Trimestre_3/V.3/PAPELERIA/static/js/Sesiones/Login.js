document.addEventListener("DOMContentLoaded", function () {
    const saludoElement = document.getElementById("saludo");
    const horaActual = new Date().getHours();

    if (horaActual >= 6 && horaActual < 12) {
        saludoElement.textContent = "BUENOS DIAS";
    } else if (horaActual >= 12 && horaActual < 18) {
        saludoElement.textContent = "BUENAS TARDES";
    } else {
        saludoElement.textContent = "BUENAS NOCHES";
    }

    const saludoPrinElement = document.getElementById("saludoPrin");

    if (horaActual >= 6 && horaActual < 12) {
        saludoPrinElement.textContent = "BUENOS DIAS";
    } else if (horaActual >= 12 && horaActual < 18) {
        saludoPrinElement.textContent = "BUENAS TARDES";
    } else {
        saludoPrinElement.textContent = "BUENAS NOCHES";
    }

    const formElement = document.getElementById("loginForm");

    formElement.addEventListener("submit", function (event) {
        event.preventDefault();  // Evita la presentación predeterminada del formulario

        // Aquí puedes agregar tu lógica de manejo del formulario, como la llamada a la API

    });
});


