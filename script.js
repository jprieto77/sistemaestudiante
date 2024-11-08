let map;
let marker;
let mode = 'residencia'; // Modo predeterminado, actualizar la residencia, es decir, las primeras coordenadas en agregar por defecto son las de la residencia

function initMap() {
    const initialPosition = { lat: 4.60971, lng: -74.08175 }; // Coordenadas de Bogotá, Colombia

    map = new google.maps.Map(document.getElementById("map"), {
        center: initialPosition,
        zoom: 12,
    });

    map.addListener("click", (event) => {
        placeMarker(event.latLng);
        if (mode === 'residencia') {
            document.getElementById("latitud").value = event.latLng.lat().toFixed(8);
            document.getElementById("longitud").value = event.latLng.lng().toFixed(8);
        } else if (mode === 'trabajo') {
            document.getElementById("latitud_trabajo").value = event.latLng.lat().toFixed(8);
            document.getElementById("longitud_trabajo").value = event.latLng.lng().toFixed(8);
        }
    });
}

function placeMarker(location) {
    if (marker) {
        marker.setMap(null);
    }
    marker = new google.maps.Marker({
        position: location,
        map: map,
    });
}

// Función para alternar entre modo residencia y trabajo
function switchMode(newMode) {
    mode = newMode;
    // Actualizamos los campos visualmente para mostrar qué coordenadas se están actualizando
    if (newMode === 'residencia') {
        document.getElementById("direccion").focus();
    } else if (newMode === 'trabajo') {
        document.getElementById("direccion_trabajo").focus();
    }
}

// Cambiar el modo a 'residencia'
function setResidenciaMode() {
    switchMode('residencia');
}

// Cambiar el modo a 'trabajo'
function setTrabajoMode() {
    switchMode('trabajo');
}

function guardarUsuario() {
    const cedula = document.getElementById("cedula").value;
    const nombres = document.getElementById("nombres").value;
    const apellidos = document.getElementById("apellidos").value;
    const direccion = document.getElementById("direccion").value;
    const latitud = parseFloat(document.getElementById("latitud").value);
    const longitud = parseFloat(document.getElementById("longitud").value);
    const direccion_trabajo = document.getElementById("direccion_trabajo").value;
    const latitud_trabajo = parseFloat(document.getElementById("latitud_trabajo").value);
    const longitud_trabajo = parseFloat(document.getElementById("longitud_trabajo").value);

    const usuario = {
        cedula,
        nombres,
        apellidos,
        direccion,
        latitud,
        longitud,
        direccion_trabajo,
        latitud_trabajo,
        longitud_trabajo
    };

    // Enviar los datos al backend usando fetch
    fetch("http://127.0.0.1:5000/guardar_usuario", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(usuario)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.mensaje);
        alert(data.mensaje);
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Ocurrió un error al guardar el usuario.");
    });
}

// Inicializar el mapa cuando se carga la página
window.onload = initMap;
