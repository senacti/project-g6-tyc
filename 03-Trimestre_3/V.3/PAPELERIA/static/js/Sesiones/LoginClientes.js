document.addEventListener("DOMContentLoaded", function () {

    const formElement = document.getElementById("loginForm");

    formElement.addEventListener("submit", function (event) {
        event.preventDefault();  // Evita la presentación predeterminada del formulario

        // Aquí puedes agregar tu lógica de manejo del formulario, como la llamada a la API
    var loginUrl = "{% url 'Login' %}";
    });
});

