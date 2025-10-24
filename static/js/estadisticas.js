document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/estadisticas")
    .then(r => r.json())
    .then(data => {
      // grafico 1 avisos por dia
      Highcharts.chart("grafico1", {
        title: { text: "Avisos agregados por día" },
        xAxis: { categories: data.por_dia.map(d => d.dia) },
        yAxis: { title: { text: "Cantidad" } },
        series: [{ name: "Avisos", data: data.por_dia.map(d => d.cantidad) }]
      });

      // grafico 2 torta
      Highcharts.chart("grafico2", {
        chart: { type: "pie" },
        title: { text: "Avisos por tipo" },
        series: [{
          name: "Cantidad",
          data: data.por_tipo.map(t => ({ name: t.tipo, y: t.cantidad }))
        }]
      });

      // grafico 3 mes y tipo
      const meses = [...new Set(data.por_mes_tipo.map(d => d.mes))];
      const gatos = meses.map(m => {
        const item = data.por_mes_tipo.find(d => d.mes === m && d.tipo === "gato");
        return item ? item.cantidad : 0;
      });
      const perros = meses.map(m => {
        const item = data.por_mes_tipo.find(d => d.mes === m && d.tipo === "perro");
        return item ? item.cantidad : 0;
      });

      Highcharts.chart("grafico3", {
        chart: { type: "column" },
        title: { text: "Avisos por mes y tipo" },
        xAxis: { categories: meses.map(m => `Mes ${m}`) },
        yAxis: { title: { text: "Cantidad" } },
        series: [
          { name: "Gatos", data: gatos },
          { name: "Perros", data: perros }
        ]
      });
    });
});
