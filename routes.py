from config import app, db
from models import Task
from flask import request
from flask import jsonify

# Ruta para crear la base de datos.
# @app.cli.command("create_db")
# def create_db():
#     db.create_all()
#     print("Base de datos creada")

# --------------------------------  Rutas  --------------------------------

# Ruta para agregar una tarea.
@app.route("/add_task", methods=["POST"])
def add_task():
    titulo = request.json.get("titulo_tarea")
    descripcion = request.json.get("descripcion")
    
    nueva_tarea = Task(titulo_tarea=titulo, descripcion=descripcion)
    
    db.session.add(nueva_tarea)
    db.session.commit()
    
    return nueva_tarea.__repr__()


# Ruta para obtener todas las tareas.
@app.route("/get_tasks", methods=["GET"])
def get_tasks():
    tareas = Task.query.all()

    return jsonify([{
                        "id": tarea.id, 
                        "Titulo": tarea.titulo_tarea, 
                        "Descripcion": tarea.descripcion, 
                        "Estado": tarea.estado_tarea 
                    } for tarea in tareas])


# Ruta para actualizar una tarea.
@app.route("/update_task/<int:id>", methods=["PUT"])
def update_task(id):
    tarea = Task.query.get_or_404(id)

    data = request.get_json()
    
    tarea.titulo_tarea = data.get('titulo_tarea', tarea.titulo_tarea)
    tarea.descripcion = data.get('descripcion', tarea.descripcion)
    tarea.estado_tarea = data.get('estado_tarea', tarea.estado_tarea)
    db.session.commit()
    
    return f"¡Tarea actualizada!\n{tarea.__repr__()}"

# Ruta para eliminar una tarea.
@app.route("/delete_task/<int:id>", methods=["DELETE"])
def delete_task(id):
    tarea = Task.query.get_or_404(id)
    
    db.session.delete(tarea)
    db.session.commit()
    
    return f"¡Tarea eliminada!\n{tarea.__repr__()}"

# Ruta para actualizar unicamente el estado de una tarea.
@app.route("/update_task_status/<int:id>", methods=["PUT"])
def update_task_status(id):
    tarea = Task.query.get_or_404(id)

    data = request.get_json()
    
    tarea.estado_tarea = data.get('estado_tarea', tarea.estado_tarea)
    db.session.commit()
    
    return f"¡Estado de la tarea actualizado!\n{tarea.__repr__()}"

# Ruta para obtener una tarea especifica
@app.route("/get_task/<int:id>", methods=["GET"])
def get_task(id):
    tarea = Task.query.get_or_404(id)
    
    return jsonify({
                        "id": tarea.id, 
                        "Titulo": tarea.titulo_tarea, 
                        "Descripcion": tarea.descripcion, 
                        "Estado": tarea.estado_tarea 
                    })

# Ruta para obtener todas las tareas con un estado especifico.
@app.route("/get_tasks_by_status/<string:estado>", methods=["GET"])
def get_tasks_by_status(estado):
    tareas = Task.query.filter_by(estado_tarea=estado).all()
    if tareas == []:
        return "No se encontraron tareas con ese estado."
    return jsonify([{
                        "id": tarea.id, 
                        "Titulo": tarea.titulo_tarea, 
                        "Descripcion": tarea.descripcion, 
                        "Estado": tarea.estado_tarea 
                    } for tarea in tareas])