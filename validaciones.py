
import re
import filetype
from datetime import datetime

# Extensiones y tipos MIME permitidos
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

def validate_conf_img(conf_img):

    ftype_guess = filetype.guess(conf_img)
   

    # Validar extensión
    if ftype_guess!=None:
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False

        # Validar MIME type
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False

    return True

def aviso_no_valido(aviso):
    errores = []

    # Nombre: obligatorio, largo mínimo 3 y máximo 200
    if not aviso.nombre or len(aviso.nombre.strip()) < 3 or len(aviso.nombre.strip()) > 200:
        errores.append("El nombre es obligatorio y debe tener entre 3 y 200 caracteres.")

    # Email: obligatorio, formato válido, máximo 100
    patron_email = r"^[^@]+@[^@]+\.[^@]+$"
    if not aviso.email or len(aviso.email) > 100 or not re.match(patron_email, aviso.email):
        errores.append("El email es obligatorio, válido y de máximo 100 caracteres.")

    # Comuna: obligatorio
    if not aviso.comuna_id:
        errores.append("Debe seleccionar una comuna.")

    # Sector: opcional, máximo 100
    if aviso.sector and len(aviso.sector) > 100:
        errores.append("El sector no puede superar los 100 caracteres.")

    # Celular: opcional, formato +NNN.NNNNNNNN
    if aviso.celular:
        patron_cel = r"^\+\d{1,3}\.\d{6,15}$"
        if not re.match(patron_cel, aviso.celular):
            errores.append("El número de celular debe cumplir el formato +NNN.NNNNNNNN.")

    # Tipo: obligatorio, gato o perro
    if aviso.tipo not in ["perro", "gato"]:
        errores.append("Debe seleccionar el tipo de mascota (gato o perro).")

    # Cantidad: >= 1
    if not aviso.cantidad or aviso.cantidad < 1:
        errores.append("La cantidad debe ser un entero mayor o igual a 1.")

    # Edad: >= 1
    if not aviso.edad or aviso.edad < 1:
        errores.append("La edad debe ser un número entero mayor o igual a 1.")

    # Unidad de medida edad: obligatorio
    if aviso.unidad_medida not in ["m", "a"]:
        errores.append("Debe seleccionar la unidad de medida de edad (meses o años).")

    # Fecha entrega: obligatorio, formato correcto y >= hoy
    if not aviso.fecha_entrega:
        errores.append("Debe indicar la fecha de entrega.")
    else:
        if not isinstance(aviso.fecha_entrega, datetime):
            errores.append("La fecha de entrega no tiene el formato válido.")
        elif aviso.fecha_entrega < datetime.now():
            errores.append("La fecha de entrega debe ser mayor o igual a la fecha actual.")

    return errores

def fotos_no_valido(lista_imgs):
    errores = []

    if not lista_imgs or len(lista_imgs) < 1:
        errores.append("Debe subir al menos una foto.")
    elif len(lista_imgs) > 5:
        errores.append("No puede subir más de 5 fotos.")
    else:
        for foto in lista_imgs:
            if not validate_conf_img(foto):
                errores.append(f"El archivo {foto.filename} no es una imagen válida (solo jpg, jpeg, png).")

    return errores
