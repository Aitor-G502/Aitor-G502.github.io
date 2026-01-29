//SECTOR 1 //


function cambiarTexto() {                                          // crea una funcion llamada cambiartexto
   const textoEjemplo = document.getElementById("textoEjemplo"); //crea una variable y busca los elementos con la id textoEjemplo
textoEjemplo.style.backgroundColor = "beige";                   // cambia el color de texto ejemplo

textoEjemplo.textContent = "Hola, se ha modificado este texto"; // modifica el texto de texto ejemp
}
function restaurarTexto() {
   const textoEjemplo = document.getElementById("textoEjemplo");   //crea una funcion que crea una variable que busca elementos por id que cambia su fondo a blanco
textoEjemplo.style.backgroundColor = "white";

textoEjemplo.textContent = "Este texto será modificado cuando hagas clic.";  // 
}

// SECTOR 4 //

const nuevoItem = document.getElementById("nuevoItem") // crea una nueva variable llamada nuevoItem y busca los elementos que tengan la ID nuevoItem

// listaElementos.removeChild(li[100000])


// SECTOR 5 //

function cambiarCajas(){
    const cajas = document.querySelectorAll(".caja"); // Crea la variable cajas y busca todos los elementos que tengan la clase caja
    for (let i = 0; i < cajas.length; i++) {
        cajas[i].style.backgroundColor = generarColorAleatorio();  //Bucle para que todas las clases cajas que no superen un limite tengan el color aleatorio
    }
}

document.querySelectorAll('.caja').forEach(caja => {       // Busca todos los elementos con la clase caja y por cada caja  crea eventos para que se vean o se vuelva invisible una caja
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