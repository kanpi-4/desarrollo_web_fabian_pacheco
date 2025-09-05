
// obtener la fecha y hora actual
const ahora = new Date();

// a la hora actual se le suma 3
ahora.setHours(ahora.getHours() + 3);

// obtenemos el año el mes el dia la hora ya cambiada y los minutos
//finalmente juntamos todo para obtener la fecha actual mas 3 horas
const año = ahora.getFullYear();
const mes = String(ahora.getMonth() + 1).padStart(2, '0');
const dia = String(ahora.getDate()).padStart(2, '0');
const horas = String(ahora.getHours()).padStart(2, '0');
const minutos = String(ahora.getMinutes()).padStart(2, '0');

const valorDateTimeLocal = `${año}-${mes}-${dia}T${horas}:${minutos}`;

// establecer esa hora como  valor predeterminado
document.getElementById('horamas3').value = valorDateTimeLocal;