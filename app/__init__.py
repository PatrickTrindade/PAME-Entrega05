from flask import Flask
from .config import Config
from .extensions import db, migrate

from app.pet.controllers import pet_api
from app.produtos.controllers import produtos_api
from app.servico.controllers import servico_api
from app.usuario.controllers import usuario_api
from app.van.controllers import van_api

'''
from .pet.model import Pet
from .produtos.model import Produtos
from .servico.model import Servico
from .usuario.model import Usuario
from .van.model import Van
'''

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(pet_api)
    app.register_blueprint(servico_api)


    return app