import flask_praetorian
from flask import request, abort

import sqlalchemy

from flask_restx import abort, Resource, Namespace

from model import db, Like, LikeSchema

# namespace declaration
api_like = Namespace("Likes", "Manejo de like")


@api_like.route("/receta/<receta_id>")
class LikeController(Resource):

    # Obtener likes de una receta
    def get(self, receta_id):
        # Sentencia sql para filtrar likes de una receta
        query = sqlalchemy.text('SELECT count(l.id) as "likes" FROM like l JOIN receta r on l.receta_id = r.id '
                                'WHERE r.id = :receta_idRequest')
        result = db.session.execute(query, {"receta_idRequest": receta_id})
        resultMapping = result.mappings().all()

        # Devolvemos los likes con el siguiente formato
        return {"likes": resultMapping[0]["likes"]}


@api_like.route("/recetas/<user_id>")
class LikeController(Resource):

    # Obtener recetas a las que un usuario ha dado like
    def get(self, user_id):
        # Sentencia sql para filtrar las recetas a las que ha dado like un usuario
        query = sqlalchemy.text(
            'SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as nombreUsuario FROM receta r, '
            'like l, usuario u WHERE r.id IN (SELECT receta_id FROM like WHERE usuario_id = :user_idRequest) '
            'AND r.id = l.receta_id AND r.id_usuario = u.id AND r.id_usuario != :user_idRequest group by r.id;')

        result = db.session.execute(query, {"user_idRequest": user_id})
        resultMapping = result.mappings().all()

        # Devolvemos las recetas con el siguiente formato
        return {r["id"]: [{"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                           "nombreUsuario": r["nombreUsuario"]}] for r in resultMapping}


@api_like.route("/tiene/<recipe_id>/<user_id>")
class LikeController(Resource):

    # Obtener id de like y booleano dependiendo de si un usuario ha hecho like a una receta
    def get(self, recipe_id, user_id):

        # Sentencia sql para filtrar el resultado
        query = sqlalchemy.text(
            'SELECT * FROM like WHERE receta_id = :recipe_idRequest AND usuario_id = :user_idRequest;')

        result = db.session.execute(query, {"recipe_idRequest": recipe_id, "user_idRequest": user_id})
        resultMapping = result.mappings().all()

        # Comprobamos si el usuario ha hecho like y devolvemos el json correspondiente
        if len(resultMapping) > 0:
            return {"result": True, "idLike": resultMapping[0].id}

        return {"result": False, "idLike": ""}


@api_like.route("/<like_id>")
class LikeController(Resource):

    # Obtener like por ID
    @flask_praetorian.auth_required
    def get(self, like_id):
        like = Like.query.get_or_404(like_id)
        return LikeSchema().dump(like)

    # Eliminar like por ID
    @flask_praetorian.auth_required
    def delete(self, like_id):
        like = Like.query.get_or_404(like_id)
        db.session.delete(like)
        db.session.commit()

        return f"Like {like_id} eliminado", 204

    # Cambiar campos like
    def put(self, like_id):
        new_like = LikeSchema().load(request.json)
        if str(new_like.id) != like_id:
            abort(400, "no coincide el id")

        db.session.commit()

        return LikeSchema().dump(new_like)


@api_like.route("/")
class LikeListController(Resource):

    # Obtener likes
    @flask_praetorian.auth_required
    def get(self):
        return LikeSchema(many=True).dump(Like.query.all())

    # Crear like
    @flask_praetorian.auth_required
    def post(self):
        like = LikeSchema().load(request.json)

        db.session.add(like)
        db.session.commit()
        return LikeSchema().dump(like), 201
