// Datos de ejemplo de mensajes
/*const mensajes = [
    { usuario: "Usuario1", mensaje: "Hola, ¿cómo estás?" },
    { usuario: "Usuario2", mensaje: "¡Hola! Estoy bien, ¿y tú?" },
    { usuario: "Usuario1", mensaje: "Maso me cuesta el TIF" },
    { usuario: "Usuario2", mensaje: "Tamos en la misma" },
    { usuario: "Usuario1", mensaje: "En particular el fron, tengo 2 dias para hacerlo." },
    { usuario: "Usuario2", mensaje: "QUEE.....!? Pense que tenia todo el finde para terminarlo. MMMMMmmmm no se si termino. aklsjdhlaskjdnasjknc" },
    // Puedes agregar más mensajes aquí
];

// Función para mostrar mensajes en la columna de mensajes
function mostrarMensajes() {
    const columnaMensajes = document.querySelector(".columnMensajes");

    // Limpiar la columna de mensajes antes de agregar nuevos mensajes
    columnaMensajes.innerHTML = "";

    // Recorrer la lista de mensajes y crear elementos para cada uno
    mensajes.forEach((mensaje) => {
        const mensajeElement = document.createElement("div");
        mensajeElement.classList.add("mensaje");
        mensajeElement.innerHTML = `<strong>${mensaje.usuario}:</strong> ${mensaje.mensaje}`;
        
        // Agregar el mensaje a la columna de mensajes
        columnaMensajes.appendChild(mensajeElement);
    });
}

// Llamar a la función para mostrar mensajes cuando la página se carga
window.addEventListener("load", mostrarMensajes);
*/


//******************************************************* */
// Función para agregar un mensaje al chat
function addMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
}

// Manejo del botón de enviar
const sendButton = document.getElementById('send-button');
sendButton.addEventListener('click', function() {
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value.trim();
    
    if (message !== '') {
        addMessage(message);
        messageInput.value = '';
    }
});

// Manejo de la tecla Enter en el input
const messageInput = document.getElementById('message-input');
messageInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        const message = messageInput.value.trim();
        
        if (message !== '') {
            addMessage(message);
            messageInput.value = '';
        }
    }
}); 