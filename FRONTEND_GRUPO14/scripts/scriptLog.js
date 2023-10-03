//******************************************************* */

// Func carga canales cuando se selecciona un servidor
function cargarCanales(id_servidor) {
    // Función para cargar los canales de un servidor
    function cargarCanales(servidorId) {
        fetch(`/canales/${servidorId}`)
            .then(response => response.json())
            .then(data => {
                const canalesServidor = document.getElementById('canales-servidor');
                canalesServidor.innerHTML = ''; // Limpia cualquier contenido anterior

                if (data.length === 0) {
                    canalesServidor.textContent = 'No se encontraron canales para este servidor.';
                } else {
                    const listaCanales = document.createElement('ul');
                    data.forEach(canal => {
                        const listItem = document.createElement('li');
                        listItem.textContent = canal.nombre;
                        listaCanales.appendChild(listItem);
                    });
                    canalesServidor.appendChild(listaCanales);
                }
            })
            .catch(error => console.error('Error:', error));
    }
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