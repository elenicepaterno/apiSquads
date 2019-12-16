import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from flask import Flask
from flask_restful import Api
from controllers.bebidaController import BebidaController
from controllers.tipo_bebidaController import TipoBebidaController


app = Flask(__name__)

api = Api(app)

# Rota Bebida Controller - Listar todos/inserir
api.add_resource(BebidaController, '/api/bebida', endpoint='bebidas')

# Rota Bebida Controller - Buscar por id/deletar/alterar
api.add_resource(BebidaController, '/api/bebida/<int:id>', endpoint='bebida')


#########################################################################


# Rota Tipo Bebida Controller - Listar todos
api.add_resource(TipoBebidaController, '/api/tipo_bebida', endpoint='tipo_bebida')

# Rota Tipo Bebida Controller - Buscar por id/deletar/alterar
api.add_resource(TipoBebidaController, '/api/tipo_bebida/<int:id>', endpoint='tipo_bebidas')


app.run(port=80, debug=True)


