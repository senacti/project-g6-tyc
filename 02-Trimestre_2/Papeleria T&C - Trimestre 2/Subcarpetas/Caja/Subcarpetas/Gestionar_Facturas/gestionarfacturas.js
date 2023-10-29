function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
    }
    document.addEventListener("DOMContentLoaded", function () {
        const facturaForm = document.getElementById("factura-form");
        const listaFacturas = document.getElementById("lista-facturas");
        const indiceInput = document.getElementById("indice");
        const modificarFacturaBtn = document.getElementById("modificar-factura");
        const nuevaDescripcionInput = document.getElementById("nueva-descripcion");
        const nuevoMontoInput = document.getElementById("nuevo-monto");
    
        facturaForm.addEventListener("submit", function (event) {
            event.preventDefault();
    
            const cliente = document.getElementById("cliente").value;
            const descripcion = document.getElementById("descripcion").value;
            const monto = parseFloat(document.getElementById("monto").value);
    
            if (isNaN(monto) || monto <= 0) {
                alert("Ingrese un monto válido.");
                return;
            }
    
            const factura = {
                cliente: cliente,
                descripcion: descripcion,
                monto: monto.toFixed(2),
            };
    
            guardarFactura(factura);
            actualizarListaFacturas();
            limpiarCampos();
        });
    
        modificarFacturaBtn.addEventListener("click", function () {
            const indice = parseInt(indiceInput.value);
            if (isNaN(indice) || indice < 0) {
                alert("Ingrese un índice válido.");
                return;
            }
    
            const facturas = JSON.parse(localStorage.getItem("facturas")) || [];
    
            if (indice >= 0 && indice < facturas.length) {
                const nuevaDescripcion = nuevaDescripcionInput.value;
                const nuevoMonto = parseFloat(nuevoMontoInput.value);
    
                if (isNaN(nuevoMonto) || nuevoMonto <= 0) {
                    alert("Ingrese un monto válido.");
                    return;
                }
    
                facturas[indice].descripcion = nuevaDescripcion;
                facturas[indice].monto = nuevoMonto.toFixed(2);
                localStorage.setItem("facturas", JSON.stringify(facturas));
                actualizarListaFacturas();
            } else {
                alert("El índice de factura no existe.");
            }
        });
    
        function guardarFactura(factura) {
            let facturas = JSON.parse(localStorage.getItem("facturas")) || [];
            facturas.push(factura);
            localStorage.setItem("facturas", JSON.stringify(facturas));
        }
    
        function actualizarListaFacturas() {
            const facturas = JSON.parse(localStorage.getItem("facturas")) || [];
    
            listaFacturas.innerHTML = "";
            facturas.forEach(function (factura, index) {
                const item = document.createElement("li");
                item.textContent = `Cliente: ${factura.cliente}, Descripción: ${factura.descripcion}, Monto: $${factura.monto}`;
                listaFacturas.appendChild(item);
            });
        }
    
        function limpiarCampos() {
            document.getElementById("cliente").value = "";
            document.getElementById("descripcion").value = "";
            document.getElementById("monto").value = "";
            document.getElementById("nueva-descripcion").value = "";
            document.getElementById("nuevo-monto").value = "";
        }
    
        // Cargar facturas existentes al cargar la página
        actualizarListaFacturas();
    });