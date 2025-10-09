document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal-foto');
    const modalImagen = document.getElementById('modal-imagen');
    const cerrarModal = document.getElementById('cerrar-modal');
    const fotos = document.querySelectorAll('.fotoDetalle');
    
    // Función para abrir el modal
    function abrirModal(src) {
        modalImagen.src = src;
        modal.classList.remove('modal-hidden');
        modal.classList.add('modal-visible');
    }
    
    // Función para cerrar el modal
    function cerrarModalFunc() {
        modal.classList.remove('modal-visible');
        modal.classList.add('modal-hidden');
        modalImagen.src = '';
    }
    
    // Agregar event listeners a cada foto
    fotos.forEach(foto => {
        foto.addEventListener('click', function() {
            abrirModal(this.src);
        });
    });
    
    // Cerrar modal con el botón
    cerrarModal.addEventListener('click', cerrarModalFunc);
    
    // Cerrar modal haciendo click fuera de la imagen
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            cerrarModalFunc();
        }
    });
    
    // Cerrar modal con la tecla ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('modal-visible')) {
            cerrarModalFunc();
        }
    });
});