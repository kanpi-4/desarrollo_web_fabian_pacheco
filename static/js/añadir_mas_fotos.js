
//esta parte es para poder agregar mas fotos aprentando un boton


//tomamos el boton y en donde se pondra las fotos
boton=document.getElementById("boton-mas-fotos")
seccionFotos=document.getElementById("seccion-fotos")

//por cada foto que se ponga , el id cambiara hasta llegar a 5
contador=1
function añadirMasFotos() {
    // crear elemento input
    if (contador==5) {
        alert("no puedes agregar mas de 5 fotos") 
        return null} 
    const nuevoInput = document.createElement("input");
    const br=document.createElement("br")
    nuevoInput.type = "file";
    nuevoInput.name = "aviso-img";
    nuevoInput.id = "fotos"+String(contador); 
    
    // Agregar al codigo html
    seccionFotos.appendChild(br)
    seccionFotos.appendChild(nuevoInput);
    
    contador+=1
}

boton.addEventListener("click", añadirMasFotos);

