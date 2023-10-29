function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

var tablaVisible = true; // Inicialmente, la tabla está visible

function agregarFila() {
    // Obtén los valores de ID del Producto y Nombre desde los input
    var idProducto = document.getElementById("idProducto").value;
    var nombre = document.getElementById("nombreInicial").value;

    // Limpia la tabla antes de agregar nuevos datos
    limpiarTabla();

    // Crea una nueva fila en la tabla
    var tabla = document.getElementById("tabla-inventario");
    var fila = tabla.insertRow();

    // Crea celdas para cada columna
    var celdaId = fila.insertCell(0);
    var celdaNombre = fila.insertCell(1);

    // Agrega los valores a las celdas
    celdaId.innerHTML = idProducto;
    celdaNombre.innerHTML = nombre;

    // Limpia los campos de entrada
    document.getElementById("idProducto").value = "";
    document.getElementById("nombreInicial").value = "";
}

function toggleTabla() {
    var tabla = document.querySelector("table");
    if (tablaVisible) {
        tabla.style.display = "none";
    } else {
        tabla.style.display = "table";
    }
    tablaVisible = !tablaVisible; // Cambia el estado de visibilidad
}

function limpiarTabla() {
    var tabla = document.getElementById("tabla-inventario");
    tabla.innerHTML = ""; // Limpia el contenido de la tabla
}