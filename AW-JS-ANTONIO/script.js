//SECTOR 1 //
const textoEjemplo = document.getElementById("textoEjemplo");
textoEjemplo.style.backgroundColor = "beige";

textoEjemplo.textContent = "Hola, se ha modificado este texto";

function cambiarTexto() {
    document.getElementById("textoEjemplo").style.color = "white";
}
function restaurarTexto() {
    document.getElementById("textoEjemplo").style.color = "black";
}


