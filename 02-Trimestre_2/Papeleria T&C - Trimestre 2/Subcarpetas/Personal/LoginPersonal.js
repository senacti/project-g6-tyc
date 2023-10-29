function validarLogin() {
    var rolSeleccionado = document.getElementById("rol").value;
    var usuario = document.getElementById("usuario").value;
    var contrasena = document.getElementById("contrasena").value;

    // Verificar rol y las credenciales

    if (rolSeleccionado === "administrador") {

        var usuarioAdmin = "admin";
        var contrasenaAdmin = "admin123";

        if (usuario === usuarioAdmin && contrasena === contrasenaAdmin) {

            window.location.href = "Personal_Admin/PersonalAdmin.html";
        } else {

            alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
        }
    } else if (rolSeleccionado === "empleado") {

        var usuarioEmpleado = "empleado";
        var contrasenaEmpleado = "empleado123";

        if (usuario === usuarioEmpleado && contrasena === contrasenaEmpleado) {

            window.location.href = "Personal_Empleado/PersonalEmpleados.html";
        } else {

            alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
        }
    }

    return false;
}

function mostrarMensajeError() {
    var mensajeError = document.getElementById("mensajeError");
    mensajeError.style.display = "block";
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
