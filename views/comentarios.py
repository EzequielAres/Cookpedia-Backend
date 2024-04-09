import flask_praetorian
from flask import request, abort, current_app

import sqlalchemy

from flask_restx import abort, Resource, Namespace

from model import db, Comentario, ComentarioSchema

# namespace declaration
api_comentario = Namespace("Comentarios", "Manejo de comentario")


@api_comentario.route("/<comentario_id>")
class ComentarioController(Resource):

    # Obtener comentario por ID
    @flask_praetorian.auth_required
    def get(self, comentario_id):
        comentario = Comentario.query.get_or_404(comentario_id)
        return ComentarioSchema().dump(comentario)

    # Eliminar comentario por ID
    @flask_praetorian.auth_required
    def delete(self, comentario_id):
        comentario = Comentario.query.get_or_404(comentario_id)
        db.session.delete(comentario)
        db.session.commit()

        return f"Comentario {comentario_id} eliminado", 204

    # Cambiar campos de un comentario
    @flask_praetorian.auth_required
    def put(self, comentario_id):
        new_comentario = ComentarioSchema().load(request.json)
        if str(new_comentario.id) != comentario_id:
            abort(400, "no coincide el id")

        db.session.commit()

        return ComentarioSchema().dump(new_comentario)


@api_comentario.route("/")
class ComentarioListController(Resource):

    # Obtener comentarios
    @flask_praetorian.auth_required
    def get(self):
        return ComentarioSchema(many=True).dump(Comentario.query.all())

    # Crear un comentario
    @flask_praetorian.auth_required
    def post(self):
        data = request.values

        # Comprobamos si el comentario va a tener una imagen y creamos el json
        if data["imagen"] == "":
            new_comment = {'usuario': data['usuario_id'], 'receta': data['receta_id'],
                           'contenido': data['contenido'], 'imagen': None}

        elif data['imagen'] != "":
            imagen = request.files['imagenFile']

            # Guardamos la imagen en el almacenamiento local y creamos el json
            carpeta = current_app.root_path
            imagen.save(carpeta + "/static/comentarios/" + imagen.filename)

            imagen_new_comment = "http://localhost:5000/static/comentarios/" + imagen.filename

            new_comment = {'usuario': data['usuario_id'], 'receta': data['receta_id'],
                           'contenido': data['contenido'], 'imagen': imagen_new_comment}

        # Comprobamos si el comentario es hijo de otro y añadimos el campo al json
        if data['padre_id'] != "":
            new_comment['padre'] = data['padre_id']
        elif data['padre_id'] == "":
            new_comment['padre'] = None

        comment = ComentarioSchema().load(new_comment)

        # Guardamos el comentario
        db.session.add(comment)
        db.session.commit()
        return ComentarioSchema().dump(comment), 201


@api_comentario.route("/padre/<receta_id>")
class ComentarioController(Resource):

    # Obtener todos los comentarios que no son hijos de otros de una receta
    def get(self, receta_id):

        # Sentencia sql para filtrar los comentarios
        query = sqlalchemy.text(
            'SELECT c.*, u.imagen as imagenUsuario, u.nombre nombreUsuario FROM comentario c, usuario u JOIN '
            'receta r on c.receta_id = r.id WHERE r.id = :receta_idRequest AND c.padre_id IS NULL '
            'AND u.id = c.usuario_id ORDER BY c.id desc')
        result = db.session.execute(query, {"receta_idRequest": receta_id})
        resultMapping = result.mappings().all()

        # Devolvemos todos los comentarios con el formato indicado
        return {r["id"]: [{"id": r["id"], "usuario_id": r["usuario_id"], "receta_id": r["receta_id"],
                           "imagenUsuario": r["imagenUsuario"],
                           "nombreUsuario": r["nombreUsuario"], "imagen": r["imagen"], "contenido": r["contenido"]}]
                for r in resultMapping}


@api_comentario.route("/hijo/<receta_id>")
class ComentarioController(Resource):

    # Obtener todos los comentarios que son hijos de otros de una receta
    def get(self, receta_id):

        # Sentencia sql para filtrar los comentarios
        query = sqlalchemy.text(
            'SELECT c.*, u.imagen as imagenUsuario, u.nombre as nombreUsuario FROM comentario c, usuario u JOIN receta '
            'r on c.receta_id = r.id WHERE r.id = :receta_idRequest AND c.padre_id IS NOT NULL AND u.id = c.usuario_id '
            'ORDER BY c.id desc')
        result = db.session.execute(query, {"receta_idRequest": receta_id})
        resultMapping = result.mappings().all()

        # Devolvemos todos los comentarios con el formato indicado
        return {r["id"]: [
            {"id": r["id"], "usuario_id": r["usuario_id"], "receta_id": r["receta_id"], "padre_id": r["padre_id"],
             "imagenUsuario": r["imagenUsuario"], "nombreUsuario": r["nombreUsuario"], "imagen": r["imagen"],
             "contenido": r["contenido"]}] for r in resultMapping}
