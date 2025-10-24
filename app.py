from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import SessionLocal, engine, Base, get_aviso,get_foto_by_id,get_comuna_by_id, aviso_vacio, get_aviso_ultimos, numero_de_avisos, get_fotos_by_id,get_fotos,cantidad_fotos_por_id,get_aviso_by_id,get_region_by_id, get_comentarios_by_aviso,insertar_comentario
from models import AvisoAdopcion, ContactarPor, Comuna, Region, nuevaFoto
from datetime import datetime
import filetype
import os
import hashlib
from werkzeug.utils import secure_filename





from validaciones import *

LISTA_FOLDER='templates'
UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LISTA_FOLDER'] = LISTA_FOLDER

@app.route('/',methods=["GET"])          
def portada():
    #obtener ultimos avisos
    avisos = []
    vacio=aviso_vacio()
    if vacio:
        return render_template('portada.html',avisos=False)
    for aviso in get_aviso_ultimos(page_size=5):
        #obtenemos la utlima foto
        foto = get_foto_by_id(aviso.id)
        comuna=get_comuna_by_id(aviso.comuna_id)

        img_filename = f"uploads/{foto.ruta_archivo}"
        avisos.append({
            "fechaPublicacion": aviso.fecha_ingreso,
            "comuna": comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad":aviso.edad,
            "edadMedida":aviso.unidad_medida,
            "path_image": url_for('static', filename=img_filename)
        })
    return render_template('portada.html',avisos=avisos)

@app.route("/anadir-aviso", methods=["GET", "POST"])
def anadir_aviso():
    db = SessionLocal()
    
    if request.method == "GET":
        regiones = db.query(Region).all()
        comunas = db.query(Comuna).all()
        
        
        db.close()
        
        
        return render_template("añadir-aviso.html", regiones=regiones, comunas=comunas)
    
    if request.method == "POST":
    # recibir datos del formulario (esto se mantiene igual)
        nombre = request.form["nombre"]
        email = request.form["email"]
        comuna_id = int(request.form["comuna_id"])
        tipo = request.form["tipo"]
        cantidad = int(request.form["cantidad"])
        edad = int(request.form["edad"])
        unidad_medida = request.form["unidad_medida"]
        fecha_entrega_str = request.form["fecha_entrega"]
    
        # Obtener TODAS las fotos (no solo una)
        aviso_imgs = request.files.getlist("aviso-img")  # getlist() en vez de get()
        
        # Convertir fecha
        fecha_entrega = datetime.strptime(fecha_entrega_str, '%Y-%m-%d')
        
        descripcion = request.form.get("descripcion", "")
        sector = request.form.get("sector", "")
        celular = request.form.get("celular", None)

        # Crear el aviso
        nuevo_aviso = AvisoAdopcion(
            fecha_ingreso=datetime.now(),
            comuna_id=comuna_id,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=celular,
            tipo=tipo,
            cantidad=cantidad,
            edad=edad,
            unidad_medida=unidad_medida,
            fecha_entrega=fecha_entrega,
            descripcion=descripcion
        )
        errores = aviso_no_valido(nuevo_aviso) + fotos_no_valido(aviso_imgs)

        if errores:
            return render_template("error-envio.html",
                                errores=errores)

        
            
        db.add(nuevo_aviso)
        db.flush()  # genera el ID sin commit final
        
        # Guardar CADA foto
        for aviso_img in aviso_imgs:
            if aviso_img and aviso_img.filename:  # Verificar que no esté vacío
                _filename = hashlib.sha256(
                    secure_filename(aviso_img.filename)
                    .encode("utf-8")
                ).hexdigest()
                _extension = filetype.guess(aviso_img).extension
                img_filename = f"{_filename}.{_extension}"
                
                # Guardar archivo
                aviso_img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                
                # Crear registro en la base de datos
                nueva_foto = nuevaFoto(
                    ruta_archivo=img_filename,
                    nombre_archivo=_filename,
                    aviso_id=nuevo_aviso.id
                )
                db.add(nueva_foto)
        
        db.commit()
        db.close()
        
        return redirect(url_for("portada"))

@app.route("/api/comunas/<int:region_id>")
def api_comunas(region_id):
    db = SessionLocal()
    comunas = db.query(Comuna).filter(Comuna.region_id == region_id).all()
    db.close()
    
    comunas_data = [{"id": c.id, "nombre": c.nombre} for c in comunas]
    return jsonify(comunas_data)

