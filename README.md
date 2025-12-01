Para el desarollo de las estadisticas, no se sabia como enviar los datos al js de forma estandar, por lo que se recurrio a ponerlo en el html de la siguente manera modificando el tag de body
<body data-aviso-id="{{ info['id'] if info is defined else '' }}">
de esta manera se logran tener los datos que necesitamos para las estadisticas de la siguente manera en el javaScript:
const avisoId = document.body.dataset.avisoId;
