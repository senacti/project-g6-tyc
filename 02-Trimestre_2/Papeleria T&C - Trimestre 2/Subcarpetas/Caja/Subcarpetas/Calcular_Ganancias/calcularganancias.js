function mostraropciones() {
    var opciones = document.getElementById('opciones');
    opciones.style.display = opciones.style.display === 'block' ? 'none' : 'block';
    }
    document.getElementById("calculadora-form").addEventListener("submit", function (event) {
        event.preventDefault();
    
        // Obtener los valores de ingresos y gastos
        const ingresos = parseFloat(document.getElementById("ingresos").value);
        const gastos = parseFloat(document.getElementById("gastos").value);
    
        // Calcular ganancias
        const ganancias = ingresos - gastos;
    
        // Mostrar el resultado
        document.getElementById("ganancias").textContent = ganancias.toFixed(2);
    });