import json

import flask_praetorian
from flask import request, abort, current_app

import sqlalchemy

from flask_restx import abort, Resource, Namespace

from model import Receta, db, RecetaSchema, Ingrediente, IngredienteReceta, Like

# namespace declaration
api_receta = Namespace("Recetas", "Manejo de receta")


@api_receta.route("/<recipe_id>")
class RecetaController(Resource):

    # Obtener receta por ID
    def get(self, recipe_id):

        # Sentencia sql para obtener los datos necesarios de una receta
        query = sqlalchemy.text('SELECT r.id, r.nombre, r.descripcion, r.imagen, r.video, r.pasos, r.id_usuario '
                                'as id_usuario, count(l.id) as likis, u.nombre as nombreUsuario FROM receta r, like l, '
                                'usuario u WHERE r.id = :recipe_idRequest AND r.id = l.receta_id AND r.id_usuario = '
                                'u.id GROUP BY r.id;')

        result = db.session.execute(query, {"recipe_idRequest": recipe_id})
        resultMapping = result.mappings().all()
        r = resultMapping[0]

        # Con esta serie de if comprobamos los diferentes campos de la receta, ya que hay campos opcionales
        # formamos el json dependiendo de los valores
        if r["video"] is not None:
            if r["pasos"] is not None:
                recipe = {"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                          "nombreUsuario":
                              r["nombreUsuario"], "id_usuario": r["id_usuario"], "descripcion": r["descripcion"],
                          "video": r["video"], "pasos": r["pasos"]}
            else:
                recipe = {"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                          "nombreUsuario":
                              r["nombreUsuario"], "id_usuario": r["id_usuario"], "descripcion": r["descripcion"],
                          "video": r["video"]}
        else:
            if r["pasos"] is not None:
                recipe = {"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                          "nombreUsuario":
                              r["nombreUsuario"], "id_usuario": r["id_usuario"], "descripcion": r["descripcion"],
                          "pasos": r["pasos"]}
            else:
                recipe = {"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                          "nombreUsuario":
                              r["nombreUsuario"], "id_usuario": r["id_usuario"], "descripcion": r["descripcion"]}

        return recipe

    # Eliminar receta por ID
    @flask_praetorian.auth_required
    def delete(self, recipe_id):
        receta = Receta.query.get_or_404(recipe_id)
        db.session.delete(receta)
        db.session.commit()

        return f"Receta {recipe_id} eliminada", 204

    # Cambiar valores receta
    @flask_praetorian.auth_required
    def put(self, recipe_id):
        new_recipe = RecetaSchema().load(request.json)
        if str(new_recipe.id) != recipe_id:
            abort(400, "no coincide el id")

        db.session.commit()

        return RecetaSchema().dump(new_recipe)


@api_receta.route("/")
class RecetaListController(Resource):

    # Obtener recetas
    def get(self):
        return RecetaSchema(many=True).dump(Receta.query.all())

    # Crear receta
    @flask_praetorian.auth_required
    def post(self):
        data = request.values
        imagen = request.files['imagen']

        # Guardamos la imagen en el almacenamiento local
        carpeta = current_app.root_path
        imagen.save(carpeta + "/static/recetas/" + imagen.filename)
        imagen_new_user = "http://localhost:5000/static/recetas/" + imagen.filename

        # Hacemos un try para comprobar si el usuario ha introducido video
        try:
            # Guardamos el vídeo en el almacenamiento local
            video = request.files['video']
            video.save(carpeta + "/static/recetas/" + video.filename)
            video_new_user = "http://localhost:5000/static/recetas/" + video.filename

            # Formamos el json de la nueva receta según los campos introducidos
            if data["pasos"] != "":
                new_recipe = {"nombre": data["nombre"], "descripcion": data["descripcion"], "imagen": imagen_new_user,
                              "pasos": data["pasos"], "video": video_new_user, "usuario": data["id_usuario"]}

            elif data["pasos"] == "":
                new_recipe = {"nombre": data["nombre"], "descripcion": data["descripcion"], "imagen": imagen_new_user,
                              "video": video_new_user, "usuario": data["id_usuario"]}

        except KeyError:
            # Formamos el json de la nueva receta según los campos introducidos
            new_recipe = {"nombre": data["nombre"], "descripcion": data["descripcion"], "imagen": imagen_new_user,
                          "pasos": data["pasos"], "usuario": data["id_usuario"]}

        # Añadimos la receta a la base de datos
        receta = RecetaSchema().load(new_recipe)
        db.session.add(receta)

        # Hacemos un try para comprobar si se han introducido correctamente los ingredientes
        try:

            # Cargamos los ingredientes en un objeto y creamos listas vacías que usaremos ahora
            ingredientes = json.loads(data["ingredientes"])
            listaIngredientes = []
            listaIngredientesReceta = []

            # Recorremos los ingredientes añadiendo a listaIngredientes los objetos ingredientes ya cargados
            # de la base de datos y su cantidad
            for r in ingredientes:
                listaIngredientes.append(
                    {"ingrediente": Ingrediente.query.filter(Ingrediente.id.in_([r["ingrediente_id"]])).all()[0],
                     "cantidad": r["cantidad"]})

            # Ahora recorremos la lista para añadir a ListaIngredientesReceta los valores necesarios para
            # rellenar la tabla externa con el ID de la receta, el ID del ingrediente y la cantidad correspondiente
            for ingrediente in listaIngredientes:
                listaIngredientesReceta.append(
                    IngredienteReceta(receta_id=receta.id, ingrediente_id=ingrediente["ingrediente"].id,
                                      cantidad=ingrediente["cantidad"]))

            # Creamos también el like del usuario a la receta creada, ya que es necesario por como está
            # estructurado el código
            like = Like(usuario_id=data["id_usuario"], receta_id=receta.id)

            # Guardamos en la base de datos los ingredientes y like creados
            db.session.bulk_save_objects(listaIngredientesReceta)
            db.session.add(like)
        except KeyError:
            print("SinIngredientes")
        db.session.commit()

        return RecetaSchema().dump(receta), 201


