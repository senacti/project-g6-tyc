//Contenedores de pestañas

document.addEventListener('DOMContentLoaded', function() {
    const showLinks = document.querySelectorAll('.show-container');
    const containers = document.querySelectorAll('.Nav-contenedor');

    showLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            const targetContainerId = this.getAttribute('data-target');

            containers.forEach(container => {
                container.style.display = 'none';
            });

            const targetContainer = document.getElementById(targetContainerId);
            if (targetContainer) {
                targetContainer.style.display = 'block';
            }
        });
    });
});

//Color opcion elegida pestañas


document.addEventListener('DOMContentLoaded', function() {
    const showLinks = document.querySelectorAll('.show-container');

    showLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();


            showLinks.forEach(otherLink => {
                otherLink.classList.remove('seleccionado');
            });


            this.classList.add('seleccionado');

        });
    });
});


function iniciarSesion() {
    var usuario = document.getElementById("usuario").value;
    var contrasena = document.getElementById("contrasena").value;

    // Validar las credenciales del administrador
    if (usuario === "admin" && contrasena === "admin123") {
        window.location.href = "Pantalla_De_Carga/PantallaDeCarga.html";
        return;
    }

    // Validar las credenciales del empleado
    if (usuario === "empleado" && contrasena === "empleado123") {
        window.location.href = "Pantalla_De_Carga/PantallaDeCarga.html";
        return;
    }

    // Si las credenciales son incorrectas, mostrar un mensaje de error
    alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
}

//Boton para ver contraseña 

function mostrarOcultarContrasena() {
    const contrasenaInput = document.getElementById("contrasena");
    const iconoMostrar = document.getElementById("iconoMostrar");

    if (contrasenaInput.type === "password") {
        contrasenaInput.type = "text";
        iconoMostrar.classList.remove("fa-eye");
        iconoMostrar.classList.add("fa-eye-slash");
    } else {
        contrasenaInput.type = "password";
        iconoMostrar.classList.remove("fa-eye-slash");
        iconoMostrar.classList.add("fa-eye");
    }
}

//CONTACTO

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

        mensajeCopiado.style.display = "block";
        setTimeout(function() {
            mensajeCopiado.style.display = "none";
        }, 2000); 
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); 

        // Muestra un mensaje en el elemento con id "mensaje"
        var mensajeElement = document.getElementById("mensaje");
        mensajeElement.textContent = "Información enviada.";

        // Limpia el formulario o realiza otras acciones necesarias
        form.reset();
    });
});


