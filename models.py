# models.py
from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "Estudiantes"  # Nombre de la tabla en la base de datos

    cedula = Column(String(50), primary_key=True)  # Campo para cédula
    nombres = Column(String(100))  # Campo para nombres
    apellidos = Column(String(100))  # Campo para apellidos
    direccion_residencia = Column(String)  # Campo para dirección de residencia
    latitud_residencia = Column(Float)  # Campo para latitud de residencia
    longitud_residencia = Column(Float)  # Campo para longitud de residencia
    direccion_trabajo = Column(String, nullable=True)  # Campo para dirección de trabajo
    latitud_trabajo = Column(Float, nullable=True)  # Campo para latitud de trabajo
    longitud_trabajo = Column(Float, nullable=True)  # Campo para longitud de trabajo


