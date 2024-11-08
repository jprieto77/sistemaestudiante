from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Estudiante 

class EstudianteDAO:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def guardar_estudiante(self, estudiante_dto):
        session = self.Session()
        estudiante = Estudiante(
            cedula=estudiante_dto.cedula,
            nombres=estudiante_dto.nombres,
            apellidos=estudiante_dto.apellidos,
            direccion_residencia=estudiante_dto.direccion,
            latitud_residencia=estudiante_dto.latitud,
            longitud_residencia=estudiante_dto.longitud,
            direccion_trabajo=estudiante_dto.direccion_trabajo, 
            latitud_trabajo=estudiante_dto.latitud_trabajo,  
            longitud_trabajo=estudiante_dto.longitud_trabajo  
        )
        session.add(estudiante)
        session.commit()
        session.close()

    def obtener_estudiantes(self):
        session = self.Session()
        estudiantes = session.query(Estudiante).all()
        session.close()
        return estudiantes
