from sqlalchemy import Column, Integer, String, DateTime, Enum, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    comunas = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = 'comuna'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship("Region", back_populates="comunas")

class AvisoAdopcion(Base):
    __tablename__ = 'aviso_adopcion'
    id = Column(Integer, primary_key=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100))
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15))
    tipo = Column(Enum('gato', 'perro'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(Enum('a', 'm'), nullable=False)
    fecha_entrega = Column(DateTime, nullable=False)
    descripcion = Column(Text(500))
    
    comuna = relationship("Comuna")
    

class ContactarPor(Base):
    __tablename__ = 'contactar_por'
    id = Column(Integer, primary_key=True)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)
    
    aviso = relationship("AvisoAdopcion")
    
    
    
class nuevaFoto(Base):
    __tablename__='foto'
    id = Column(Integer, primary_key=True)
    ruta_archivo=Column(String(150), nullable=False)
    nombre_archivo = Column(String(150), nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)
    aviso = relationship("AvisoAdopcion")
    

    
    
    
    
    
    
    
    
    
    
    
    
    
#modelo para el comentario    
class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha = Column(DateTime, nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship("AvisoAdopcion")

    
    
    
    
