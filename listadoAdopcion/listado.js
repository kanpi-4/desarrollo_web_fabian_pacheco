// selecciona todas las filas
const filas = document.querySelectorAll("tbody tr");

// recorre cada fila
//y hacemos que cada vez que de click a una fila, el window.location es decir donde estemos, sea
//la pagina donde tenemos los detalles del aviso
for (const fila of filas) {
  fila.addEventListener("click", () => {
    // toma el id (ej: "aviso1-fila")
    const aviso = fila.id;  

    // quita el "-fila" para quedarte con "aviso1"
    

    // redirige a la página correspondiente
    window.location.href = aviso;
  });
}
