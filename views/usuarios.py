import flask_praetorian
from flask import request, abort, current_app

from flask_restx import abort, Resource, Namespace

from model import Usuario, db, UsuarioSchema

# namespace declaration
api_usuario = Namespace("Usuarios", "Manejo de usuario")


@api_usuario.route("/<user_id>")
class UsuarioController(Resource):

    # Obtener usuario por ID
    def get(self, user_id):
        user = Usuario.query.get_or_404(user_id)
        return UsuarioSchema().dump(user)

    # Eliminar usuario por ID
    @flask_praetorian.auth_required
    def delete(self, user_id):
        user = Usuario.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return f"Usuario {user_id} eliminado", 204

    # Cambiar campos usuario
    @flask_praetorian.auth_required
    def put(self, user_id):
        data = request.values

        # Comprobamos si vamos a cambiar la imagen del usuario y la contraseña, dependiendo del request
        # formaremos un json con los datos que vamos a cambiar
        if data['imagen'] != "":
            if data['hashed_password'] != "":
                new_user = {"id": user_id, "nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                            "hashed_password": data["hashed_password"], "imagen": data["imagen"]}
            else:
                new_user = {"id": user_id, "nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                            "imagen": data["imagen"]}

        elif data['imagen'] == "":
            imagen = request.files['nuevaImagen']

            # Guardamos la imagen en el almacenamiento local
            carpeta = current_app.root_path
            imagen.save(carpeta + "/static/usuarios/" + imagen.filename)

            imagen_new_user = "http://localhost:5000/static/usuarios/" + imagen.filename

            if data['hashed_password'] != "":
                new_user = {"id": user_id, "nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                            "hashed_password": data["hashed_password"], "imagen": imagen_new_user}
            else:
                new_user = {"id": user_id, "nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                            "imagen": imagen_new_user}

        new_user = UsuarioSchema().load(new_user)

        # Cargamos el usuario y comprobamos que los ID coinciden
        if str(new_user.id) != user_id:
            abort(400, "no coincide el id")

        # Si vamos a cambiar la contraseña debemos hashearla con praetorian
        if data["hashed_password"] != "":
            guard = flask_praetorian.Praetorian()
            guard.init_app(current_app, Usuario)
            new_user.hashed_password = guard.hash_password(new_user.hashed_password)

        db.session.commit()

        return UsuarioSchema().dump(new_user)


@api_usuario.route("/")
class UsuarioListController(Resource):

    # Obtener todos los usuarios
    @flask_praetorian.auth_required
    def get(self):
        return UsuarioSchema(many=True).dump(Usuario.query.all())

    # Crear un usuario
    def post(self):
        data = request.values

        # Hacemos un try para poder comprobar si el usuario ha introducido una imagen
        try:
            imagen = request.files['imagen']

            # Guardamos la imagen en el almacenamiento local y creamos el json
            carpeta = current_app.root_path
            imagen.save(carpeta + "/static/usuarios/" + imagen.filename)

            imagen_new_user = "http://localhost:5000/static/usuarios/" + imagen.filename

            new_user = {"nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                        "hashed_password": data["hashed_password"], "imagen": imagen_new_user}

        # Si no hemos introducido imagen cargamos una por defecto
        except KeyError:
            imagen = "http://localhost:5000/static/usuarios/anon.jpg"

            new_user = {"nombre": data["nombre"], "nick": data["nick"], "email": data["email"],
                        "hashed_password": data["hashed_password"], "imagen": imagen}

        user = UsuarioSchema().load(new_user)

        # Hasheamos la contraseña y guardamos el usuario
        guard = flask_praetorian.Praetorian()
        guard.init_app(current_app, Usuario)
        user.hashed_password = guard.hash_password(user.hashed_password)

        db.session.add(user)
        db.session.commit()
        return UsuarioSchema().dump(user), 201
