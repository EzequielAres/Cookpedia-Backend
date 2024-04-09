from flask import Flask, jsonify, request
import flask_praetorian
from model import init_db, Usuario
from views import blueprint as api


def create_app(config_file='config.py'):
    # instantiate praetorian object
    guard = flask_praetorian.Praetorian()
    # instantiate flask app
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    # get configuration parameters
    app.config.from_pyfile(config_file)

    # praetorian init
    guard.init_app(app, Usuario)

    # SQLAlchemy init
    init_db(app, guard, 'tests' in config_file)

    # register blueprint
    app.register_blueprint(api, url_prefix="/api/")

    @app.route("/")
    def home():
        """
        Home page

        Send static file with link to api to avoid 404 on /
        """
        return app.send_static_file("index.html")

    # authentication system
    @app.route("/login", methods=['POST'])
    def login():
        """
        Process login requests

        Get login credentials from body using json
        Parameters: username and password
        """

        # get username and password from body (json)
        nombre = request.json.get('nombre')
        password = request.json.get('password')

        # praetorian authentication
        user = guard.authenticate(nombre, password)

        id = user.id;
        admin = user.is_admin

        # get JWT from praetorian
        ret = {"access_token": guard.encode_jwt_token(user),
               "id": id,
               "admin" : admin}

        # return JWT
        return jsonify(ret), 200

    return app

if __name__ == '__main__':
    # starts app
    # in production: debug=False
    app.create_app()
    app.run(debug=True)
