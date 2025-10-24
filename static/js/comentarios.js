document.addEventListener("DOMContentLoaded", () => {
  // esto no usa Jinja toma el valor desde el DOM
  const avisoId = document.body.dataset.avisoId;
  const comentariosDiv = document.getElementById("comentarios");
  const form = document.getElementById("formComentario");

  if (!avisoId) {
    comentariosDiv.innerHTML = "<p>ID de aviso no disponible.</p>";
    return;
  }

  function cargarComentarios() {
    fetch(`/api/comentarios/${avisoId}`)
      .then(r => r.json())
      .then(data => {
        comentariosDiv.innerHTML = data.length
          ? data.map(c => `
            <div class="comentario">
              <p><b>${c.nombre}</b> (${c.fecha})</p>
              <p>${c.texto}</p>
            </div>
          `).join('')
          : "<p>No hay comentarios aún.</p>";
      })
      .catch(() => {
        comentariosDiv.innerHTML = "<p>Error al cargar comentarios.</p>";
      });
  }

  form.addEventListener("submit", e => {
    e.preventDefault();
    const nombre = document.getElementById("nombre").value.trim();
    const texto = document.getElementById("texto").value.trim();

    fetch(`/api/comentarios/${avisoId}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ nombre, texto })
    })
      .then(async res => {
        if (!res.ok) {
          const data = await res.json().catch(()=>({errores:['Error desconocido']}));
          alert((data.errores||['Error']).join("\n"));
          return;
        }
        form.reset();
        cargarComentarios();
      });
  });

  cargarComentarios();
});
