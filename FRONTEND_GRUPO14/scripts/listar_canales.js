function cargaServidores() {
    const data = {
        nombre_usuario: document.getElementById("nombre_usuario").value,
        clave: document.getElementById("clave").value,
    };

    fetch("http://127.0.0.1:5000/auth/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            // Redirect to profile page if login is successful
            return response.json().then(data => {
                window.location.href = "homeLog.html";
                //window.location.href = "profile.html";
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "Upss A ocurrido un error.";
    });
}



const buttonsDivCanales = document.getElementById("listarCanales");

const jsonResponseCanales = {
    Canal1: "Contenido del canal 1",
    Canal2: "Contenido del Canal 2",
    Canal3: "Contenido del Canal 3",
    Canal4: "Contenido del Canal 4",
    Canal5: "Contenido del Canal 5",
    Canal6: "Contenido del Canal 6",
    Canal7: "Contenido del Canal 7"
};

// Función para lanzar un evento personalizado "evento"
function lanzarEvento(valor) {
    const evento = new Event("evento");     // llamado a la API para obtener lista de Canales de el Servidor seleccionado.
    evento.valor = valor;
    document.dispatchEvent(evento);
}



// Crear botones dinámicamente con el valor JSON
for (const key in jsonResponseCanales) {
    if (jsonResponseCanales.hasOwnProperty(key)) {
        const valor = jsonResponseCanales[key];
        const button = document.createElement("button");
        button.textContent = valor;
        button.addEventListener("click", () => {
            lanzarEvento(valor);
        });
        buttonsDivCanales.appendChild(button);
    }
}

// Agregar un oyente de eventos para el evento personalizado "evento"
document.addEventListener("evento", (e) => {
    console.log(`Evento personalizado 'evento' ha sido lanzado con el valor: ${e.valor}`);
});