@app.route('/lista')
@app.route('/lista/<int:page>')
def lista_avisos(page=1):  # page=1 por defecto
    
    avisos = []
    vacio=aviso_vacio()
    if vacio:
        return render_template('lista.html',avisos=False)
    for aviso in get_aviso(page, page_size=5):
        
        comuna=get_comuna_by_id(aviso.comuna_id)
        numeroDeFotos=cantidad_fotos_por_id(aviso.id)
        avisos.append({
            "nombre":aviso.nombre,
            "fecha_entrega":aviso.fecha_entrega,
            "fechaPublicacion": aviso.fecha_ingreso,
            "comuna": comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad":aviso.edad,
            "edadMedida":aviso.unidad_medida,   
            "cantidadFotos":numeroDeFotos,
            "id":aviso.id  

        })
    
        
    
    total_avisos = numero_de_avisos()  # Función para contar total
    return render_template('lista.html',
                           avisos=avisos, 
                         current_page=page,
                         total_pages=(total_avisos + 4) // 5)  # +4 para redondear hacia arriba
    
    

@app.route('/detalle/<int:aviso_id>')
def detalle_aviso(aviso_id):
    aviso = get_aviso_by_id(aviso_id)
    dataAviso=({
        "id": aviso.id, 
        "nombre":aviso.nombre,
        "email":aviso.email,
        "sector":aviso.sector,
        "fecha_ingreso":aviso.fecha_ingreso,
        "celular":aviso.celular,
        "tipo":aviso.tipo,
        "cantidad":aviso.cantidad,
        "edad":aviso.edad,
        "unidad_medida":aviso.unidad_medida,
        "fecha_entrega":aviso.fecha_entrega,
        "descripcion":aviso.descripcion
    })
    
    getcomuna=get_comuna_by_id(aviso.comuna_id)
    comuna=getcomuna.nombre
    getregion=get_region_by_id(getcomuna.region_id)
    region=getregion.nombre
    fotos=[]
    for foto in get_fotos_by_id(aviso_id):
        img_filename = f"uploads/{foto.ruta_archivo}"
        ruta=url_for('static', filename=img_filename)
        fotos.append(ruta)
        
        
    return render_template('detalle.html', info=dataAviso,comuna=comuna,region=region,fotos=fotos)

    
    
    

#rutas para los comentarios

@app.route('/api/comentarios/<int:aviso_id>', methods=['GET'])
def api_get_comentarios(aviso_id):
    comentarios = get_comentarios_by_aviso(aviso_id)
    data = [{
        "nombre": c.nombre,
        "texto": c.texto,
        "fecha": c.fecha.strftime("%Y-%m-%d %H:%M:%S")
    } for c in comentarios]
    return jsonify(data)


@app.route('/api/comentarios/<int:aviso_id>', methods=['POST'])
def api_post_comentario(aviso_id):
    data = request.get_json()
    nombre = data.get("nombre", "").strip()
    texto = data.get("texto", "").strip()

    errores = []
    if not (3 <= len(nombre) <= 80):
        errores.append("el nombre debe tener entre 3 y 80 caracteres.")
    if not (5 <= len(texto) <= 300):
        errores.append("el comentario debe tener entre 5 y 300 caracteres.")

    if errores:
        return jsonify({"errores": errores}), 400

    insertar_comentario(nombre, texto, aviso_id)
    return jsonify({"mensaje": "comentario agregado exitosamente."}), 201



#estadisticas
@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')


@app.route('/api/estadisticas')
def api_estadisticas():
    from sqlalchemy import func, extract
    db = SessionLocal()

    # cantidad por dia
    por_dia = db.query(
        func.date(AvisoAdopcion.fecha_ingreso).label('dia'),
        func.count(AvisoAdopcion.id)
    ).group_by('dia').order_by('dia').all()

    # tipo
    por_tipo = db.query(
        AvisoAdopcion.tipo,
        func.count(AvisoAdopcion.id)
    ).group_by(AvisoAdopcion.tipo).all()

    # por mes y tipo 
    por_mes_tipo = db.query(
        extract('month', AvisoAdopcion.fecha_ingreso).label('mes'),
        AvisoAdopcion.tipo,
        func.count(AvisoAdopcion.id)
    ).group_by('mes', AvisoAdopcion.tipo).order_by('mes').all()

    db.close()

    return jsonify({
        "por_dia": [{"dia": str(d), "cantidad": c} for d, c in por_dia],
        "por_tipo": [{"tipo": t, "cantidad": c} for t, c in por_tipo],
        "por_mes_tipo": [{"mes": int(m), "tipo": t, "cantidad": c} for m, t, c in por_mes_tipo]
    })

    
    

    
if __name__ == "__main__":
    app.run(debug=True)