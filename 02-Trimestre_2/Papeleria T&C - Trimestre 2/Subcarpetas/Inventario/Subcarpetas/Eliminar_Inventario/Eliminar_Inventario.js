function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}
function toggleVisibility() {
    var contenido = document.getElementById('contenido');
    if (contenido.style.display === 'none' || contenido.style.display === '') {
        contenido.style.display = 'block';
    } else {
        contenido.style.display = 'none';
    }
}   
function toggleVisibility() {
    var contenido = document.getElementById('contenido');
    var tabla = document.getElementById('tabla');
    if (contenido.style.display === 'none' || contenido.style.display === '') {
        contenido.style.display = 'block';
        tabla.style.display = 'none';
    } else {
        contenido.style.display = 'none';
        tabla.style.display = 'block';
    }
}
function toggleVisibility() {
    var contenido = document.getElementById('contenido');
    if (contenido.style.display === 'none' || contenido.style.display === '') {
        contenido.style.display = 'block';
    } else {
        contenido.style.display = 'none';
    }
}
function agregarFila() {
    // Obtener los valores de los campos de entrada
    var idProducto = document.getElementById('idProducto').value;
    var nombreProducto = document.getElementById('nombreProducto').value;

    // Obtener la tabla donde se mostrarán los valores
    var tabla = document.getElementById('tablaDatos');

    // Crear una nueva fila
    var fila = tabla.insertRow();

    // Crear celdas y asignar los valores
    var celdaId = fila.insertCell(0);
    celdaId.textContent = idProducto;
    var celdaNombre = fila.insertCell(1);
    celdaNombre.textContent = nombreProducto;

    // Limpiar los campos de entrada
    document.getElementById('idProducto').value = '';
    document.getElementById('nombreProducto').value = '';
}