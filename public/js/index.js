

import { recuperarData, getMascotas, crearCards } from './cards.js';

// Filtros de ejemplo (puedes mejorar la lógica según tu UI real)
let mascotasFilter = [];

async function selectUbicacion() {
    const DATA = await recuperarData();
    const ubicacionesUnicas = new Set();
    if (DATA && DATA.pets) {
        DATA.pets.forEach(mascota => {
            if (mascota.ubication) ubicacionesUnicas.add(mascota.ubication);
        });
    }
    const ubicacionesArray = Array.from(ubicacionesUnicas);
    const ubicaciones = document.querySelector('#ubicaciones');
    for (let i = 0; i < ubicacionesArray.length; i++) {
        const option = document.createElement("option");
        option.classList.add('optionUbic');
        option.value = ubicacionesArray[i];
        option.textContent = ubicacionesArray[i];
        ubicaciones.appendChild(option);
    }
    return ubicaciones;
}

selectUbicacion();

// Eliminar lógica rota y logs innecesarios
   
    
