// Función para mostrar u ocultar las opciones en el menú
function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}

// Función para agregar un pedido
function agregarPedido() {

    var cliente = document.getElementById("clientePedido").value;
    var producto = document.getElementById("productoPedido").value;
    var cantidad = document.getElementById("cantidadPedido").value;
    var fecha = new Date().toLocaleDateString();


    if (cliente === "" || producto === "" || cantidad === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    var tabla = document.getElementById("tablaResultados").getElementsByTagName('tbody')[0];
    var fila = tabla.insertRow(tabla.rows.length);
    var celdas = [cliente, producto, cantidad, fecha];

    for (var i = 0; i < celdas.length; i++) {
        var celda = fila.insertCell(i);
        celda.innerHTML = celdas[i];
    }

    document.getElementById("clientePedido").value = "";
    document.getElementById("productoPedido").value = "";
    document.getElementById("cantidadPedido").value = "";
}

function generarInforme() {

}

function consultarMonto() {
    var cliente = document.getElementById("clienteMonto").value;
    
    
    var monto = 1000; 
    
    alert("El monto para el cliente " + cliente + " es: $" + monto);
}

// Función para consultar la historia de pedidos
function consultarHistoriaPedidos() {
    var cliente = document.getElementById("clienteHistoria").value;
    
    var historia = [
        { producto: "Producto A", cantidad: 2, fecha: "2023-09-10" },
        { producto: "Producto B", cantidad: 3, fecha: "2023-09-11" },
        { producto: "Producto C", cantidad: 1, fecha: "2023-09-12" }
    ];
    
    var mensaje = "Historia de pedidos para el cliente " + cliente + ":\n";
    for (var i = 0; i < historia.length; i++) {
        var pedido = historia[i];
        mensaje += "Producto: " + pedido.producto + ", Cantidad: " + pedido.cantidad + ", Fecha: " + pedido.fecha + "\n";
    }
    
    alert(mensaje);
}
