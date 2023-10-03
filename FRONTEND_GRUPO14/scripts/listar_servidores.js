
const buttonsDivServidores = document.getElementById("listarServidores");

const jsonResponse = {
    Server1: "Nombre del Server 1",
    Server2: "Nombre del Server 2",
    Server3: "Nombre del Server 3",
    Server4: "Nombre del Server 4",
    Server5: "Nombre del Server 5",
    Server6: "Nombre del Server 6",
    Server7: "Nombre del Server 7"
};

// Función para lanzar un evento personalizado "evento"
function lanzarEvento(valor) {
    const evento = new Event("evento");  // llamado a la API para obtener lista de servidores de el usuario logueado.
    evento.valor = valor;
    document.dispatchEvent(evento);
}

// Crear botones dinámicamente con el valor JSON
for (const key in jsonResponse) {
    if (jsonResponse.hasOwnProperty(key)) {
        const valor = jsonResponse[key];
        const button = document.createElement("button");
        button.textContent = valor;
        button.addEventListener("click", () => {
            lanzarEvento(valor);
        });
        buttonsDivServidores.appendChild(button);
    }
}

// Agregar un oyente de eventos para el evento personalizado "evento"
document.addEventListener("evento", (e) => {
    console.log(`Evento personalizado 'evento' ha sido lanzado con el valor: ${e.valor}`);
});
