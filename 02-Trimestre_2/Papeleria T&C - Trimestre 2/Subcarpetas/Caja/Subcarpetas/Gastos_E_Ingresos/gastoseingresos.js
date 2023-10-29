function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}
document.addEventListener("DOMContentLoaded", function () {
    const tipo = document.getElementById("tipo");
    const monto = document.getElementById("monto");
    const registrar = document.getElementById("registrar");
    const listaTransacciones = document.getElementById("lista-transacciones");
    const total = document.getElementById("total");
    const limpiar = document.getElementById("limpiar");

    let transacciones = [];

    registrar.addEventListener("click", function () {
        const tipoTransaccion = tipo.value;
        const montoTransaccion = parseFloat(monto.value);

        if (isNaN(montoTransaccion) || montoTransaccion <= 0) {
            alert("Ingrese un monto válido.");
            return;
        }

        const transaccion = {
            tipo: tipoTransaccion,
            monto: montoTransaccion,
        };

        transacciones.push(transaccion);

        actualizarHistorial();
        calcularTotal();
        limpiarCampos();
    });

    limpiar.addEventListener("click", function () {
        // Limpiar el historial y el saldo
        transacciones = [];
        actualizarHistorial();
        calcularTotal();
        limpiarCampos();
    });

    function actualizarHistorial() {
        listaTransacciones.innerHTML = "";
        transacciones.forEach(function (transaccion, index) {
            const item = document.createElement("li");
            item.textContent = `${transaccion.tipo}: $${transaccion.monto.toFixed(2)}`;
            listaTransacciones.appendChild(item);
        });
    }

    function calcularTotal() {
        const totalIngresos = transacciones.reduce(function (total, transaccion) {
            return transaccion.tipo === "ingreso" ? total + transaccion.monto : total;
        }, 0);

        const totalGastos = transacciones.reduce(function (total, transaccion) {
            return transaccion.tipo === "gasto" ? total + transaccion.monto : total;
        }, 0);

        const saldoTotal = totalIngresos - totalGastos;

        total.textContent = saldoTotal.toFixed(2);
    }

    function limpiarCampos() {
        tipo.value = "ingreso";
        monto.value = "";
    }
});