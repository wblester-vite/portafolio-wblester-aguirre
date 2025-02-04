from flask import Flask

# Importante: define la carpeta estática y de plantillas
app = Flask(__name__, static_folder='static', template_folder='templates')

from app import routes

