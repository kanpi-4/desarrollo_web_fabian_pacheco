//este codigo esta basado en lo que se vio en el aux

//creamos las funciones que validan cada parametro asumineod que se va obtener el value de
//cada elemento. retorna true si es valido el value
const validateName = (name) => {
  if(!name) return false;
  let lengthValid =  name.trim().length >= 4;
  
  return lengthValid;
}

const validateEmail = (email) => {
  if (!email) return false;
  let lengthValid = email.length > 15;

  // validamos el formato
  let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  let formatValid = re.test(email);

  // devolvemos la lógica AND de las validaciones.
  return lengthValid && formatValid;
};

const validatePhoneNumber = (phoneNumber) => {
  //el numero es opcional
  if (!phoneNumber) return true;
  // validación de longitud
  let lengthValid = phoneNumber.length >= 8;

  // validación de formato
  let re = /^\+\d{3}\.\d{8}$/;
  let formatValid = re.test(phoneNumber);

  // devolvemos la lógica AND de las validaciones.
  return lengthValid && formatValid;
};



const validateSelect = (select) => {
  if(!select) return false;
  return true
}


const validateTipoMascota=(tipoMascota)=>{
  if (tipoMascota=="") return false ;
  else return true
}

const validateCantidadMascota = (cantidadMascota) => {
  
  if (cantidadMascota === "" || cantidadMascota < 1) {
    return false;
  }
  return true;
};



const validateEdadMascota = (edadMascota) => {
  
  if (edadMascota === "" || edadMascota < 1) {
    return false;
  }
  return true;
};

const validateUnidadMedida=(unidadMedida)=>{
  if (unidadMedida==="") return false
  else return true
}



  //obtener la fecha de  now mas 3 h
  // Obtener la fecha y hora actual
  const now = new Date();

  // Sumar 3 horas
   now.setHours( now.getHours() + 3);

  // Formatear para el input datetime-local (YYYY-MM-DDTHH:MM)
  const añoo = now.getFullYear();
  const mess = String( now.getMonth() + 1).padStart(2, '0');
  const diaa = String( now.getDate()).padStart(2, '0');
  const horass = String( now.getHours()).padStart(2, '0');
  const minutoss = String( now.getMinutes()).padStart(2, '0');

  const valorDateTimeLocall = `${añoo}-${mess}-${diaa}T${horass}:${minutoss}`;



const validatehoramas3=(horamas3)=>{
  if (horamas3<valorDateTimeLocall) return false
  else return true


}



const validateFotos = () => {
  // Obtener todos los inputs de tipo file que tengan name="files"
  const fileInputs = document.querySelectorAll('input[type="file"][name="aviso-img"]');
  
  // Verificar si alguno tiene al menos un archivo
  for (let input of fileInputs) {
    if (input.files.length > 0) {
      return true; //  ya hay al menos un archivo
    }
  }
  return false; // ninguno tiene archivo
};




//se usan las funciones creadas anteriormente, se obtiene los elementos html, y se hace una 
//lista de los errores o se de un mensaje de exito en caso de que todo resulte true
const validateForm = () => {
  // obtener elementos del DOM usando el nombre del formulario.
  let myForm = document.forms["myForm"];
  let email = myForm["email"].value;
  let phoneNumber = myForm["celular"].value;
  let name = myForm["nombre"].value;
  
  let region = myForm["region_id"].value;
  let comuna = myForm["comuna_id"].value;
  let tipoMascota= myForm["tipo"].value
  let cantidadMascota=myForm["cantidad"].value
  let edadMascota=myForm["edad"].value
  let unidadMedida=myForm["unidad_medida"].value
  let fecha=myForm["fecha_entrega"].value


  // variables auxiliares de validación y función.
  let invalidInputs = [];
  let isValid = true;
  const setInvalidInput = (inputName) => {
    invalidInputs.push(inputName);
    isValid &&= false;
  };

  // lógica de validación
  if (!validateName(name)) {
    setInvalidInput("Nombre");
  }
  if (!validateEmail(email)) {
    setInvalidInput("Email");
  }
  if (!validatePhoneNumber(phoneNumber)) {
    setInvalidInput("Número");
  }
  
  if (!validateSelect(region)) {
    setInvalidInput("Region");
  }
  if (!validateSelect(comuna)) {
    setInvalidInput("Comuna");
  }
  if (!validateTipoMascota(tipoMascota)){
    setInvalidInput("Tipo")
  }
  if (!validateEdadMascota(edadMascota)){
    setInvalidInput("Edad")
  }
  if (!validateCantidadMascota(cantidadMascota)){
    setInvalidInput("Cantidad")
  }

  if (!validateUnidadMedida(unidadMedida)){
    setInvalidInput("Unidad de medida")
  }

  if (!validatehoramas3(fecha)){
    setInvalidInput("Fecha disponible")
  }

  if (!validateFotos()){
    setInvalidInput("Fotos")
  }

 


  // finalmente mostrar la validación
  let validationBox = document.getElementById("val-box");
  let validationMessageElem = document.getElementById("val-msg");
  let validationListElem = document.getElementById("val-list");
  let formContainer = document.querySelector(".main-container");
  //para apuntar hacia el nuevo mensaje
    window.scrollTo(0, 0);

  if (!isValid) {

    validationListElem.textContent = "";
    // agregar elementos inválidos al elemento val-list.
    for (input of invalidInputs) {
      let listElement = document.createElement("li");
      listElement.innerText = input;
      validationListElem.append(listElement);
    }
    // establecer val-msg
    validationMessageElem.innerText = "Los siguientes campos son inválidos:";

    // aplicar estilos de error
    validationBox.style.backgroundColor = "#ffdddd";
    validationBox.style.borderLeftColor = "#f44336";

    // hacer visible el mensaje de validación
    validationBox.hidden = false;
  } else {
    //para apuntar hacia el nuevo mensaje
    window.scrollTo(0, 0);

    

    botonAntesDeConfirmar=document.getElementById("enviarForm")
    botonAntesDeConfirmar.style.display="none"
    // establecer mensaje de éxito
    validationMessageElem.innerText = "¿Está seguro que desea agregar este aviso de adopción?";
    validationListElem.textContent = "";

    // aplicar estilos de éxito
    validationBox.style.backgroundColor = "#ddffdd";
    validationBox.style.borderLeftColor = "#4CAF50";

    // Agregar botones para enviar el formulario o volver
    let submitButton = document.createElement("button");
    //el boton creado en si estoy seguro enviara los datos
    submitBtn.type="submit";
    submitButton.innerText = "Sí, estoy seguro";
    submitButton.style.marginRight = "10px";

    
    let backButton = document.createElement("button");
    backButton.type = "button";
    backButton.innerText = "“No, no estoy seguro, quiero volver al formulario";
    backButton.addEventListener("click", () => {
      // Mostrar el formulario nuevamente
      botonAntesDeConfirmar.style.display = "block";
      validationBox.hidden = true;
    });
    validationListElem.appendChild(submitButton);
    validationListElem.appendChild(backButton);

    // hacer visible el mensaje de validación
    validationBox.hidden = false;
  }
};


let submitBtn = document.getElementById("enviarForm");
submitBtn.addEventListener("click", validateForm);
















