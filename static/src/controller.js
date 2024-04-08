function mostrarParticipantes(params) {
    var navbar = document.getElementById("participantes");
    if (navbar.style.left === "-100%") {
        navbar.style.left = "0";
    } else {
        navbar.style.left = "-100%";
    }
}

function convertir(){
    var entrada = document.getElementById('texto-entrada').value;

    document.getElementById('texto-salida').innerHTML = 'Hola ' + entrada;
}