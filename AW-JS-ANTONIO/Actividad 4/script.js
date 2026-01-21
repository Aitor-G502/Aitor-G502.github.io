//SECTOR 1 //


function cambiarTexto() {
   const textoEjemplo = document.getElementById("textoEjemplo");
textoEjemplo.style.backgroundColor = "beige";

textoEjemplo.textContent = "Hola, se ha modificado este texto";
}
function restaurarTexto() {
   const textoEjemplo = document.getElementById("textoEjemplo");
textoEjemplo.style.backgroundColor = "white";

textoEjemplo.textContent = "Este texto será modificado cuando hagas clic.";
}

// SECTOR 4 //

const nuevoItem = document.getElementById("nuevoItem")

// listaElementos.removeChild(li[100000])


// SECTOR 5 //

function cambiarCajas(){
    const cajas = document.querySelectorAll(".caja");
    for (let i = 0; i < cajas.length; i++) {
        cajas[i].style.backgroundColor = generarColorAleatorio();
    }
}

document.querySelectorAll('.caja').forEach(caja => {
    caja.addEventListener('mouseenter', () => caja.style.opacity ='0');
    caja.addEventListener('mouseleave', () => caja.style.opacity ='1');
});




// color aleatorio //
function generarColorAleatorio() {
// Generar un color hexadecimal aleatorio
const letras = '0123456789ABCDEF';
let color = '#';
for (let i = 0; i < 6; i++) {
color += letras[Math.floor(Math.random() * 16)];
}
return color;
}