from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth

appCar = Flask(__name__)

appCar.config.from_object(Config)

appCar.register_blueprint(site)
appCar.register_blueprint(auth)