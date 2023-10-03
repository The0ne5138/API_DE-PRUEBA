
// FUNCION PARA REDIRIGIR AL PERFIL
//document.getElementById("perfilUsuario-btn").addEventListener("click", perfil);
//window.addEventListener('loadPerfil', function () {
//    getProfile();
//});

//function perfil() {
    // Redirige a la otra página
//    window.location.href = "profile.html ";
//};

document.getElementById("logout-btn").addEventListener("click", logout);














//******************************************************* */

// Func carga canales cuando se selecciona un servidor
function cargarCanales(id_servidor) {
    
}

// Func cargar mensajes cuando se selecciona un canal
function cargarMensajes(id_canal) {
    
}

// Event listener para cuando se selecciona un servidor
document.querySelector(".column.servers").addEventListener("click", function(event) {
    if (event.target.classList.contains("server")) {
        const servidorId = event.target.dataset.servidorId;
        cargarCanales(id_servidor);
    }
});

// Event listener para cuando se selecciona un canal
document.querySelector(".column.channels").addEventListener("click", function(event) {
    if (event.target.classList.contains("channel")) {
        const canalId = event.target.dataset.canalId;
        cargarMensajes(id_canal);
    }
});







// FUNCION para cerrar sesion.
function logout() {
    const url = "http://127.0.0.1:5000/auth/logout";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                window.location.href = "login.html";
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}






