from config import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo_tarea = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    estado_tarea = db.Column(db.String(20), default="agendada", nullable=False)

    def __repr__(self):
        return f"Tarea #{self.id}.\nTitulo: {self.titulo_tarea}\nDescripcion: {self.descripcion}\nEstado: {self.estado_tarea}"
    
