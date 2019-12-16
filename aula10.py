import sys
sys.path.append("C:/Users/900223/Desktop/apiSquads/")


from flask import Flask
from flask_restful import Api
from controllers.squadsController import SquadsController
from controllers.buscaController import BuscaController


app = Flask(__name__)

api = Api(app)


# Mateus = framework: angular, linguagem: python, db: mongo
# Tiago = framework: vue, linguagem: java, db: postgree
# Nicole = framework: react, linguagem: php, db: mysqlserver


# Rota Squad Controller - Listar todos/inserir
api.add_resource(SquadsController, '/api/squads', endpoint='squads')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(SquadsController, '/api/squads/<int:id>', endpoint='squad')


######################################################################################## 


# Rota Programadores - Listar todos/inserir
api.add_resource(BuscaController, '/api/listagem/<string:tabela>', endpoint='listas')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(BuscaController, '/api/listar/<string:tabela>/<int:id>', endpoint='lista')



app.run(port=80, debug=True)