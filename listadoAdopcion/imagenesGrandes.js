// seleccionamos todas los fotos de la  pagina
const todasLasImagenes = document.querySelectorAll('img');

// para cada imagen le hacemo un addevent listener que hara que con el click el div es
//escondido ya no sea escondido
todasLasImagenes.forEach(imagen => {
    imagen.addEventListener('click', function() {
        // Mostrar el div escondido
        divEscondido=document.getElementById('div-escondido')
        divEscondido.hidden=false
        
        
        
        

        
        // limpiamos el contenido anterior
        const fotoGrande = document.getElementById('foto-grande');
        fotoGrande.innerHTML = '';
        
        // ponemos la imagenes y modificamos su tamaño
        const imagenGrande = document.createElement('img');
        imagenGrande.src = this.src; // Usar la misma source de la imagen clickeada
        imagenGrande.style.width = "800px";
        imagenGrande.style.height = "600px";
  
        
        // agregamos la imagen al div en html
        fotoGrande.appendChild(imagenGrande);
    });
});

//  para el botón cerrar
document.getElementById('cerrar').addEventListener('click', function() {
    document.getElementById('div-escondido').hidden = true;
});