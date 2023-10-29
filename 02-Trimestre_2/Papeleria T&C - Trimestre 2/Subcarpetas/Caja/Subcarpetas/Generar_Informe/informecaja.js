function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
}
let totalIngresos = 0.00;
let totalGastos = 0.00;

function registrarTransaccion() {
    const ingresos = parseFloat(document.getElementById("ingresos").value) || 0;
    const gastos = parseFloat(document.getElementById("gastos").value) || 0;

    totalIngresos += ingresos;
    totalGastos += gastos;

    actualizarInformeCaja();
    limpiarCampos();
}

function cerrarCaja() {
    const totalEfectivo = totalIngresos - totalGastos;
    alert(`Caja cerrada.\nTotal Efectivo: $${totalEfectivo.toFixed(2)}`);
}

function actualizarInformeCaja() {
    document.getElementById("total-ingresos").textContent = totalIngresos.toFixed(2);
    document.getElementById("total-gastos").textContent = totalGastos.toFixed(2);

    const totalEfectivo = totalIngresos - totalGastos;
    document.getElementById("total-efectivo").textContent = totalEfectivo.toFixed(2);
}

function limpiarCampos() {
    document.getElementById("ingresos").value = "";
    document.getElementById("gastos").value = "";
}
