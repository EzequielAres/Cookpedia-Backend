from flask import Blueprint
from flask_restx import Api

from .comentarios import api_comentario
from .likes import api_like
from .usuarios import api_usuario
from .recetas import api_receta
from .ingredientes import api_ingrediente


# one blueprint (Flask) for all the resources
blueprint = Blueprint('RecipeProject', __name__)
api = Api(blueprint, title="RecipeProject", version="1.0", description="RecipeProject", doc="/docs")

# every resource in a namespace (RestX)
api.add_namespace(api_usuario, path='/usuario')
api.add_namespace(api_receta, path='/receta')
api.add_namespace(api_ingrediente, path='/ingrediente')
api.add_namespace(api_like, path='/like')
api.add_namespace(api_comentario, path='/comentario')
