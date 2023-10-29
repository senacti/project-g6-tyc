function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener("DOMContentLoaded", function() {
    var textosACopiar = document.querySelectorAll(".copiar-texto");
    var mensajeCopiado = document.getElementById("mensaje-copiado");

    textosACopiar.forEach(function(texto) {
        texto.style.cursor = "pointer";
        texto.addEventListener("click", function() {
            copiarAlPortapapeles(this.getAttribute("data-texto"));
        });
    });

    function copiarAlPortapapeles(texto) {
        var elementoTemporario = document.createElement("textarea");
        elementoTemporario.value = texto;
        document.body.appendChild(elementoTemporario);
        elementoTemporario.select();
        document.execCommand("copy");
        document.body.removeChild(elementoTemporario);

        // Mostrar el mensaje en la parte inferior central de la pantalla
        mensajeCopiado.style.display = "block";
        setTimeout(function() {
            mensajeCopiado.style.display = "none";
        }, 2000); // Ocultar el mensaje después de 2 segundos (puedes ajustar el tiempo)
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto
        // Aquí puedes realizar cualquier otra operación que necesites con los datos del formulario

        // Muestra un mensaje en el elemento con id "mensaje"
        var mensajeElement = document.getElementById("mensaje");
        mensajeElement.textContent = "Información enviada.";

        // Limpia el formulario o realiza otras acciones necesarias
        form.reset();
    });
});

function regresar() {
    window.history.back();
}