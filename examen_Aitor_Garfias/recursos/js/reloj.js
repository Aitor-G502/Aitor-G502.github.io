const ahora = new Date();

const hora = ahora.getHours().toString().padStart(2, '0');
const minutos = ahora.getMinutes().toString().padStart(2, '0');
const segundos = ahora.getSeconds().toString().padStart(2, '0');

document.getElementById("reloj").textContent = `${hora}:${minutos}:${segundos}`;
