from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])  

# Configuración de la base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:12345@localhost/SistemaEstudiantes"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de la tabla Estudiantes
class Estudiante(Base):
    __tablename__ = "Estudiantes"
    cedula = Column(String(50), primary_key=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    direccion_residencia = Column(String)
    latitud_residencia = Column(Float)
    longitud_residencia = Column(Float)
    direccion_trabajo = Column(String, nullable=True)
    latitud_trabajo = Column(Float, nullable=True)
    longitud_trabajo = Column(Float, nullable=True)


Base.metadata.create_all(engine)

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    data = request.json
    session = Session()

    estudiante = Estudiante(
        cedula=data["cedula"],
        nombres=data["nombres"],
        apellidos=data["apellidos"],
        direccion_residencia=data["direccion"],
        latitud_residencia=data["latitud"],
        longitud_residencia=data["longitud"],
        direccion_trabajo=data["direccion_trabajo"],
        latitud_trabajo=data["latitud_trabajo"],
        longitud_trabajo=data["longitud_trabajo"]
    )

    # Se guarda el estudiante en la base de datos
    session.add(estudiante)
    session.commit()
    session.close()

    return jsonify({"mensaje": "Usuario guardado correctamente"}), 201

if __name__ == "__main__":
    app.run(debug=True)
