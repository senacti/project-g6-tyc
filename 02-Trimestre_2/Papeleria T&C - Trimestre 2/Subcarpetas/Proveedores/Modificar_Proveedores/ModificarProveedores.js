
function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
    }

    var proveedores = [];

    function modificarTabla() {
        document.getElementById("formulario").style.display = "block";
    }

    function agregarProveedor() {
        var idProveedor = document.getElementById("idProveedor").value;
        var nombreEmpresa = document.getElementById("nombreEmpresa").value;
        var correo = document.getElementById("correo").value;
        var telefono = document.getElementById("telefono").value;
        var metodoPago = document.getElementById("metodoPago").value;

        var proveedor = {
            idProveedor: idProveedor,
            nombreEmpresa: nombreEmpresa,
            correo: correo,
            telefono: telefono,
            metodoPago: metodoPago,
        };

        proveedores.push(proveedor);
        mostrarProveedores();
        limpiarFormulario();
    }

    function mostrarProveedores() {
        var tabla = document.getElementById("proveedores").getElementsByTagName('tbody')[0];
        tabla.innerHTML = '';
        
        for (var i = 0; i < proveedores.length; i++) {
            var proveedor = proveedores[i];
            var fila = tabla.insertRow(tabla.rows.length);
            var celdas = [
                proveedor.idProveedor,
                proveedor.nombreEmpresa,
                proveedor.correo,
                proveedor.telefono,
                proveedor.metodoPago,
                '<button onclick="verDetalles(' + i + ')">Ver Detalles</button>',
            ];

            for (var j = 0; j < celdas.length; j++) {
                var celda = fila.insertCell(j);
                celda.innerHTML = celdas[j];
            }
        }
    }

    function limpiarFormulario() {
        document.getElementById("idProveedor").value = "";
        document.getElementById("nombreEmpresa").value = "";
        document.getElementById("correo").value = "";
        document.getElementById("telefono").value = "";
        document.getElementById("metodoPago").value = "";
        document.getElementById("formulario").style.display = "none";
    }

    function verDetalles(index) {
        var proveedor = proveedores[index];
        var detalleProveedor = document.getElementById("detalleProveedor");
        detalleProveedor.innerHTML = '<h3>Detalles del Proveedor</h3>' +
            '<p>ID del Proveedor: ' + proveedor.idProveedor + '</p>' +
            '<p>Nombre de la Empresa: ' + proveedor.nombreEmpresa + '</p>' +
            '<p>Correo: ' + proveedor.correo + '</p>' +
            '<p>Teléfono: ' + proveedor.telefono + '</p>' +
            '<p>Método de Pago: ' + proveedor.metodoPago + '</p>' +
            '<button class="GuardarProveedor" onclick="agregarPedido(' + index + ')">Agregar Pedido</button>';
    }

    function agregarPedido(index) {
        var proveedor = proveedores[index];
        var idPedido = prompt("ID del Pedido:");
        var nombreProducto = prompt("Nombre del Producto:");
        var cantidad = prompt("Cantidad:");
        var fechaCompra = prompt("Fecha de Compra:");
        var precioUnitario = prompt("Precio Unitario:");
        var precioTotal = prompt("Precio Total:");
        var fechaEntrega = prompt("Fecha de Entrega:");

        var pedido = {
            idPedido: idPedido,
            nombreProducto: nombreProducto,
            cantidad: cantidad,
            fechaCompra: fechaCompra,
            precioUnitario: precioUnitario,
            precioTotal: precioTotal,
            fechaEntrega: fechaEntrega,
        };

        if (!proveedor.pedidos) {
            proveedor.pedidos = [];
        }

        proveedor.pedidos.push(pedido);
        verDetalles(index); // Actualizar los detalles del proveedor
    }
    