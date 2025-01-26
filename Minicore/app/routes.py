from flask import Blueprint
from app.Controllers.core_controller import recomendaciones_basicas

routes = Blueprint('routes', __name__)

routes.add_url_rule('/', 'recomendaciones', recomendaciones_basicas, methods=['GET', 'POST'])
