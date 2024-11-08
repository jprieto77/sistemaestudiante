class EstudianteDTO:
    def __init__(self, cedula, nombres, apellidos, direccion, latitud, longitud, direccion_trabajo, latitud_trabajo, longitud_trabajo):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.direccion_trabajo = direccion_trabajo  
        self.latitud_trabajo = latitud_trabajo  
        self.longitud_trabajo = longitud_trabajo  

    def to_dict(self):
        return {
            "cedula": self.cedula,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "direccion": self.direccion,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "direccion_trabajo": self.direccion_trabajo,  
            "latitud_trabajo": self.latitud_trabajo, 
            "longitud_trabajo": self.longitud_trabajo  
        }
