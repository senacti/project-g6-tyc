
function mostraropciones() {
var opciones = document.getElementById('opciones');
opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener("DOMContentLoaded", function () {
    const formularioDevolucion = document.getElementById("formularioDevolucion");
    const listaDevoluciones = document.getElementById("listaDevoluciones");

    formularioDevolucion.addEventListener("submit", function (event) {
        event.preventDefault();

        const nombreProveedor = document.getElementById("nombreProveedor").value;
        const motivo = document.getElementById("motivo").value;
        const producto = document.getElementById("producto").value;
        const cantidad = document.getElementById("cantidad").value;

        // Crear una nueva fila en la tabla de devoluciones
        const newRow = listaDevoluciones.insertRow();
        const cellProveedor = newRow.insertCell(0);
        const cellMotivo = newRow.insertCell(1);
        const cellProducto = newRow.insertCell(2);
        const cellCantidad = newRow.insertCell(3);

        cellProveedor.textContent = nombreProveedor;
        cellMotivo.textContent = motivo;
        cellProducto.textContent = producto;
        cellCantidad.textContent = cantidad;

        // Limpiar el formulario
        formularioDevolucion.reset();
    });
});
