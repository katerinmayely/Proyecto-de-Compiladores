function mostrarParticipantes(params) {
    var navbar = document.getElementById("participantes");
    if (navbar.style.left === "-100%") {
        navbar.style.left = "0";
    } else {
        navbar.style.left = "-100%";
    }
}

function convertir(){
    console.log('Tamos aqui')
    var entrada = document.getElementById('texto-entrada').value;
    console.log(entrada)

    if(entrada == ""){
        alert('La entrada no puede estar vacía.')
        return
    }

    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
      fetch(`http://127.0.0.1:5000/analizando/${entrada}`, requestOptions)
        .then(response => response.text())
        .then(result => {
            console.log(result);
            mostrarSalida(result);
        })
        .catch(error => {
            alert('Entrada Inválida.')
        });
}

function mostrarSalida(salida){
    try {
        document.getElementById('texto-salida').innerHTML = salida; 
    } catch (error) {
        alert('Entrada Inválida.')
    }
    
}