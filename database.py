from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import AvisoAdopcion, nuevaFoto, Comuna,Region


#para la parte de comentarios
from models import Comentario
from datetime import datetime

DB_USER = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "tarea2"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_aviso_ultimos(page_size):
    session = SessionLocal()
    avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.fecha_ingreso.desc()).limit(page_size).all()
    session.close()
    return avisos


def get_aviso(page_number, page_size=5):
    session = SessionLocal()
    offset = (page_number - 1) * page_size  # Calcular salto
    
    avisos = session.query(AvisoAdopcion)\
        .order_by(AvisoAdopcion.id.desc())\
        .offset(offset)\
        .limit(page_size)\
        .all()
    session.close()
    return avisos

def get_foto_by_id(id):
    session = SessionLocal()
    #obtenemso la primera foto
    foto = session.query(nuevaFoto).filter_by(aviso_id=id).first()
    session.close()
    return foto

def get_fotos_by_id(id):
    session = SessionLocal()
    #obtenemos las fotos con el mismo id
    fotos = session.query(nuevaFoto).filter_by(aviso_id=id)
    session.close()
    return fotos

def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna

#funcion para saber si hay datos
def aviso_vacio():
    session = SessionLocal()
    count = session.query(AvisoAdopcion).count()
    session.close()
    return count == 0

def numero_de_avisos():
    session = SessionLocal()
    count = session.query(AvisoAdopcion).count()
    session.close()
    return count
    
def get_fotos():
    session=SessionLocal()
    fotos=session.query(nuevaFoto)
    session.close
    return fotos

def cantidad_fotos_por_id(id):
    session = SessionLocal()
    count = session.query(nuevaFoto).filter_by(aviso_id=id).count()
    session.close()
    return count

def get_aviso_by_id(id):
    session=SessionLocal()
    aviso=session.query(AvisoAdopcion).filter_by(id=id).first()
    session.close()
    return aviso

def get_region_by_id(id):
    session=SessionLocal()
    region=session.query(Region).filter_by(id=id).first()
    session.close()
    return region



#funciones para los comentarios

def get_comentarios_by_aviso(aviso_id):
    session = SessionLocal()
    comentarios = session.query(Comentario).filter_by(aviso_id=aviso_id).order_by(Comentario.fecha.desc()).all()
    session.close()
    return comentarios

def insertar_comentario(nombre, texto, aviso_id):
    session = SessionLocal()
    nuevo = Comentario(
        nombre=nombre,
        texto=texto,
        fecha=datetime.now(),
        aviso_id=aviso_id
    )
    session.add(nuevo)
    session.commit()
    session.close()