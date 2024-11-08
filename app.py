from flask import Flask, request, jsonify
from flask_cors import CORS  # Asegúrate de importar CORS
from sqlalchemy import create_engine
from dao import EstudianteDAO  
from dto import EstudianteDTO  

app = Flask(__name__)

# Configuración de CORS para permitir acceso desde el origen especificado
CORS(app, resources={r"/guardar_usuario": {"origins": "http://127.0.0.1:5500"}})

# Configuración de la base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:12345@localhost/SistemaEstudiantes"
engine = create_engine(DATABASE_URL)

# Inicializamos el DAO
estudiante_dao = EstudianteDAO(engine)

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    data = request.json  
    
    # Crear un DTO con los datos que llegan del frontend
    estudiante_dto = EstudianteDTO(
        cedula=data["cedula"],
        nombres=data["nombres"],
        apellidos=data["apellidos"],
        direccion=data["direccion"],
        latitud=data["latitud"],
        longitud=data["longitud"],
        direccion_trabajo=data["direccion_trabajo"],
        latitud_trabajo=data["latitud_trabajo"],
        longitud_trabajo=data["longitud_trabajo"]
    )
    
    # Guardar al estudiante utilizando el DAO
    estudiante_dao.guardar_estudiante(estudiante_dto)
    
    # Responder con los datos del DTO
    return jsonify(estudiante_dto.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)
