import sys
sys.path.append("C:/Users/900223/Desktop/apiSquads/")


from flask import Flask
from flask_restful import Api
from controllers.squadsController import SquadsController


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
api.add_resource(SquadsController, '/api/programadores', endpoint='programadores')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(SquadsController, '/api/programadores/<int:id>', endpoint='programador')

#########################################################################################


# Rota Squad Controller - Listar todos/inserir
api.add_resource(SquadsController, '/api/linguagens', endpoint='linguagens')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(SquadsController, '/api/linguagens/<int:id>', endpoint='linguagem')


#########################################################################################


# Rota Squad Controller - Listar todos/inserir
api.add_resource(SquadsController, '/api/frameworks', endpoint='frameworks')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(SquadsController, '/api/frameworks/<int:id>', endpoint='framework')


###########################################################################################


# Rota Squad Controller - Listar todos/inserir
api.add_resource(SquadsController, '/api/bancos_dados', endpoint='bancos_dados')

# Rota Squad Controller - Buscar por id/deletar/alterar
api.add_resource(SquadsController, '/api/bancos_dados/<int:id>', endpoint='banco_dados')


app.run(port=80, debug=True)