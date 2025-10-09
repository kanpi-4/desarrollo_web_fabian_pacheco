const filas = document.querySelectorAll("tbody tr");

filas.forEach(fila => {
    fila.addEventListener("click", () => {
        window.location.href =fila.id;
    });
});
