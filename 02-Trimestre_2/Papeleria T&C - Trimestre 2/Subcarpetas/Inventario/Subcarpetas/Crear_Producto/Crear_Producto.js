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
   function agregarFila() {
            // Obtener los valores de los campos de entrada
            var idProducto = document.getElementById('idProducto').value;
            var nombreInicial = document.getElementById('nombreInicial').value;
            var tamaño = document.getElementById('tamaño').value;
            var cantidad = document.getElementById('cantidad').value;
            var precio = document.getElementById('precio').value;

            // Obtener la tabla donde se mostrarán los valores
            var tabla = document.getElementById('tablaDatos');

            // Crear una nueva fila
            var fila = tabla.insertRow();

            // Crear celdas y asignar los valores
            var celdaId = fila.insertCell(0);
            celdaId.textContent = idProducto;
            var celdaNombreInicial = fila.insertCell(1);
            celdaNombreInicial.textContent = nombreInicial;
            var celdaTamaño = fila.insertCell(2);
            celdaTamaño.textContent = tamaño;
            var celdaCantidad = fila.insertCell(3);
            celdaCantidad.textContent = cantidad;
            var celdaPrecio = fila.insertCell(4);
            celdaPrecio.textContent = precio;

            // Limpiar los campos de entrada
            document.getElementById('idProducto').value = '';
            document.getElementById('nombreInicial').value = '';
            document.getElementById('tamaño').value = '';
            document.getElementById('cantidad').value = '';
            document.getElementById('precio').value = '';
        }