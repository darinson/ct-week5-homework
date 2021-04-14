from flask import Flask
from config import Config

from .site.routes import site
from .authentication.routes import auth

from flask_migrate import Migrate
from .models import db as root_db

appCar = Flask(__name__)

appCar.config.from_object(Config)

appCar.register_blueprint(site)
appCar.register_blueprint(auth)

root_db.init_app(appCar)
migrate = Migrate(appCar, root_db)

from car_inventory import models