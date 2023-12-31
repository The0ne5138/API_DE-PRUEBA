window.addEventListener('load', function () {
    getProfile();
});

document.getElementById("logout").addEventListener("click", logout);
document.getElementById("volver").addEventListener("click", volver);

function getProfile() {
    const url = "http://127.0.0.1:5000/auth/profile";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {

                document.getElementById("nombre_usuario").innerText = data.nombre_usuario;
                document.getElementById("email").innerText = data.email;
                document.getElementById("nombre").innerText = data.nombre;
                document.getElementById("apellido").innerText = data.apellido;
                document.getElementById("clave").innerText = data.clave;
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "Ups ocurrio un error.";
    });
}

// Fucnion para volver a HOME
function volver() {
    
    window.location.href = "homeLog.html"; 
    //window.history.back();
}

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
