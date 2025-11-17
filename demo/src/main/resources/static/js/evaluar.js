async function evaluar(btn) {
    const avisoId = btn.getAttribute('data-aviso-id');
    // pedir nota al usuario (1..7)
    let input = prompt("Ingrese una nota entera entre 1 y 7 para este aviso:");
    if (input === null) return; // usuario cancelo

    input = input.trim();
    const nota = parseInt(input, 10);
    if (isNaN(nota) || nota < 1 || nota > 7) {
        alert("Nota inválida. Debe ser un número entero entre 1 y 7.");
        return;
    }

    try {
        const resp = await fetch('/api/notas/agregar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ avisoId: avisoId, nota: nota })
        });

        const json = await resp.json();
        if (!resp.ok) {
            alert("Error: " + (json.error || JSON.stringify(json)));
            return;
        }

        // actualizar la fila correspondiente
        // recorremos hasta encontrar el <tr> padre
        let tr = btn.closest('tr');
        if (!tr) return;

        // celda de nota es la 8ava columna (index 7)
        const notaCell = tr.children[7];

        if (json.count == 0) {
            notaCell.innerHTML = '-';
        } else {
            // formatear promedio con 1 decimal
            const avg = Number(json.average);
            notaCell.innerHTML = avg.toFixed(1) + '<br/><small>(' + json.count + ' nota(s))</small>';
        }
        alert("Nota agregada correctamente.");
    } catch (e) {
        console.error(e);
        alert("Error al comunicarse con el servidor.");
    }
}
