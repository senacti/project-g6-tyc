function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

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

const imagenes = document.querySelectorAll('.ZoomClick');

imagenes.forEach(imagen => {
    imagen.addEventListener('mouseover', () => {
        imagenes.forEach(imagen => imagen.classList.add('hover'));
    });

    imagen.addEventListener('mouseout', () => {
        imagenes.forEach(imagen => imagen.classList.remove('hover'));
    });
});