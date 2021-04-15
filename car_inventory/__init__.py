from flask import Flask
from config import Config

from .site.routes import site
from .authentication.routes import auth
from .api.routes import api


from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma

from flask_cors import CORS #prevent malware from possible sources. 

from .helpers import JSONEncoder

appCar = Flask(__name__)

appCar.config.from_object(Config)

appCar.register_blueprint(site)
appCar.register_blueprint(auth)
appCar.register_blueprint(api)

root_db.init_app(appCar)
migrate = Migrate(appCar, root_db)

login_manager.init_app(appCar)
login_manager.login_view = 'auth.signin'

ma.init_app(appCar)

CORS(appCar)

appCar.json_encoder = JSONEncoder

from car_inventory import models