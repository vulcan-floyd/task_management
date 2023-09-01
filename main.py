import importlib
import os

from flask import Flask, jsonify, request, g

from api_views import blueprints
from config import config
from extensions import swagger, db
from flask_migrate import Migrate

def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])
    application.config.from_pyfile(".env", silent=False)
    for i in application.config:
        os.environ[i] = str(application.config[i])
    
    db.init_app(application)
    with application.app_context():
        db.create_all()
    return application

def init_api(application):
    for i in application.config:
        os.environ[i] = str(application.config[i])
        
    application.url_map.strict_slashes = False
    swagger.init_app(application)
    print(blueprints)
    for path, blueprint, url_prefix in blueprints:
        module = importlib.import_module(path)
        print(module, blueprint)
        application.register_blueprint(
            getattr(module, blueprint), url_prefix=url_prefix)
        
    @application.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text=str(e)), 404

    @application.errorhandler(500)
    def application_error(e):
        return jsonify(error=500, text="Application error"), 500

    @application.errorhandler(400)
    def client_error(e):
        return jsonify(error=400, text=str(e)), 400

    return application