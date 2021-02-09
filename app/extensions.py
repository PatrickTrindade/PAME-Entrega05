from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask import Blueprint, request, jsonify -> tem no arquivo do html.3

db = SQLAlchemy()
migrate = Migrate()