@api_receta.route("/list")
class RecetaListController(Resource):

    # Obtener todas las recetas ordenadas por un filtro
    def get(self):
        order = request.args.get('order')

        # Obtenemos el filtro que nos indica el usuario y ejecutamos la sentencia sql correspondiente
        # luego creamos el json con las distintas recetas
        if order == "date":
            query = sqlalchemy.text('SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as '
                                    'nombreUsuario FROM receta r, like l, usuario u WHERE r.id = l.receta_id '
                                    'AND u.id = r.id_usuario group by r.id order by r.id desc')

            result = db.session.execute(query)
            resultMapping = result.mappings().all()

            return {r["id"]: [{"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                               "nombreUsuario": r["nombreUsuario"]}] for r in resultMapping}

        elif order == "likes":
            query = sqlalchemy.text('SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as '
                                    'nombreUsuario FROM receta r, like l, usuario u WHERE r.id = l.receta_id '
                                    'AND u.id = r.id_usuario group by r.id order by likis desc')

            result = db.session.execute(query)
            resultMapping = result.mappings().all()

            return {r["nombre"]: [{"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                                   "nombreUsuario": ["nombreUsuario"]}] for r in resultMapping}


@api_receta.route("/count")
class RecetaListController(Resource):

    # Obtenemos la cantidad de recetas que hay en la base de datos
    def get(self):
        count = Receta.query.count()
        return count


@api_receta.route("/search/<string:name>")
class RecetaController(Resource):

    # Obtenemos las recetas filtradas por búsqueda y ordenadas por el filtro indicado
    def get(self, name):
        order = request.args.get('order')
        name = '%' + name + '%'

        # Introducimos la sentencia sql dependiendo del filtro que hayamos indicado
        if order == "date":
            query = sqlalchemy.text('SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as '
                                    'nombreUsuario FROM receta r, like l, usuario u WHERE r.id = l.receta_id AND '
                                    'u.id = r.id_usuario AND r.nombre LIKE :nameRequest group by r.id '
                                    'order by r.id desc')

        elif order == "likes":
            query = sqlalchemy.text('SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as '
                                    'nombreUsuario FROM receta r, like l, usuario u WHERE r.id = l.receta_id AND '
                                    'u.id = r.id_usuario AND r.nombre LIKE :nameRequest group by r.id '
                                    'order by likis desc')

        result = db.session.execute(query, {"nameRequest": name})
        resultMapping = result.mappings().all()

        # Devolvemos las recetas con el siguiente formato
        return {r["id"]: [{"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                           "nombreUsuario": r["nombreUsuario"]}] for r in resultMapping}


@api_receta.route("/home")
class RecetaController(Resource):

    # Obtenemos las últimas 6 recetas creadas por los usuarios
    def get(self):
        count = Receta.query.count()

        # Sentencia sql para obtener las últimas 6 recetas
        query = sqlalchemy.text(
            'SELECT r.id, r.nombre as nombre, r.imagen, count(l.id) as likis, u.nombre as nombreUsuario FROM receta r, '
            'like l, usuario u WHERE r.id = l.receta_id AND u.id = r.id_usuario AND r.id BETWEEN (:count-5) AND :count '
            'group by r.id order by r.id desc')

        result = db.session.execute(query, {"count": count})
        resultMapping = result.mappings().all()

        # Devolvemos las recetas con el siguiente formato
        return {r["id"]: [{"id": r["id"], "nombre": r["nombre"], "imagen": r["imagen"], "likes": r["likis"],
                           "nombreUsuario": r["nombreUsuario"]}] for r in resultMapping}
