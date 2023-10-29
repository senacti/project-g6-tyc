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
    // Captura los valores de los campos de entrada
    var idProducto = document.getElementById('idProducto').value;
    var nombreInicial = document.getElementById('nombreInicial').value;
    var cambiarNombre = document.getElementById('cambiarNombre').value;
    var cantidad = document.getElementById('cantidad').value;
    var tamaño = document.getElementById('tamaño').value;
    var precio = document.getElementById('precio').value;

    // Obtén la tabla donde deseas agregar la fila
    var tabla = document.querySelector('.tabla-actualizar table');

    // Crea una nueva fila y las celdas
    var fila = tabla.insertRow(-1); // -1 para agregarla al final de la tabla
    var celdaId = fila.insertCell(0);
    var celdaNombre = fila.insertCell(1);
    var celdaCambiarNombre = fila.insertCell(2);
    var celdaCantidad = fila.insertCell(3);
    var celdaTamaño = fila.insertCell(4);
    var celdaPrecio = fila.insertCell(5);

    // Establece el contenido de las celdas con los valores capturados
    celdaId.textContent = idProducto;
    celdaNombre.textContent = nombreInicial;
    celdaCambiarNombre.textContent = cambiarNombre;
    celdaCantidad.textContent = cantidad;
    celdaTamaño.textContent = tamaño;
    celdaPrecio.textContent = precio;

    // Limpiar los campos de entrada
    document.getElementById('idProducto').value = '';
    document.getElementById('nombreInicial').value = '';
    document.getElementById('cambiarNombre').value = '';
    document.getElementById('cantidad').value = '';
    document.getElementById('tamaño').value = '';
    document.getElementById('precio').value = '';
}







